select hour(datetime) as hour, count(hour(Datetime)) as count from animal_outs
where hour(datetime)>=9 and hour(datetime)<20
group by hour order by hour;