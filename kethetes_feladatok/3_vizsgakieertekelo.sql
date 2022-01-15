create table students (
student_id serial primary key,
name varchar(100),
created_date date default now()
);

create table test_types(
test_type_id serial primary key,
name varchar(100),
created_date date default now()
);
drop table test_results ;

create table test_results(
result_id serial primary key,
student_fk_id int,
test_type_id int,
test_result_value decimal,
created_date date default now(),

constraint fk_student_id
foreign key (student_fk_id)
references students(student_id)
on delete cascade,

constraint fk_test_type_id
foreign key (test_type_id)
references test_types(test_type_id)
on delete cascade

);




select * from test_types;
select * from students t;

delete from test_results ;

select
from
where
group by
having
order by

-- a beadando a jegy 10%-át adja
-- a vizsga a jegy 70%-át
-- a labor gyakorlat pedig a jegy 20%-át
------------------------
---if else

--case when

-- subselect

/*
 * 
 * 
	if point >= 0 and point <60:
		return 1
	if point >= 60 and point <70:
		return 2
	if point >= 70 and point <80:
		return 3
	if point >= 80 and point <90:
		return 4
	if point >= 90:
		return 5
 * 
 * */


create table student_statistics as (
select
sum(calc.calculated_avg) as  osszpontszam,
case 
  when sum(calc.calculated_avg) < 60 then 1
  when sum(calc.calculated_avg) < 70 and sum(calc.calculated_avg) >= 60 then 2
  when sum(calc.calculated_avg) < 80 and sum(calc.calculated_avg) >= 70 then 3
  when sum(calc.calculated_avg) < 90 and sum(calc.calculated_avg) >= 80 then 4
  when sum(calc.calculated_avg) >= 90 then 5
end as jegy,
calc.student as tanulo
from
(select
base_data.avg_result,
base_data.student,
base_data.name,
case 
  when base_data.name = 'beadando' then base_data.avg_result*0.1
  when base_data.name = 'vizsga' then base_data.avg_result*0.7
  when base_data.name = 'labor' then base_data.avg_result*0.2
end as calculated_avg
from
(select s.name as student, t.name,
avg(tr.test_result_value) as avg_result--, count(tr.test_result_value), sum(tr.test_result_value)--, min(), max() stb
from test_results tr
inner join students s on tr.student_fk_id = s.student_id
inner join test_types t on tr.test_type_id = t.test_type_id
group by s.name, t.name
order by s.name) as base_data
) as calc
group by calc.student)
;




select s.name, t.name, tr.test_result_value
from test_results tr
inner join students s on tr.student_fk_id = s.student_id
inner join test_types t on tr.test_type_id = t.test_type_id

;


select
avg(osszpontszam), avg(jegy)
from student_statistics t;

drop table cars;
create table cars (name varchar(50),
miles_per_gallon int4,
cylinders int4,
displacement int4,
horsepower int4,
weight_in_lbs int4,	
acceleration numeric,
year date,
origin varchar(10),
creation_date date default now())
;
delete from cars c
where c.horsepower < 100;

select * from cars

