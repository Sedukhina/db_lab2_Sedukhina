import psycopg2

username = 'user'
password = 'password'
database = 'db_lab_2'
host = 'localhost'
port = '5432'

query_1 = 'select company_name, count(bar_id) from bars group by company_name;'

query_2 = 'select company_country, count(company_name) from companies group by company_country;'

query_3 = 'select rating, count(rating) from reviews group by rating;'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    print('Query 1: ')
    cur = conn.cursor()
    cur.execute(query_1)
    for row in cur:
        print(row)

    print("")

    print('Query 2: ')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print("")

    print('Query 3: ')
    cur.execute(query_3)
    for row in cur:
        print(row)