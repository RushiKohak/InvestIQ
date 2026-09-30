\# Product Insights



\## 1. Executive Summary



This case study analyzes a synthetic investment-platform event dataset containing

10,000 users and their onboarding, product discovery, and investment events.



The analysis focuses on identifying conversion and engagement opportunities

across the investment journey.



\---



\## 2. Key Observations



\### Observation 1 — KYC completion



67.19% of signed-up users completed KYC.



This indicates that a meaningful portion of users progress through onboarding,

while a substantial group does not reach completed KYC.



\### Observation 2 — Product discovery



28.27% of the overall user base reached the fund-viewed stage.



This creates a potentially important point of investigation in the user journey:

many users do not reach meaningful investment-product discovery.



\### Observation 3 — Fund selection



63.78% of fund viewers proceeded to select a fund.



The relatively stronger conversion at this stage suggests that users who reach

fund discovery are substantially more engaged than the overall signed-up user

population.



\### Observation 4 — Investment completion



9.74% of signed-up users completed an investment.



The difference between initial signup volume and completed investments indicates

a substantial funnel gap between acquisition and transaction completion.



\### Observation 5 — Acquisition-channel differences



Fund-view → fund-selection conversion varies across acquisition channels:



\- Organic: 66.77%

\- Referral: 63.31%

\- Paid Search: 63.30%

\- Social Media: 61.45%

\- Partner: 58.56%



This difference should be treated as a signal for further investigation rather

than proof of causation.



\---



\## 3. Product Hypotheses



The available synthetic event data does not explain why users drop between

stages. Therefore, the following are hypotheses rather than established causes.



\### Hypothesis A — Product discovery friction



Users may have difficulty finding relevant investment products after completing

onboarding.



Potential areas to investigate:



\- fund discovery layout

\- search and filtering

\- category organization

\- recommendations

\- educational information



\### Hypothesis B — Acquisition intent mismatch



Differences in view-to-selection conversion between acquisition channels may

reflect differences in user intent or traffic composition.



Further analysis should examine:



\- campaign/source

\- user intent

\- product preference

\- onboarding completion

\- downstream investment conversion



\### Hypothesis C — Decision friction



Some users may reach a fund but hesitate before selecting it.



Potential areas for investigation:



\- information clarity

\- risk information

\- returns presentation

\- comparison functionality

\- minimum investment information



\---



\## 4. Recommended Investigation



Before implementing a product change, collect additional behavioral data around

the fund-discovery experience.



Useful events could include:



\- fund\_search

\- filter\_used

\- fund\_comparison\_started

\- fund\_details\_viewed

\- risk\_information\_viewed

\- returns\_information\_viewed

\- recommendation\_clicked

\- investment\_amount\_entered



These events would help identify the specific interaction where users abandon

the investment journey.



\---



\## 5. Success Metrics



A potential product improvement should be evaluated using measurable outcomes.



\### Primary metric



Fund View → Fund Selection Conversion



\### Secondary metrics



\- Investment completion rate

\- KYC completion rate

\- Fund-detail engagement

\- Search/filter usage

\- Investment initiation rate



\### Guardrail metrics



\- Payment failure rate

\- User drop-off during onboarding

\- Support/contact rate

\- Cancellation rate



\---



\## 6. Important Data Limitation



This project uses synthetic user-event data.



Therefore, the findings demonstrate the analytical workflow and product-thinking

process rather than representing real customer behavior from an investment

platform.



The observations should not be interpreted as actual performance metrics of

Upstox or any other company.

