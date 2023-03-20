import psycopg2

try:
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'doan3_db',
        user = 'postgres',
        password = 'doremon0',
        port = 5432
    )
except Exception as error:
    print(error)

conn.close()
