import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================
# INVESTMENT PRODUCT ANALYTICS
# Synthetic User Event Generator
# ============================================================

np.random.seed(42)

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

NUM_USERS = 10_000

START_DATE = "2026-01-01"
END_DATE = "2026-09-01"

USERS = [f"U{str(i).zfill(5)}" for i in range(1, NUM_USERS + 1)]

ACQUISITION_CHANNELS = [
    "Organic",
    "Referral",
    "Paid Search",
    "Social Media",
    "Partner"
]

CHANNEL_PROBABILITIES = [
    0.35,
    0.20,
    0.20,
    0.15,
    0.10
]

PRODUCTS = [
    "Mutual Funds",
    "Stocks",
    "ETFs"
]

PRODUCT_PROBABILITIES = [
    0.50,
    0.35,
    0.15
]


# ------------------------------------------------------------
# Generate users
# ------------------------------------------------------------

user_df = pd.DataFrame({
    "user_id": USERS,

    "signup_date": pd.to_datetime(
        np.random.choice(
            pd.date_range(
                START_DATE,
                END_DATE
            ),
            size=NUM_USERS
        )
    ),

    "acquisition_channel": np.random.choice(
        ACQUISITION_CHANNELS,
        size=NUM_USERS,
        p=CHANNEL_PROBABILITIES
    ),

    "primary_product": np.random.choice(
        PRODUCTS,
        size=NUM_USERS,
        p=PRODUCT_PROBABILITIES
    )
})


# ------------------------------------------------------------
# Generate event history
# ------------------------------------------------------------

event_rows = []


for _, user in user_df.iterrows():

    user_id = user["user_id"]
    signup_date = user["signup_date"]
    channel = user["acquisition_channel"]
    product = user["primary_product"]

    # ========================================================
    # 1. SIGNUP
    # ========================================================

    event_rows.append({
        "user_id": user_id,
        "event": "signup",
        "event_timestamp": signup_date,
        "product": product,
        "acquisition_channel": channel
    })


    # ========================================================
    # 2. KYC STARTED
    # 90% of users
    # ========================================================

    if np.random.random() < 0.90:

        kyc_started = signup_date + pd.Timedelta(
            hours=np.random.randint(1, 48)
        )

        event_rows.append({
            "user_id": user_id,
            "event": "kyc_started",
            "event_timestamp": kyc_started,
            "product": product,
            "acquisition_channel": channel
        })


        # ====================================================
        # 3. KYC COMPLETED
        # 75% of users who start KYC
        # ====================================================

        if np.random.random() < 0.75:

            kyc_completed = kyc_started + pd.Timedelta(
                hours=np.random.randint(1, 72)
            )

            event_rows.append({
                "user_id": user_id,
                "event": "kyc_completed",
                "event_timestamp": kyc_completed,
                "product": product,
                "acquisition_channel": channel
            })


            # =================================================
            # MUTUAL FUND PRODUCT FUNNEL
            # =================================================

            if product == "Mutual Funds":

                # ---------------------------------------------
                # 4. FUND VIEWED
                # 85% of KYC-completed MF users
                # ---------------------------------------------

                if np.random.random() < 0.85:

                    fund_viewed = kyc_completed + pd.Timedelta(
                        hours=np.random.randint(1, 96)
                    )

                    event_rows.append({
                        "user_id": user_id,
                        "event": "fund_viewed",
                        "event_timestamp": fund_viewed,
                        "product": "Mutual Funds",
                        "acquisition_channel": channel
                    })


                    # -----------------------------------------
                    # 5. FUND SELECTED
                    # 65%
                    # -----------------------------------------

                    if np.random.random() < 0.65:

                        fund_selected = fund_viewed + pd.Timedelta(
                            hours=np.random.randint(1, 48)
                        )

                        event_rows.append({
                            "user_id": user_id,
                            "event": "fund_selected",
                            "event_timestamp": fund_selected,
                            "product": "Mutual Funds",
                            "acquisition_channel": channel
                        })


                        # -------------------------------------
                        # 6. INVESTMENT STARTED
                        # 70%
                        # -------------------------------------

                        if np.random.random() < 0.70:

                            investment_started = (
                                fund_selected
                                + pd.Timedelta(
                                    hours=np.random.randint(1, 24)
                                )
                            )

                            event_rows.append({
                                "user_id": user_id,
                                "event": "investment_started",
                                "event_timestamp": investment_started,
                                "product": "Mutual Funds",
                                "acquisition_channel": channel
                            })


                            # ---------------------------------
                            # 7. PAYMENT INITIATED
                            # 85%
                            # ---------------------------------

                            if np.random.random() < 0.85:

                                payment_initiated = (
                                    investment_started
                                    + pd.Timedelta(
                                        hours=np.random.randint(1, 12)
                                    )
                                )

                                event_rows.append({
                                    "user_id": user_id,
                                    "event": "payment_initiated",
                                    "event_timestamp": payment_initiated,
                                    "product": "Mutual Funds",
                                    "acquisition_channel": channel
                                })


                                # -----------------------------
                                # 8. INVESTMENT COMPLETED
                                # 90%
                                # -----------------------------

                                if np.random.random() < 0.90:

                                    investment_completed = (
                                        payment_initiated
                                        + pd.Timedelta(
                                            hours=np.random.randint(1, 12)
                                        )
                                    )

                                    event_rows.append({
                                        "user_id": user_id,
                                        "event": "investment_completed",
                                        "event_timestamp": investment_completed,
                                        "product": "Mutual Funds",
                                        "acquisition_channel": channel
                                    })


# ------------------------------------------------------------
# Convert to DataFrame
# ------------------------------------------------------------

events_df = pd.DataFrame(event_rows)


# ------------------------------------------------------------
# Clean and sort data
# ------------------------------------------------------------

events_df["event_timestamp"] = pd.to_datetime(
    events_df["event_timestamp"]
)

events_df = events_df.sort_values(
    ["user_id", "event_timestamp"]
).reset_index(drop=True)


# ------------------------------------------------------------
# Add analytics-friendly fields
# ------------------------------------------------------------

events_df["event_date"] = (
    events_df["event_timestamp"]
    .dt.date
)

events_df["week"] = (
    events_df["event_timestamp"]
    .dt.to_period("W")
    .astype(str)
)

events_df["month"] = (
    events_df["event_timestamp"]
    .dt.to_period("M")
    .astype(str)
)


# ------------------------------------------------------------
# Save dataset
# ------------------------------------------------------------

OUTPUT_DIR = Path("data")

OUTPUT_DIR.mkdir(
    exist_ok=True
)

OUTPUT_FILE = OUTPUT_DIR / "user_events.csv"

events_df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ------------------------------------------------------------
# Print summary
# ------------------------------------------------------------

print("=" * 60)
print("INVESTMENT PRODUCT ANALYTICS")
print("Synthetic User Event Generator")
print("=" * 60)

print(f"\nCreated: {OUTPUT_FILE}")

print(f"Users: {events_df['user_id'].nunique():,}")

print(f"Total events: {len(events_df):,}")

print("\nEvent distribution:")
print(
    events_df["event"]
    .value_counts()
    .to_string()
)

print("\nProduct distribution:")
print(
    events_df["product"]
    .value_counts()
    .to_string()
)

print("\nAcquisition channel distribution:")
print(
    events_df["acquisition_channel"]
    .value_counts()
    .to_string()
)

print("\nFirst 10 rows:")
print(
    events_df.head(10).to_string(index=False)
)

print("\n" + "=" * 60)
print("Dataset generation complete!")
print("=" * 60)