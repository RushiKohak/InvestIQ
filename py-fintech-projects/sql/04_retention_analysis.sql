-- ============================================================
-- MONTHLY COHORT RETENTION
-- ============================================================

WITH user_cohorts AS (
    SELECT
        user_id,
        strftime('%Y-%m', MIN(event_timestamp)) AS cohort_month
    FROM user_events
    GROUP BY user_id
),

user_activity AS (
    SELECT DISTINCT
        user_id,
        strftime('%Y-%m', event_timestamp) AS activity_month
    FROM user_events
),

cohort_activity AS (
    SELECT
        uc.cohort_month,
        ua.activity_month,
        COUNT(DISTINCT ua.user_id) AS active_users
    FROM user_cohorts uc
    JOIN user_activity ua
        ON uc.user_id = ua.user_id
    GROUP BY
        uc.cohort_month,
        ua.activity_month
)

SELECT
    cohort_month,
    activity_month,
    active_users
FROM cohort_activity
ORDER BY
    cohort_month,
    activity_month;