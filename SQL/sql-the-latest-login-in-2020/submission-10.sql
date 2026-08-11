-- Write your query below
SELECT 
    l.user_id, 
    MAX(l.time_stamp) AS last_stamp
FROM  logins l
WHERE
    l.time_stamp::timestamp >= TIMESTAMP '2020-01-01 00:00:00'
    AND l.time_stamp::timestamp < TIMESTAMP '2021-01-01 00:00:00'
GROUP BY l.user_id;