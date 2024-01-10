import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()

db_params = {
    'host': os.getenv('DB_HOST'),
    'database':  os.getenv('DB_DATABASE'),
    'user':  os.getenv('DB_USER'),
    'password':  os.getenv('DB_PASSWORD'),
    'port':  os.getenv('DB_PORT'),
}

def insertSourceMetadata(source_uri, source_name, title):
  conn = psycopg2.connect(**db_params)
  cur = conn.cursor()

  col_name = "source_uri, source_name, source_title"
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
  table_name = "data"

  query = "INSERT INTO {} ({}) VALUES (%s, %s) RETURNING id;"
  query = query.format(table_name, col_name)

  cur.execute(query, (source_id, chunk))
  source_id = cur.fetchone()[0]
  conn.commit()

  return source_id  