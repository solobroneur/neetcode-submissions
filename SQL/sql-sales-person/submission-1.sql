-- Write your query below
SELECT
    sp.name
FROM
    sales_person AS sp
WHERE NOT EXISTS (
    SELECT
        *
    FROM
        orders AS o
    JOIN
        company AS c
    ON
        c.com_id = o.com_id
    WHERE
        o.sales_id = sp.sales_id AND
        c.name = 'CRIMSON'
);