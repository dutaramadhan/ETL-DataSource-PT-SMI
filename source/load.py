import psycopg2
from psycopg2 import sql

db_params = {
    'host': 'your_host',
    'database': 'your_database',
    'user': 'your_user',
    'password': 'your_password',
    'port': 'your_port',
}

def loadSourceMetadata(source_uri, source_name, title):
  conn = psycopg2.connect(**db_params)
  cur = conn.cursor()

  col_name = "source_uri source_name source_title"
  table_name = "source_metadata"

  query = "INSERT INTO {} ({}) VALUES ({}) RETURNING id;"
  query = query.format(table_name, col_name, ' '.join([source_uri, source_name, title]))

  cur.execute(query)
  source_id = cur.fetchone()[0]
  conn.commit()

  return source_id

def loadChunkData(source_id, splitted_text):
  conn = psycopg2.connect(**db_params)
  cur = conn.cursor()

  col_name = "source_id content"
  table_name = "data"

  query = "INSERT INTO {} ({}) VALUES ({}, %s)"
  query = query.format(table_name, col_name, source_id)

  for text in splitted_text:
    cur.execute(query, text)
  conn.commit()