import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="Investment Product Analytics",
    page_icon="📊",
    layout="wide"
)

DB_PATH = "data/investment_analytics.db"


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    connection = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM user_events",
        connection
    )

    connection.close()

    df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])
    df["event_date"] = pd.to_datetime(df["event_date"])

    return df


df = load_data()


# ============================================================
# HEADER
# ============================================================

st.title("📊 Investment Product Analytics Dashboard")

st.markdown(
    """
    **Product analytics case study for a digital investment platform**

    Synthetic user-event dataset used to analyze acquisition,
    onboarding, investment funnel performance and user behavior.
    """
)

st.divider()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_users = df["user_id"].nunique()

signup_users = df.loc[
    df["event"] == "signup",
    "user_id"
].nunique()

kyc_completed = df.loc[
    df["event"] == "kyc_completed",
    "user_id"
].nunique()

fund_viewed = df.loc[
    df["event"] == "fund_viewed",
    "user_id"
].nunique()

fund_selected = df.loc[
    df["event"] == "fund_selected",
    "user_id"
].nunique()

investment_completed = df.loc[
    df["event"] == "investment_completed",
    "user_id"
].nunique()

kyc_rate = kyc_completed / signup_users * 100

investment_rate = investment_completed / signup_users * 100

fund_view_rate = fund_viewed / signup_users * 100

fund_selection_rate = fund_selected / fund_viewed * 100


# ============================================================
# KPI CARDS
# ============================================================

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Users",
    f"{total_users:,}"
)

col2.metric(
    "KYC Completion",
    f"{kyc_rate:.2f}%"
)

col3.metric(
    "Fund View Rate",
    f"{fund_view_rate:.2f}%"
)

col4.metric(
    "Fund Selection",
    f"{fund_selection_rate:.2f}%"
)

col5.metric(
    "Investment Conversion",
    f"{investment_rate:.2f}%"
)


st.divider()


# ============================================================
# FUNNEL
# ============================================================

st.subheader("Investment Funnel")

funnel_events = [
    "signup",
    "kyc_started",
    "kyc_completed",
    "fund_viewed",
    "fund_selected",
    "investment_started",
    "payment_initiated",
    "investment_completed"
]

funnel_labels = [
    "Signup",
    "KYC Started",
    "KYC Completed",
    "Fund Viewed",
    "Fund Selected",
    "Investment Started",
    "Payment Initiated",
    "Investment Completed"
]

funnel_data = []

for event, label in zip(funnel_events, funnel_labels):

    users = df.loc[
        df["event"] == event,
        "user_id"
    ].nunique()

    funnel_data.append({
        "Stage": label,
        "Users": users
    })

funnel_df = pd.DataFrame(funnel_data)

fig_funnel = px.funnel(
    funnel_df,
    x="Users",
    y="Stage",
    title="User Conversion Funnel"
)

st.plotly_chart(
    fig_funnel,
    use_container_width=True
)


# ============================================================
# ACQUISITION CHANNEL
# ============================================================

st.subheader("Acquisition Channel Performance")

channel_view = df[
    df["event"] == "fund_viewed"
].groupby(
    "acquisition_channel"
)["user_id"].nunique()

channel_selection = df[
    df["event"] == "fund_selected"
].groupby(
    "acquisition_channel"
)["user_id"].nunique()

channel_df = pd.DataFrame({
    "Fund Viewed": channel_view,
    "Fund Selected": channel_selection
}).fillna(0)

channel_df["Conversion %"] = (
    channel_df["Fund Selected"]
    / channel_df["Fund Viewed"]
    * 100
)

channel_df = channel_df.reset_index()

fig_channel = px.bar(
    channel_df,
    x="acquisition_channel",
    y="Conversion %",
    title="Fund View → Selection Conversion",
    text_auto=".2f"
)

st.plotly_chart(
    fig_channel,
    use_container_width=True
)


# ============================================================
# PRODUCT DISTRIBUTION
# ============================================================

st.subheader("Product Distribution")

product_df = (
    df.groupby("product")["user_id"]
    .nunique()
    .reset_index()
)

product_df.columns = [
    "Product",
    "Users"
]

fig_product = px.pie(
    product_df,
    names="Product",
    values="Users",
    title="Users by Investment Product"
)

st.plotly_chart(
    fig_product,
    use_container_width=True
)


# ============================================================
# MONTHLY USER COHORTS
# ============================================================

st.subheader("Monthly User Cohorts")

cohort_df = (
    df.groupby(
        df["event_timestamp"].dt.to_period("M")
    )["user_id"]
    .nunique()
    .reset_index()
)

cohort_df["event_timestamp"] = (
    cohort_df["event_timestamp"]
    .astype(str)
)

cohort_df.columns = [
    "Month",
    "Users"
]

fig_cohort = px.bar(
    cohort_df,
    x="Month",
    y="Users",
    title="Monthly Active User Cohorts",
    text_auto=True
)

st.plotly_chart(
    fig_cohort,
    use_container_width=True
)


# ============================================================
# PRODUCT INSIGHTS
# ============================================================

st.subheader("🔎 Product Observations")

st.markdown(
    f"""
    **1. Onboarding:**  
    {kyc_rate:.2f}% of signed-up users completed KYC.

    **2. Product discovery:**  
    {fund_view_rate:.2f}% of the total user base reached the fund-view stage.

    **3. Fund selection:**  
    {fund_selection_rate:.2f}% of fund viewers proceeded to select a fund.

    **4. Investment conversion:**  
    {investment_rate:.2f}% of signed-up users completed an investment.

    **5. Acquisition:**  
    Fund view → selection conversion varies across acquisition channels,
    indicating an opportunity to investigate differences in user intent,
    traffic quality or product experience.
    """
)


# ============================================================
# DATA PREVIEW
# ============================================================

with st.expander("View Event Data"):

    st.dataframe(
        df.head(100),
        use_container_width=True
    )