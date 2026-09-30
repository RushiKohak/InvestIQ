-- ============================================================
-- COHORT ANALYSIS
-- Users grouped by their first activity month
-- ============================================================

WITH user_cohorts AS (
    SELECT
        user_id,
        strftime('%Y-%m', MIN(event_timestamp)) AS cohort_month
    FROM user_events
    GROUP BY user_id
)

SELECT
    cohort_month,
    COUNT(*) AS users
FROM user_cohorts
GROUP BY cohort_month
ORDER BY cohort_month;