\# Product Requirements Document

\## Investment Discovery Experience



\### 1. Product Context



This project analyzes a synthetic investment-platform dataset to identify

potential opportunities in the user journey from signup to completed investment.



The analysis currently shows:



\- 10,000 total users

\- 67.19% KYC completion

\- 28.27% fund-view rate

\- 63.78% fund-view → selection conversion

\- 9.74% signup → investment completion



These figures are generated from synthetic data and are used to demonstrate

the product analytics workflow.



\---



\## 2. Problem Statement



A significant proportion of users who enter the investment-platform journey

do not progress to a completed investment.



The available event data identifies drop-off points but does not explain the

underlying user reasons.



The product opportunity is therefore to improve the investment discovery

experience and collect better behavioral signals to understand where users

experience friction.



\---



\## 3. User Problem



Users who are interested in investing may have difficulty moving from

general interest to confidently selecting an investment product.



Potential friction areas include:



\- finding relevant funds

\- understanding fund information

\- comparing alternatives

\- understanding risk

\- understanding expected returns

\- deciding how much to invest



These are hypotheses that require validation through additional user research

and behavioral data.



\---



\## 4. Goal



Improve the investment discovery experience and increase the percentage of

users who progress from viewing an investment product to selecting one.



\### Primary success metric



Fund View → Fund Selection Conversion



\### Secondary metrics



\- Investment initiation rate

\- Investment completion rate

\- Fund-detail engagement

\- Search usage

\- Filter usage

\- Comparison usage



\---



\## 5. Non-Goals



This initiative will not initially:



\- redesign the entire investment application

\- change investment products themselves

\- provide personalized financial advice

\- change pricing or fees

\- redesign the complete onboarding/KYC process



\---



\## 6. Proposed Product Direction



Introduce a clearer investment discovery experience containing:



\### A. Improved discovery



Allow users to:



\- search funds

\- filter funds by relevant attributes

\- browse categories

\- discover popular/relevant funds



\### B. Better fund information



Present important information clearly:



\- historical performance

\- risk information

\- investment minimum

\- expense-related information

\- fund category

\- portfolio information



\### C. Comparison



Allow users to compare multiple funds using a consistent set of attributes.



\### D. Decision support



Provide educational explanations and contextual information that help users

understand investment characteristics without presenting personalized financial

advice.



\---



\## 7. Proposed User Flow



Signup

↓

KYC

↓

Investment Discovery

↓

Search / Browse / Filter

↓

Fund Details

↓

Compare

↓

Select Fund

↓

Investment Amount

↓

Payment

↓

Investment Completed



\---



\## 8. Analytics Instrumentation



To understand the experience better, introduce the following events:



| Event | Purpose |

|---|---|

| fund\_search | Measure search usage |

| filter\_used | Measure filtering behavior |

| fund\_details\_viewed | Measure detailed product engagement |

| fund\_comparison\_started | Measure comparison intent |

| fund\_comparison\_completed | Measure comparison completion |

| risk\_information\_viewed | Measure risk-information engagement |

| returns\_information\_viewed | Measure returns-information engagement |

| recommendation\_clicked | Measure recommendation engagement |

| investment\_amount\_entered | Measure investment intent |



\---



\## 9. User Stories



\### Discovery



As an investor,

I want to search and filter investment products,

so that I can find relevant options quickly.



\### Fund information



As an investor,

I want to understand a fund's risk, performance and key characteristics,

so that I can make an informed decision.



\### Comparison



As an investor,

I want to compare multiple funds,

so that I can evaluate alternatives before selecting one.



\### Investment



As an investor,

I want a clear investment flow,

so that I can complete my investment without unnecessary friction.



\---



\## 10. Experimentation



Potential experiments could include:



\### Experiment A



Current fund discovery interface

vs.

Improved search/filter discovery interface.



Measure:



\- Fund View → Selection Conversion

\- Fund Details Engagement

\- Investment Initiation



\### Experiment B



Current fund information page

vs.

Improved information hierarchy.



Measure:



\- Fund Selection

\- Investment Initiation

\- Investment Completion



Experiments should be evaluated using predefined success and guardrail metrics.



\---



\## 11. Risks



Potential risks include:



\- Excessive information creating decision fatigue

\- Filters making discovery more complicated

\- Recommendations being misunderstood as financial advice

\- Increased UI complexity

\- Improving selection without improving actual investment completion



\---



\## 12. Rollout Plan



\### Phase 1 — Instrumentation



Add missing behavioral events.



\### Phase 2 — User Research



Conduct usability testing and qualitative interviews.



\### Phase 3 — Prototype



Build and test the redesigned discovery experience.



\### Phase 4 — Experiment



Run controlled experimentation with defined success metrics.



\### Phase 5 — Rollout



Gradually increase exposure if the experiment meets success and guardrail

criteria.



\---



\## 13. Data Limitation



This PRD is based on a synthetic dataset created for a portfolio case study.



The metrics do not represent real users, customers or internal data from

Upstox or another investment platform.



The proposed product changes are hypotheses intended for further validation.

