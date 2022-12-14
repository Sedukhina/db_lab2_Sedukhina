--Скільки видів плиток випускає кожна компанія
select trim(company_name), count(bar_id) from bars group by company_name;

--Розприділення компаній по країнах
select company_country, count(company_name) from companies group by company_country;

--Кількість кожної з оцінок
select rating, count(rating) from reviews group by rating;
