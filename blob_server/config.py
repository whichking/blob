from os import getenv

SQL_USER = getenv('BLOB_SQL_USER', 'blob_user')
SQL_PASSWORD = getenv('BLOB_SQL_PASSWORD', 'test_blob_pw')
SQL_DB_NAME = getenv('BLOB_SQL_DB_NAME', 'blob_db')
SQL_DB_PORT = getenv('BLOB_SQL_DB_PORT', '5432')
SQL_DB_HOST = getenv('BLOB_SQL_DB_HOST', 'localhost')

