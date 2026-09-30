-- ============================================================
-- INVESTMENT PRODUCT ANALYTICS
-- Mutual Fund Investment Funnel
-- ============================================================

SELECT
    event,
    COUNT(DISTINCT user_id) AS users
FROM user_events
WHERE product = 'Mutual Funds'
GROUP BY event
ORDER BY
    CASE event
        WHEN 'signup' THEN 1
        WHEN 'kyc_started' THEN 2
        WHEN 'kyc_completed' THEN 3
        WHEN 'fund_viewed' THEN 4
        WHEN 'fund_selected' THEN 5
        WHEN 'investment_started' THEN 6
        WHEN 'payment_initiated' THEN 7
        WHEN 'investment_completed' THEN 8
    END;

    -- ============================================================
-- Funnel performance by acquisition channel
-- ============================================================

SELECT
    acquisition_channel,

    COUNT(DISTINCT CASE
        WHEN event = 'fund_viewed'
        THEN user_id
    END) AS fund_viewed_users,

    COUNT(DISTINCT CASE
        WHEN event = 'fund_selected'
        THEN user_id
    END) AS fund_selected_users,

    ROUND(
        100.0 *
        COUNT(DISTINCT CASE
            WHEN event = 'fund_selected'
            THEN user_id
        END)
        /
        NULLIF(
            COUNT(DISTINCT CASE
                WHEN event = 'fund_viewed'
                THEN user_id
            END),
            0
        ),
        2
    ) AS view_to_selection_conversion

FROM user_events

WHERE product = 'Mutual Funds'

GROUP BY acquisition_channel

ORDER BY view_to_selection_conversion DESC;