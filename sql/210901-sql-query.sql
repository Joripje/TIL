use SSAC;

create table user(
    user_id int primary key auto_increment,
    name varchar(30) not null
);

create table addr(
	addr_id int primary key auto_increment,
    addr_name varchar(30) not null,
    user_id int not null
);

insert into user(name)
values ('jin'), ('po'), ('alice');
select * from user;

insert into addr(addr_name, user_id)
values ('seoul', 1), ('pusan', 2), ('daegu', 4), ('seoul', 5);
select * from addr;

# inner join
select user.user_id, user.name, addr.addr_name
from user
join addr
where user.user_id = addr.user_id;

select user.user_id, user.name, addr.addr_name
from user
join addr
on user.user_id = addr.user_id;

# left join
select user.user_id, user.name, addr.addr_name
from user
left join addr
on user.user_id = addr.user_id;

# right join
select addr.user_id, user.name, addr.addr_name
from user
right join addr
on user.user_id = addr.user_id;

# 국가코드, 국가이름, 국가인구, 도시이름, 도시 인구 출력
use world;
SELECT *
FROM country;
SELECT *
FROM city;

SELECT country.code, country.name, country.population, city.name, city.population
FROM country
JOIN city
ON country.code = city.countrycode;

SELECT country.code, country.name, country.population, city.name, city.population
FROM country
JOIN city
ON country.code = city.countrycode
HAVING city.population >= 5000000
ORDER BY city.population DESC;

SELECT country.code, country.name, country.population
       , city.name, city.population
       , ROUND(city.population / country.population * 100, 2) AS rate
FROM country
JOIN city
ON country.code = city.countrycode
HAVING city.population >= 5000000
ORDER BY rate DESC;

# 스태프 아이디, 스태프 풀네임, 매출액
use sakila;
select *
from payment;
select *
from staff;

select staff.staff_id
       , concat(first_name, ' ', last_name) AS fullname
       , payment.amount
from staff
join payment
on staff.staff_id = payment.staff_id;

# 스태프별 발생한 총 매출을 출력
select staff.staff_id
       , concat(first_name,' ', last_name) AS fullname
       , sum(amount)
from staff
join payment
on staff.staff_id = payment.staff_id
group by staff.staff_id, fullname;

#테이블 세개 조인
# 국가이름, 도시이름, 사용언아, 사용언어 비율
use world;

select country.name as country_name, city.name as city_name
       , language, percentage
from country
join city
on country.code = city.countrycode
join countrylanguage
on country.code = countrylanguage.countrycode;

select country.name as country_name, city.name as city_name
       , language, percentage
from country, city, countrylanguage
where country.code = city.countrycode
      and country.code = countrylanguage.countrycode;

# 국가의 언어 사용 비율을 도시의 언어 사용비율과 같다고 가정할때 도시의 언어 사용인구를 출력      
select country.name as country_name, city.name as city_name
	   , countrylanguage.language, countrylanguage.percentage
       , round(city.population * countrylanguage.percentage / 100, 0) as rate
from country, city, countrylanguage
where country.code = city.countrycode 
      and country.code = countrylanguage.countrycode;


# UNION: 쿼리를 실행한 결과를 
# OUTER JOIN을 구현 가능

use SSAC;
select name
from user
union all
select addr_name
from addr;

# outer join
select user.user_id, user.name, addr.addr_name
from user
left join addr
on user.user_id = addr.user_id
union
select user.user_id, user.name, addr.addr_name
from user
right join addr
on user.user_id = addr.user_id;

# sub query

# subquery : select
# 전체 나라수, 전체 도시수, 전체 언어수를 하나의 row, 세개의 column으로 출력
# 괄호 안에 쿼리를 넣음
# from dual(from절에 쓸 것이 없을 때)
use world;
select (select count(*) from country) as country_count
       , (select count(*) from city) as city_count
       , (select count(distinct(language)) from countrylanguage) as language_count
from dual;

# from
# 800만 이상이 되는 도시의 국가코드 도시이름 도시인구수 출력
select country.code, country.name, city.name, city.population
from country 
join city
on country.code = city.countrycode
having city.population >= 8000000
ORDER BY city.population;

# 서브쿼리 사용
select country.code, country.name, city.name, city.population
from (select * from city where population >= 8000000) as city
join country
on country.code = city.countrycode
ORDER BY city.population;

# where
# 800만 이상 도시의 국가코드, 국가이름, 대통령 이름을 출력
select countrycode
from city
where population >= 8000000;

select code, name, headofstate
from country
where code in (
    select countrycode
    from city
    where population >= 8000000
);

select code, name, headofstate
from country
where population >= (select population from country where code = 'kor');

# any: or: 둘중에 한가지만 만족해도 TRUE
# all: and: 둘 다 만족해야 TRUE

select code, name, headofstate
from country
where population >= any (
    select population from country where code in ('kor', 'bra')
);

select code, name, headofstate
from country
where population >= all (
    select population from country where code in ('kor', 'bra')
);

# 대륙과 지역별 사용하는 언어의 수 출력
SELECT  country.continent, country.region, countrylanguage.language
FROM country
JOIN countrylanguage
ON country.code = countrylanguage.countrycode;

# continent, region별 language의 수를 출력

SELECT  country.continent, ifnull(country.region, 'total'), count(language)
FROM country
JOIN countrylanguage
ON country.code = countrylanguage.countrycode
GROUP BY country.continent, country.region
WITH ROLLUP;


select country.continent, country.region, count(countrylanguage.language)
from country
join countrylanguage
on country.code = countrylanguage.countrycode
group by country.continent, country.region;

select continent, region, count(language)
from(
	select country.continent, country.region, countrylanguage.language
	from country
	join countrylanguage
	on country.code = countrylanguage.countrycode
) as sub
group by continent, region;


# view
# 가상의 테이블로 특정 쿼리를 실행한 결과 데이터를 출력하는 용도
# 실제 데이터를 저장x 수정 및 인덱스 설정이 불가능
# 쿼리를 조금 더 단순하게 작성하게 해주는 기능

# 800만 이상의 도시인구가 있는 국가의 국가코드, 국가이름, 도시이름

select country.code, country.name, city_800.name
from(
    select countrycode, name
    from city
    where population >= 8000000) as city_800
join country
on country.code = city_800.countrycode;

create view city2 as
select countrycode, name
from city
where population >= 8000000;

select country.code, country.name, city2.name
from city2
join country
on country.code = city2.countrycode;

# index: 테이블에서 데이터를 빠르게 검색
use employees;
select count(*) from salaries;
show index from salaries;

select * from salaries where to_date < '1986-01-01';

create index tdate on salaries (to_date);

drop index tdate on salaries;

explain
select * from salaries where to_date < '1986-01-01';

# trigger: 특정 테이블을 감시하고 있다가 설정한 조건이 감지되면 지정해놓은 쿼리가 자동으로 실행

use test;
show tables;

create table chat(
    chat_id int primary key auto_increment
    , msg varchar(200)
);

create table backup(
    backup_id int primary key auto_increment
    , backup_msg varchar(200)
    , backup_date timestamp default current_timestamp
);

insert into chat(msg) values ('hello'), ('hi'), ('my name is peter');
select * from chat;

# delimiter |
#	create trigger backup_tr
#	before delete on chat
#	for each row begin
#		insert into backup(backup_msg)
#		values (old.msg);
# end |

show triggers;

select * from chat;

select * from backup;

delete from chat
where msg like'h%'
limit 10;

# JOIN
# 국가별로 국가코드, 국가이름, 국가 인구, 도시인구, 도시개수를 출력

use world;

select country.code, country.name, country.population, sum(city.population), count(city.name)
from country
join city
on country.code = city.countrycode
group by country.code, country.name, country.population
ORDER BY country.population desc;

use world;
# Q1
  SELECT name, population
    FROM country
   WHERE population > (SELECT population
						 FROM country
						WHERE name = 'mexico')
ORDER BY population DESC;

# Q2
  SELECT country.name, count(city.name) AS count
    FROM country
    JOIN city
      ON country.code = city.countrycode
GROUP BY country.name
ORDER BY count(city.name) DESC
   LIMIT 10;

# Q3
  SELECT countrylanguage.language
         , ROUND(sum(country.population* countrylanguage.percentage / 100), 0) AS population
    FROM countrylanguage
    JOIN country
      ON countrylanguage.countrycode = country.code
GROUP BY countrylanguage.language
ORDER BY population DESC
   LIMIT 10;

# Q4
  SELECT city.name, country.code, country.name
         , ROUND((city.population / country.population * 100), 2) AS percentage
    FROM country
    JOIN (SELECT * FROM city WHERE population > 5000000) AS city
      ON country.code = city.countrycode
  HAVING percentage >= 10
ORDER BY percentage DESC;

# Q5
  SELECT country.name , ROUND(( population / surfacearea), 0) as density
         , count(countrylanguage.language) AS count, group_concat(language) AS languages
    FROM (SELECT * FROM country WHERE surfacearea >= 10000) AS country
    JOIN countrylanguage
      ON country.code = countrylanguage.countrycode
GROUP BY country.name, density
  HAVING density >= 200 AND count = 2;

# Q6
CREATE VIEW city_300 AS
SELECT countrycode, name, population
FROM city
WHERE population >= 3000000;
CREATE VIEW language_3 AS
SELECT countrycode, count(language) AS count, group_concat(language) AS languages
FROM countrylanguage
GROUP BY countrycode;

SELECT city_300.countrycode AS code, city_300.name
, city_300.population, country.name, count(countrylanguage.language) AS count
, group_concat(language) AS languages 
FROM city_300
JOIN country
ON city_300.countrycode = country.code
JOIN countrylanguage
ON countrylanguage.countrycode = city_300.countrycode
GROUP BY code, city_300.name, city_300.population
HAVING count <= 3;
use world;
select * from KORUSA;
# Q7
CREATE VIEW KORUSA AS
	SELECT code, population, gnp
	  FROM country
	 WHERE code = 'KOR' OR code = 'USA';
SELECT
	group_concat(CASE WHEN code = 'KOR' THEN 'population' END) AS 'category'
	, sum(CASE WHEN code = 'KOR' THEN population END) AS 'KOR'
	, sum(CASE WHEN code = 'USA' THEN population END) AS 'USA'
  FROM KORUSA
UNION
SELECT
	group_concat(CASE WHEN code = 'KOR' THEN 'gnp' END) AS 'category'
	,  round(sum(CASE WHEN code = 'KOR' THEN gnp END), 0) AS 'KOR'
	,  round(sum(CASE WHEN code = 'USA' THEN gnp END), 0) AS 'USA'
  FROM KORUSA;

use world;
use sakila;
# Q8
CREATE VIEW date_pay AS
	  SELECT distinct(date_format(payment_date, "%Y-%m")) AS date
			 , sum(amount) AS amount
		FROM payment
	GROUP BY date;
SELECT 
	  sum(CASE WHEN date = '2005-05' THEN amount END) AS '2005-05'
	, sum(CASE WHEN date = '2005-06' THEN amount END) AS '2005-06'
	, sum(CASE WHEN date = '2005-07' THEN amount END) AS '2005-07'
	, sum(CASE WHEN date = '2005-08' THEN amount END) AS '2005-08'
	, sum(CASE WHEN date = '2006-02' THEN amount END) AS '2006-02'
  FROM date_pay;

# Q9
CREATE VIEW rentnpay AS
	  SELECT distinct(date_format(payment_date, "%Y-%m")) AS date
		     , sum(amount) AS amount, count(payment_date) AS rent
	    FROM payment
	GROUP BY date;
SELECT 
    group_concat(CASE WHEN date = '2005-05' THEN 'amount' END) AS 'category'
	, sum(CASE WHEN date = '2005-05' THEN amount END) AS '2005-05'
	, sum(CASE WHEN date = '2005-06' THEN amount END) AS '2005-06'
	, sum(CASE WHEN date = '2005-07' THEN amount END) AS '2005-07'
	, sum(CASE WHEN date = '2005-08' THEN amount END) AS '2005-08'
	, sum(CASE WHEN date = '2006-02' THEN amount END) AS '2006-02'
  FROM rentnpay
UNION
SELECT 
    group_concat(CASE WHEN date = '2005-05' THEN 'rent' END) AS 'category'
	, sum(CASE WHEN date = '2005-05' THEN rent END) AS '2005-05'
	, sum(CASE WHEN date = '2005-06' THEN rent END) AS '2005-06'
	, sum(CASE WHEN date = '2005-07' THEN rent END) AS '2005-07'
	, sum(CASE WHEN date = '2005-08' THEN rent END) AS '2005-08'
	, sum(CASE WHEN date = '2006-02' THEN rent END) AS '2006-02'
  FROM rentnpay;