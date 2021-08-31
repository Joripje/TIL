# SELECT FROM
use world;

select *
from country;

select Code, Name, Population
from country;

select code as country_code, name as country_name, population
from country;

## 주석처리 방법
/*
*/
--
/* show databases;
show tables; */
-- desc country

select code
#		, name
from country;

select code, name, gnp
from country;

select code, name, gnp * 1000 as gnp_1000
from country;

select code, name, continent
from country;

select code, name, continent, continent = 'asia' as is_asia
from country;

select code, name, population, LifeExpectancy,
(LifeExpectancy >= 70) and (population >= 5000*10000)
from country;

## WHERE

select code, name, population
from country
where(population >= 7000 * 10000) and (population <= 10000 * 10000);

## between을 사용해 같은 문장으로
select code, name, population
from country
where population between 7000*10000 and 10000 * 10000;


# 아시아와 아프리카 대륙의 국가 데이터를 출력

select code, name, population, continent
from country
where continent = 'Asia' or continent = 'Africa';

# IN, NOT IN

select code, name, continent, population
from country
where continent in ('Asia', 'Africa');

# 아시아 아프리카를 제외한

select code, name, continent, population
from country
where continent not in ('Asia', 'Africa');

# LIKE : 특정 문자열이 포함되어 있는 데이터를 출력
select code, name, localname
from country
where localname like 'A%';
# % 아무 문자 여러개, A% A로 시작하는 문자열
# %A A로 끝나는 문자열

# ODER BY

# LIMIT : 조회되는 데이터의수를 제한
# 인구 상위 5개의 국가를 내림차순으로 출력

select code, name, population
from country
order by population desc
limit 5;

# 인구 상위 6위 ~ 8위까지의 국가를 내림차순으로 출력

select code, name, population
from country
order by population desc
limit 5, 3;  # 5개의 데이터를 스킵하고 그 뒤의 3개를 출력

# distinct : 중복을 제거해주는 예약어
# 인구가 300만 이상인 도시를 가지고 있는 국가의 국가 코드를 출력
select distinct countrycode
from city
where population >=800 * 10000;

# Quiz: 한국 도시 중 인구수가 100만이 넘는 도시를 인구수 순으로 오름차순으로 정렬해서 출력

# Q1
SELECT countrycode, name, population
FROM city
WHERE (countrycode = 'KOR') AND (Population >= 1000000)
ORDER BY population DESC;

# Q2
SELECT countrycode, name, population
FROM city
WHERE population BETWEEN 8000000 and 10000000
ORDER BY population;

# Q3
SELECT code, name, continent, gnp
FROM country
WHERE (IndepYear BETWEEN 1940 AND 1950)
  AND (gnp >= 100000)
ORDER BY GNP DESC;

# Q4
SELECT countrycode, language, percentage
FROM countrylanguage
WHERE (language in ('Spanish', 'English', 'Korean')) and (percentage >= 95)
ORDER BY language ASC, percentage DESC;

# Q5
SELECT code, name, continent, lifeExpectancy
FROM country
WHERE code LIKE 'K%' AND (lifeExpectancy >= 70) 
ORDER BY lifeExpectancy DESC;

#
USE sakila;
select *
from film_text;

# Q6
SELECT film_id, title, description
FROM film_text
WHERE title LIKE '%ICE%' AND description LIKE '%Drama%';

# Q7
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name LIKE 'A%' AND last_name LIKE '%N';

# Q8
SELECT film_id, title, description, rental_duration, rental_rate, length, rating
FROM film
WHERE rating = 'R'
ORDER BY length DESC
LIMIT 10;

# Q9
SELECT film_id, title, description, length
FROM film
WHERE (length BETWEEN 60 AND 120) AND (description LIKE '%robot%')
ORDER BY length ASC
LIMIT 10, 3;

# Q10
SELECT title, description, category, length, actors
FROM film_list
WHERE (
      category NOT IN ('sci-fi', 'animation', 'drama')
  AND actors LIKE '%ed chase%'
  )
   OR (
	  category NOT IN ('sci-fi', 'animation', 'drama')
  AND actors LIKE '%kevin bloom%'
  )
ORDER BY length DESC
LIMIT 5;