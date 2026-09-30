-- ============================================================
-- PRODUCT METRICS
-- ============================================================

-- 1. Total users
SELECT
    COUNT(DISTINCT user_id) AS total_users
FROM user_events;


-- 2. KYC completion rate
SELECT
    ROUND(
        100.0 *
        COUNT(DISTINCT CASE WHEN event = 'kyc_completed' THEN user_id END)
        /
        NULLIF(COUNT(DISTINCT CASE WHEN event = 'signup' THEN user_id END), 0),
        2
    ) AS kyc_completion_rate
FROM user_events;


-- 3. Fund view rate
SELECT
    ROUND(
        100.0 *
        COUNT(DISTINCT CASE WHEN event = 'fund_viewed' THEN user_id END)
        /
        NULLIF(COUNT(DISTINCT CASE WHEN event = 'signup' THEN user_id END), 0),
        2
    ) AS fund_view_rate
FROM user_events;


-- 4. Fund selection rate among viewers
SELECT
    ROUND(
        100.0 *
        COUNT(DISTINCT CASE WHEN event = 'fund_selected' THEN user_id END)
        /
        NULLIF(COUNT(DISTINCT CASE WHEN event = 'fund_viewed' THEN user_id END), 0),
        2
    ) AS fund_selection_rate
FROM user_events
WHERE product = 'Mutual Funds';


-- 5. Investment completion rate among signups
SELECT
    ROUND(
        100.0 *
        COUNT(DISTINCT CASE WHEN event = 'investment_completed' THEN user_id END)
        /
        NULLIF(COUNT(DISTINCT CASE WHEN event = 'signup' THEN user_id END), 0),
        2
    ) AS investment_completion_rate
FROM user_events;


-- 6. Overall product funnel conversion
SELECT
    ROUND(
        100.0 *
        COUNT(DISTINCT CASE WHEN event = 'investment_completed' THEN user_id END)
        /
        NULLIF(COUNT(DISTINCT CASE WHEN event = 'signup' THEN user_id END), 0),
        2
    ) AS signup_to_investment_conversion
FROM user_events;


-- 7. Users by product
SELECT
    product,
    COUNT(DISTINCT user_id) AS users
FROM user_events
GROUP BY product
ORDER BY users DESC;


-- 8. Users by acquisition channel
SELECT
    acquisition_channel,
    COUNT(DISTINCT user_id) AS users
FROM user_events
GROUP BY acquisition_channel
ORDER BY users DESC;