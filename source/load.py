import psycopg2
from psycopg2 import sql

db_params = {
    'host': 'your_host',
    'database': 'your_database',
    'user': 'your_user',
    'password': 'your_password',
    'port': 'your_port',
}

def insertSourceMetadata(source_uri, source_name, title):
  conn = psycopg2.connect(**db_params)
  cur = conn.cursor()

  col_name = "source_uri source_name source_title"
  table_name = "source_metadata"

  query = "INSERT INTO {} ({}) VALUES (%s, %s, %s) RETURNING id;"
  query = query.format(table_name, col_name)

  cur.execute(query, (source_uri, source_name, title))
  source_id = cur.fetchone()[0]
  conn.commit()

  return source_id

def insertChunkData(source_id, chunk):
  conn = psycopg2.connect(**db_params)
  cur = conn.cursor()

  col_name = "source_id, content"
  table_name = "source_metadata"

  query = "INSERT INTO {} ({}) VALUES (%s, %s, %s) RETURNING id;"
  query = query.format(table_name, col_name)

  cur.execute(query, (source_id, chunk))
  source_id = cur.fetchone()[0]
  conn.commit()

  return source_id  