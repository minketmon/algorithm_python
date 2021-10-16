select ID, NAME from
(SELECT s.id, name, line_color, station_id, drive_order
From SUBWAY_STATIONS s left outer join LINE_ROUTES l on s.id=l.station_id
GROUP BY id HAVING COUNT(*) = 1) ss
where line_color is null or line_color="Yellow" order by id;