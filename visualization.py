import psycopg2
import matplotlib.pyplot as plt

username = 'user'
password = 'password'
database = 'db_lab_2'
host = 'localhost'
port = '5432'

query_1 = 'select trim(company_name), count(bar_id) from bars group by company_name;'

query_2 = 'select company_country, count(company_name) from companies group by company_country;'

query_3 = 'select rating, count(rating) from reviews group by rating;'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

figure, (bar1_ax, pie_ax, bar2_ax) = plt.subplots(1, 3)

with conn:
    cur = conn.cursor()
    
    cur.execute(query_1)
    manufacturers = []
    barsAmount = []

    for row in cur:
        manufacturers.append(row[0])
        barsAmount.append(row[1])

    x_range = range(len(manufacturers))

    bar1_ax.bar(x_range, barsAmount, label='Total')
    bar1_ax.set_xlabel('Виробник')
    bar1_ax.set_ylabel('Кількість плиток')
    bar2_ax.set_title('Кількість видів плиток у кожного виробника')
    bar1_ax.set_xticks(x_range)
    bar1_ax.set_xticklabels(manufacturers)


    cur.execute(query_2)
    countries = []
    count = []
    for row in cur:
        countries.append(row[0])
        count.append(row[1])
    pie_ax.pie(count, labels=countries, autopct='%1.1f%%')
    pie_ax.set_title('Частка плиток по країнах')

    cur.execute(query_3)
    rating = []
    amount = []

    for row in cur:
        rating.append(row[0])
        amount.append(row[1])

    x_range = range(len(rating))

    bar2_ax.bar(x_range, amount, label='Total')
    bar2_ax.set_xlabel('Оцінка')
    bar2_ax.set_ylabel('Кількість')
    bar2_ax.set_title('Кількість кожної з оцінок')
    bar2_ax.set_xticks(x_range)
    bar2_ax.set_xticklabels(rating)

    mng = plt.get_current_fig_manager()
    mng.resize(1400, 600)

    plt.show()