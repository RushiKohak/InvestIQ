\# Investment Product Analytics — Fintech Product Case Study



A fintech product analytics case study built on top of an existing investment-analysis project.



The project combines investment strategy analysis with a synthetic user-event analytics layer to demonstrate how a product team could analyze an investment journey, identify funnel friction, define product hypotheses, and translate insights into a PRD and user stories.



> \*\*Attribution:\*\* The original investment-analysis notebooks and stock dataset are from the

> \[py-fintech-projects](https://github.com/akmadan/py-fintech-projects) repository by the original author.

>

> The product analytics, synthetic event dataset, SQL analysis, dashboard, product insights, PRD, user stories, and competitive teardown were added as part of this case study.



\---



\## Project Overview



The project models an investment-product journey:



```text

User Signup

&#x20;   ↓

KYC Started

&#x20;   ↓

KYC Completed

&#x20;   ↓

Fund Viewed

&#x20;   ↓

Fund Selected

&#x20;   ↓

Investment Started

&#x20;   ↓

Payment Initiated

&#x20;   ↓

Investment Completed



The analytics layer uses synthetic user-event data to answer questions such as:



Where are users dropping off?

How does conversion differ by acquisition channel?

How large are monthly user cohorts?

What product interactions should be instrumented?

What product hypotheses can be tested?

How can analytics findings be translated into product requirements?

Project Architecture

Existing Investment Analysis

&#x20;       │

&#x20;       ▼

Synthetic User Events

&#x20;       │

&#x20;       ▼

&#x20;      SQL

&#x20;       │

&#x20;       ├── Product Metrics

&#x20;       ├── Funnel Analysis

&#x20;       ├── Cohort Analysis

&#x20;       └── Retention Analysis

&#x20;       │

&#x20;       ▼

Streamlit + Plotly Dashboard

&#x20;       │

&#x20;       ▼

Product Insights

&#x20;       │

&#x20;       ▼

PRD + User Stories

&#x20;       │

&#x20;       ▼

Competitive Product Teardown

Dataset



A synthetic investment-product event dataset was generated for the analytics case study.



Dataset size

10,000 users

33,680 events

8 event/data attributes

No missing values

Event types

signup

kyc\_started

kyc\_completed

fund\_viewed

fund\_selected

investment\_started

payment\_initiated

investment\_completed

Products

Mutual Funds

Stocks

ETFs

Acquisition channels

Organic

Paid Search

Partner

Referral

Social Media



The dataset is synthetic and does not represent Upstox customers or any real company's internal data.



Key Analytics Results

Overall Product Metrics

Metric	Result

Total Users	10,000

KYC Completion Rate	67.19%

Fund View Rate	28.27%

Fund View → Selection	63.78%

Signup → Investment Completion	9.74%

Mutual Fund Funnel

Funnel Stage	Users

Signup	4,837

KYC Started	4,364

KYC Completed	3,290

Fund Viewed	2,827

Fund Selected	1,803

Investment Started	1,253

Payment Initiated	1,083

Investment Completed	974



The largest observed downstream opportunity in the synthetic funnel is between Fund Viewed → Fund Selected, where approximately 63.8% of viewers proceed to selection.



This is treated as a product hypothesis rather than a causal conclusion.



Acquisition Channel Analysis



Synthetic mutual-fund discovery data showed the following fund-view → selection conversion:



Acquisition Channel	Conversion

Organic	66.77%

Referral	63.31%

Paid Search	63.30%

Social Media	61.45%

Partner	58.56%



These differences provide a basis for investigating whether acquisition intent, traffic quality, or the investment experience varies by channel.



The analysis does not establish causality.



SQL Analytics



The sql/ directory contains four analytical modules:



sql/

├── 01\_product\_metrics.sql

├── 02\_funnel\_analysis.sql

├── 03\_cohort\_analysis.sql

└── 04\_retention\_analysis.sql

Product Metrics



Measures:



User count

KYC completion

Fund discovery

Fund selection

Investment conversion

Product distribution

Acquisition-channel distribution

Funnel Analysis



Analyzes:



Signup

→ KYC

→ Fund Discovery

→ Selection

→ Investment

→ Completion



and compares conversion across acquisition channels.



Cohort Analysis



Groups users according to their first observed event month.



Retention Analysis



Measures active users across cohort and activity months.



Product Analytics Dashboard



The project includes a Streamlit + Plotly dashboard.



Run it with:



streamlit run dashboard/app.py



The dashboard contains:



KPI cards

Investment funnel

Acquisition-channel performance

Product distribution

Monthly cohorts

Product observations

Event-level data preview

Product Thinking



The analytics findings are translated into product hypotheses rather than simply reporting numbers.



Example hypotheses include:



1\. Investment Discovery Friction



Users may be viewing funds without progressing to selection.



Potential investigation areas:



Search

Filters

Fund details

Risk information

Returns information

Comparison

2\. Acquisition Intent Differences



Differences between acquisition channels may indicate differences in user intent or traffic quality.



This should be investigated using behavioral data rather than assuming causality.



3\. Decision Friction



Users may need better tools to compare funds and understand relevant information before selecting an investment.



Proposed Analytics Instrumentation



Additional product events proposed in the case study:



fund\_search

filter\_used

fund\_comparison\_started

fund\_details\_viewed

risk\_information\_viewed

returns\_information\_viewed

recommendation\_clicked

investment\_amount\_entered



These events would allow a product team to analyze the complete discovery-to-investment journey.



Product Requirements



The product/ directory contains the product-thinking layer:



product/

├── product\_insights.md

├── PRD.md

├── user\_stories.md

└── competitive\_analysis.md

PRD



The PRD proposes improvements around:



Investment discovery

Search and filtering

Fund information

Fund comparison

Decision support

Analytics instrumentation

User Stories



User stories cover:



Investment discovery

Search and filters

Fund information

Fund comparison

Investment flow

Analytics instrumentation

Competitive Analysis



The competitive teardown examines publicly documented capabilities across:



Upstox

Groww

Zerodha Coin

INDmoney



The comparison focuses on investment discovery, fund research, comparison, portfolio context, and decision support.



Product Metrics

Primary Metric



Fund View → Fund Selection Conversion



This metric is used because the case study focuses on improving the investment-discovery and decision stage.



Secondary Metrics

Investment completion rate

Fund-detail engagement

Search usage

Filter usage

Comparison usage

Investment initiation

Guardrail Metrics

Payment failure

Onboarding drop-off

Support/contact rate

Cancellation

Technology Stack

Data \& Analytics

Python

Pandas

NumPy

SQLite

SQL

Dashboard

Streamlit

Plotly

Product Documentation

PRD

User Stories

Product Insights

Competitive Analysis

Development

Git

GitHub

VS Code

Repository Structure

py-fintech-projects/

│

├── 01\_equal\_weights.ipynb

├── 02\_value\_investing.ipynb

├── 03\_dividend\_based\_investing.ipynb

│

├── data/

│   ├── user\_events.csv

│   └── investment\_analytics.db

│

├── sql/

│   ├── 01\_product\_metrics.sql

│   ├── 02\_funnel\_analysis.sql

│   ├── 03\_cohort\_analysis.sql

│   └── 04\_retention\_analysis.sql

│

├── dashboard/

│   └── app.py

│

├── product/

│   ├── product\_insights.md

│   ├── PRD.md

│   ├── user\_stories.md

│   └── competitive\_analysis.md

│

├── generate\_user\_events.py

├── load\_database.py

├── run\_sql.py

└── README.md

Running the Project

1\. Create the environment

python -m venv .venv

2\. Activate it



Windows PowerShell:



.venv\\Scripts\\Activate.ps1

3\. Install dependencies

pip install pandas numpy streamlit plotly

4\. Generate synthetic events

python generate\_user\_events.py

5\. Load the SQLite database

python load\_database.py

6\. Run SQL analysis

python run\_sql.py

7\. Launch the dashboard

streamlit run dashboard/app.py



Important Data Disclaimer



This project uses synthetic user-event data created specifically for demonstrating product analytics workflows.



It does not contain:



Upstox customer data

Internal company metrics

Proprietary product analytics

Real customer behavior

Confidential information



Competitive analysis is based on publicly available product information.



Learning Objectives



This case study demonstrates practical exposure to:



Product analytics

SQL funnel analysis

Cohort analysis

Retention analysis

Product metrics

Event instrumentation

Product hypothesis generation

PRD writing

User-story definition

Competitive product analysis

Dashboard development

Data-driven product thinking

