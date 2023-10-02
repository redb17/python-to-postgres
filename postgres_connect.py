import psycopg2


conn = psycopg2.connect(
    user='postgres',
    password='pg123',
    host='172.17.0.2', # Postgres docker container IP
    port='5432',
    database='education'
)

cursor = conn.cursor()


def ingest(table, rows, tables_cols):
    print('Ingesting:', table)
    cols_str = ','.join(tables_cols[table])
    
    total = len(rows)
    segment = 500

    # avoiding 'Packet Too Large' error by executing the insert in segments of 100 rows
    for i in range(0, total, segment):
        to = min(i+segment, total)
        segment_rows = rows[i: to]
        vals_str = '),('.join([str(row)[1:-1] for row in segment_rows])

        insert_query = f'''
            INSERT INTO {table} ({cols_str})
            VALUES ({vals_str});
        '''

        cursor.execute(insert_query, None)
        conn.commit()
        print('Ingested to:', to)
