\# Competitive Product Teardown — Indian Investment Platforms



\## Purpose



This teardown compares publicly documented investment-product experiences across Upstox, Groww, Zerodha Coin, and INDmoney.



The analysis focuses on investment discovery, fund research, comparison, decision support, and portfolio analytics — areas relevant to the product analytics case study in this repository.



> \*\*Scope note:\*\* This is based on publicly available product pages and documentation. It does not use internal Upstox/customer data and does not claim that any observed experience is an internal product gap.



\## Feature Comparison



| Product area | Upstox | Groww | Zerodha Coin | INDmoney |

|---|---|---|---|---|

| Mutual-fund discovery | Public mutual-fund screener with fund/category/return/risk information | Mutual-fund discovery plus curated collections | Search and filters by AMC, category, subcategory, plan, AUM, minimum investment, expense ratio and CAGR | Screener with filters for category, returns, risk and expense ratio |

| Fund comparison | Public fund screener exposes comparison-oriented metrics | Dedicated comparison with NAV, returns, risk, rating, expense ratio, holdings and fund-manager information | Fund comparison and analysis tools | Dedicated comparison plus portfolio analytics |

| Decision support | Strategy, performance and cost criteria are publicly documented | Curated collections and detailed comparison | Fund analysis including sectors and underlying companies | INDmoney Rank, risk/return filters and portfolio analytics |

| SIP / recurring investing | Mutual-fund investing and SIP-oriented experience | SIPs and mutual-fund investing | Flexible SIPs, pause/modify, step-up SIP, STP and SWP | SIPs, step-up SIP and STP |

| Portfolio analytics | Investment tracking/research | Portfolio tracking | Unified demat portfolio across stocks and mutual funds | XIRR, returns, benchmark comparison, sector/market-cap exposure and portfolio scan |

| External portfolio aggregation | Not established from sources reviewed | Not established from sources reviewed | Unified Zerodha holdings experience | Can import external mutual funds and track them |



\## Evidence



\### Upstox



Upstox's public mutual-fund screener currently exposes metrics including CAGR, expense ratio, returns versus category, and risk versus category.



Its public educational material also identifies investment strategy, performance, costs, and fund-manager considerations as factors users can consider when selecting funds.



\### Groww



Groww provides a dedicated mutual-fund comparison experience covering parameters such as NAV, returns, risk, rating, expense ratio, fund size, holdings, and fund-manager information.



Groww also provides curated mutual-fund collections and comparison as part of its investing product.



\### Zerodha Coin



Zerodha documents search and filtering by:



\- AMC

\- Category

\- Subcategory

\- Plan

\- AUM

\- Minimum investment

\- Expense ratio

\- CAGR



Coin also documents fund comparison, sector/company analysis, flexible SIPs, STP, SWP, and a unified demat portfolio.



\### INDmoney



INDmoney provides mutual-fund screening and comparison using attributes such as category, returns, risk, and expense ratio.



Its portfolio analytics include XIRR, returns, benchmark comparison, sector/market-cap exposure, and portfolio scanning. It also supports importing external mutual-fund investments.



\## Product Takeaways



\### 1. Discovery is a competitive product surface



Across these platforms, users are given structured ways to narrow a large fund universe using attributes such as category, risk, returns, expense ratio, and other fund characteristics.



This supports the case-study hypothesis that discovery friction is worth measuring rather than assuming.



\### 2. Comparison can reduce decision friction



Several competitors explicitly expose comparison or analysis capabilities.



Therefore, a product analytics implementation should instrument not only:



\- `fund\_viewed`

\- `fund\_selected`



but also intermediate actions such as:



\- `fund\_search`

\- `filter\_used`

\- `fund\_comparison\_started`

\- `fund\_details\_viewed`

\- `risk\_information\_viewed`

\- `returns\_information\_viewed`



\### 3. Portfolio context can extend beyond the purchase decision



INDmoney publicly emphasizes external mutual-fund tracking and portfolio scans, while Coin emphasizes a unified portfolio experience.



This creates an interesting product question:



> Does providing more portfolio context help users make decisions, or does additional information create decision overload?



This should be tested using behavioral data rather than assumed.



\### 4. Measure the complete decision journey



A useful product funnel is:



`Discovery → Search/Filter → Fund Detail → Comparison → Selection → Investment`



The current project already measures several downstream stages.



The next analytical opportunity would be to instrument the missing discovery and decision events and identify where users hesitate or abandon.



\## Suggested Product KPIs



For a real product team, useful metrics could include:



\- Search-to-fund-detail conversion

\- Filter usage rate

\- Fund-detail-to-comparison conversion

\- Comparison-to-selection conversion

\- Fund-view-to-selection conversion

\- Selection-to-investment-start conversion

\- Investment completion rate

\- Repeat investment rate

\- 30-day investment retention



These metrics should be segmented by acquisition channel, user tenure, product category, and new versus returning investors where appropriate.



\## Product Opportunity Hypotheses



These are \*\*hypotheses for experimentation\*\*, not conclusions about any company's current product.



\### Hypothesis 1 — Guided Discovery



A goal/risk-oriented discovery flow could reduce the number of users who browse funds without reaching a selection.



\### Hypothesis 2 — Comparison-First Research



Making fund comparison easier could improve movement from fund-detail pages to selection.



\### Hypothesis 3 — Decision Summaries



A concise summary of risk, costs, returns, holdings, and relevant context could reduce information overload while preserving access to detailed information.



\### Hypothesis 4 — Personalized Context



Showing relevant existing portfolio exposure could help users understand how a new fund fits into their portfolio.



\### Hypothesis 5 — Better Instrumentation



Tracking search, filtering, comparison, and information-view events would allow a product team to identify the actual friction point before shipping a solution.



\## Limitations



\- Public websites do not reveal internal conversion, retention, experimentation, or user-behavior data.

\- Feature availability can change by app version, user type, geography, or product eligibility.

\- This teardown compares \*\*documented product capabilities\*\*, not measured product performance.

\- The synthetic analytics dataset in this repository must not be presented as Upstox or competitor customer data.



\## Sources



\- Upstox — Mutual Funds Explore  

&#x20; https://upstox.com/mutual-funds/explore/



\- Groww — Compare Funds  

&#x20; https://groww.in/mutual-funds/compare



\- Groww — Products  

&#x20; https://groww.in/products



\- Zerodha — What is Coin?  

&#x20; https://support.zerodha.com/category/mutual-funds/understanding-mutual-funds/about-coin/articles/what-is-coin



\- Zerodha — Mutual Fund Search and Filters  

&#x20; https://support.zerodha.com/category/mutual-funds/understanding-mutual-funds/getting-started-with-coin/articles/basic-filtered-search



\- INDmoney — Mutual Funds  

&#x20; https://www.indmoney.com/mutual-funds



\- INDmoney — Mutual Fund Portfolio Scan  

&#x20; https://www.indmoney.com/features/mutual-fund-portfolio-scan

