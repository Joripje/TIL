use SSAC;
CREATE table number1(data tinyint);
show tables;

desc number2;
insert into number1 value(127);
select * from number1;

create table number2 ( data tinyint unsigned);
insert into number2 value(128);
select * from number2;

create table number3 (data float);
create table number4 (data double);
insert into number3 value(123.456789);
insert into number4 value(123.4567890123456789);
select * from number3;
select * from number4;

desc purchases;

create database test;
show databases;
select database();

## DDL: CREATE: database, table 생성
use SSAC;

create table user1(
	user_id int,
    name varchar(20),
    email varchar(30),
    age int,
    rdate date
);
show tables;
desc user1;

create table user2(
	user_id int primary key auto_increment,
    name varchar(20) not null,
    email varchar(30) not null unique,
    age int default 30,
    rdate timestamp
);
desc user2;

## DDL: ALTER
## 인코딩: 사람이 인식할 수 있는 문자를 컴퓨터가 인식할 수 있는 문자로 바꾸는 과정 (<-> 디코딩)
## 저장장치의 발달로 UTF-8이 널리 쓰인다
show variables like 'character_set_database';
alter database SSAC character set = ascii;
alter database SSAC character set = utf8;

### column add
alter table user2 add tmp text;
### column modify
alter table user2 modify column tmp int;
### column drop
alter table user2 drop tmp;
### table encoding check table
show full columns from user2;
### table encoding modify
alter table user2 convert to character set ascii;
alter table user2 convert to character set utf8;
desc user2;

# DDL : DELETE

show tables;
DROP table number4;
show databases;
 
DROP database test;

# CRUD: create: insert
use SSAC;
desc user2;

insert into user2 (name, email, age)
value ("peter", "peter@gmail.com", 23);

select * from user2;

insert into user2 (name, email, age)
values ("andy", "andy@gmail.com", 32)
, ("po", "po@naver.com", 25)
, ("ted", "ted@gmail.com", 39);

insert into user2 (name, email)
value ('mysql', 'mysql@gmail.com');

insert into user2 (name, email)
value ('alice', 'ted@gmail.com');

use world;

# INSERT

select countrycode, name, population
from city
where population >= 8000000;

create table city_800(
	countrycode char(3),
    name varchar(50),
    population int
);
desc city_800;

insert into city_800
select countrycode, name, population
from city
where population >= 8000000;
select * from city_800;

### UPDATE
use SSAC;
select * from user2;
update user2
set email = 'mysql@daum.net', age = 40
where name = 'mysql'
limit 5;

## delete
select * from user2;
delete from user2
where age <= 30
limit 2;

# foreign key
# 데이터의 무결성을 지킬 수 있는 제약조건입니다.
# 데이터의 무결성? 

create database test;
use test;

create table user(
    user_id int primary key auto_increment
    , name varchar(20)
    , addr varchar(20)
);
create table money(
    money_id int primary key auto_increment
    , incom int
    , user_id int
);
desc user;
desc money;

# foreign key 생성
# 다른 테이블에서 참조하고 있는 값은 삭제할 수 없다

desc money;
alter table money add constraint fk_user
foreign key (user_id)
references user (user_id);

insert into user(name, addr)
values('peter', 'seoul'), ('andy', 'pusan');
select * from user;

insert into money(incom, user_id)
values(5000, 1), (6000, 2);

insert into money(incom, user_id)
values(15000, 3);


# on delete, on update
# 참조되는 데이터를 수정, 삭제할때 참조하는 데이터를 어떻게 처리할지를 설정
# cascade: 참조되는 테이블 데이터를 삭제, 수정하면 참조하는 테이블 데이터도 삭제 수정
# set null: 참조되는 테이블 데이터를 삭제, 수정하면 참조하는 테이블 데이터는 null값으로 변경
# no action: 참조되는 테이블 데이터를 삭제, 수정해도 참조하는 데이터를 변경하지 않음
# set default: 참조되는 테이블 데이터를 삭제 수정하면, 참조하는 테이블 데이터를 column의 default값으로 변경
# restrict: 참조하는 데이터를 삭제하거나 수정할 수 없음

drop table money;
drop table user;
create table user(
	user_id int primary key auto_increment,
    name varchar(20),
    addr varchar(20)
);
insert into user(name, addr)
values ("peter", "seoul"), ("andy", "pusan");
select * from user;

create table money(
	money_id int primary key auto_increment,
    income int,
    user_id int,
    foreign key (user_id) references user(user_id)
    on update cascade on delete set null
);

insert into money(income, user_id)
values (5000, 1), (6000, 2);
select * from money;


insert into money(income, user_id)
values (1000, 1), (4000, 1), (9000, 2), (3000, 2);

update user
set user_id = 3
where user_id = 2
limit 1;

delete from user
where user_id = 3
limit 1;

# Functions 1: round, date_format, concat, count, dictinct
# round
use world;
select countrycode, language, percentage
       , ceil(percentage), round(percentage, 0), truncate(percentage, 0) 
from countrylanguage;

# date_format(): 날짜 데이터에 대한 포맷을 변경

use sakila;
select payment_date, date_format(payment_date, "%Y-%m")
from payment;
select distinct(date_format(payment_date, "%H")) as unique_hour
from payment
order by unique_hour;


#concat 문자열 연결
use world;
select code, name, concat(name, "(", code, ")")
from country;


# count : row의 개수를 세어줌
select *
from city;

# countrylanguage 테이블에서 전세계 언어의 개수를 출력
# distinct: 중복값 제거
select count(distinct(language))
from countrylanguage;

# Functions 2: if, ifnull, case when then
# if
# 도시의 인구가 100만이 넘으면 big 아니면 smaill을 출력하는 sacle 컬럼을 추가하세요.

select name, population, if(population>=1000000, 'big', 'small') as scale
from city
order by population desc;

#ifnull
#null값이 있는 경우 null을 대체할 값
select code, name, indepyear, ifnull(indepyear, 0)
from country;

# case when then: 조건이 여러개인 경우 사용
# 국가의 인구가 1억 이상 big, 1천만 이상 medium, 1천만 미만 small
select name, population,
       case
            when population >= 100000000 then 'big'
            when population >= 10000000 then 'medium'
            else 'small'
		end as scale
from country
order by population desc;

# GROUP BY
# 국가코드별 도시의 개수
select countrycode, count(countrycode) as city_count
from city
group by countrycode
order by city_count desc;

# 국가코드별 모든 도시의 인구 총합을 출력
select countrycode, sum(population)
from city
group by countrycode;

# country 테이블에서 대륙별 인구의 총합을 출력
SELECT continent, sum(population)
FROM country
GROUP BY continent
ORDER BY sum(population) DESC;

# 대륙별 GNP의 총합
SELECT continent, sum(gnp)
FROM country
GROUP BY continent
ORDER BY sum(gnp) DESC;

# 대륙별 인당 GNP
SELECT continent, sum(gnp) / sum(population) AS gnp_1
FROM country
GROUP BY continent
ORDER BY gnp_1 DESC;

use sakila;

select *
from payment;

# 년월별 총 매출을 출력
select date_format(payment_date, "%Y-%m"), sum(amount)
from payment
group by date_format(payment_date, "%Y-%m");

select date_format(payment_date, '%h' ), sum(amount)
from payment
group by date_format(payment_date, '%h' );

# HAVING
# group by, join과 같은 쿼리를 실행한 결과 데이터를 필터링 할 때 사용
# 대륙별 전체 인구를 출력하고 전체 인구가 5억 이상인 대륙을 출력

use world;
SELECT continent, sum(population) as total_population
FROM country
where population >= 500000000
GROUP BY continent;

SELECT continent, sum(population) as total_population
FROM country
GROUP BY continent
having total_population >= 500000000;

# with rollup
# 여러개의 컬럼을 group by하고 각 컬럼별 총합을 row로 출력
# 대륙별, 지역별 인구수의 총합

select continent, region, sum(population) as population
from country
group by continent, region
with rollup;

select ifnull(continent, "total"), ifnull(region, "total")
	   , sum(population) as population
from country
group by continent, region
with rollup;

# 변수선언
set @data = 1;
select @data;

# city 테이블에서 도시의 인구수가 많은 5개 도시를 출력하고 내림차순으로 소팅
set @RANK = 0;
select @RANK:= @RANK+1 as ranking, countrycode, name, population
from city
order by population desc
limit 5;

# countrylanguage에서 언어별 20개 이상의 국가에서 사용하는 언어를 조회해서
# 언어별 사용되는 국가 수에 따라서 내림차순으로 정령해서 출력
SELECT language, count(language)
FROM countrylanguage
GROUP BY language
HAVING count(language) >= 20
ORDER BY count(language) DESC;

# country 테이블에서 대륙별 전체면적, 전체인구, 인구밀도
# 인구밀도 높은 순으로 내림차순 해서 정렬

SELECT continent, sum(surfacearea), sum(population),  sum(population)/sum(surfacearea)
FROM country
GROUP BY continent
ORDER BY sum(population)/sum(surfacearea) DESC;



# Q1
  SELECT countrycode, count(countrycode) AS count
    FROM city
GROUP BY countrycode
ORDER BY count DESC
   LIMIT 5;

select *
from country;
# Q2
  SELECT continent, count(name)
    FROM country
GROUP BY continent
ORDER BY count(name) DESC;

# Q3
  SELECT continent, count(name), round(avg(gnp), 1) AS avgnp
    FROM country
   WHERE population >= 10000000
GROUP BY continent
ORDER BY avgnp DESC;

# Q4
  SELECT countrycode, sum(population)
    FROM city
GROUP BY countrycode
  HAVING sum(population) >= 50000000
ORDER BY sum(population) DESC;

# Q5
  SELECT language, count(language)
    FROM countrylanguage
GROUP BY language
ORDER BY count(language) DESC
   LIMIT 5, 5;

# Q6
  SELECT language, count(language)
    FROM countrylanguage
GROUP BY language
  HAVING count(language) >= 20
ORDER BY count(language) DESC;

# Q7
  SELECT continent, round(sum(surfacearea), 0) AS surfacearea
    FROM country
GROUP BY continent
ORDER BY sum(surfacearea) DESC;

# Q8
SELECT count(distinct(language)) AS COUNT
  FROM countrylanguage
 WHERE percentage < 100 AND percentage >= 90;

# Q9
  SELECT CASE
            WHEN indepyear >= 1800 AND indepyear < 1900 THEN '1800'
            WHEN indepyear >= 1900 AND indepyear < 2000 THEN '1900'
		 END AS indepyear_ages
	   , count(name) AS count
    FROM country
GROUP BY indepyear_ages
  HAVING indepyear_ages IS NOT NULL;

use sakila;
# Q10
  SELECT date_format(payment_date, "%Y-%m") AS date, sum(amount) AS amount
    FROM payment
GROUP BY date_format(payment_date, "%Y-%m")
ORDER BY date;

# Q11
  SELECT first_name
    FROM actor
GROUP BY first_name
  HAVING count(first_name) = 4
ORDER BY 'penelope';

# Q12
  SELECT category
    FROM film_list
GROUP BY category
ORDER BY sum(price) DESC
   LIMIT 3;