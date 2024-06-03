
-- a)	Show a number of clicks by User and calendar month
SELECT
    DATE_TRUNC('month', TO_DATE(day, 'YYYY-MM-DD')) AS month,
    _name,
    SUM(_clicks) AS total_clicks
FROM
    websitestatisticsdata
GROUP BY
    month,
    _name
ORDER BY
    month,
    _name;

-- b)	Show a share of clicks of each user by month
WITH monthly_clicks AS (
    SELECT
        DATE_TRUNC('month', TO_DATE(day, 'YYYY-MM-DD')) AS month,
        _name,
        SUM(_clicks) AS total_clicks
    FROM
        websitestatisticsdata
    GROUP BY
        month,
        _name
),
total_monthly_clicks AS (
    SELECT
        month,
        SUM(total_clicks) AS month_total_clicks
    FROM
        monthly_clicks
    GROUP BY
        month
)
SELECT
    mc.month,
    mc._name,
    mc.total_clicks,
    (mc.total_clicks::FLOAT / tmc.month_total_clicks) * 100 AS share_of_clicks
FROM
    monthly_clicks mc
JOIN
    total_monthly_clicks tmc ON mc.month = tmc.month
ORDER BY
    mc.month,
    mc._name;
