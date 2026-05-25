import streamlit as st
import pandas as pd
from PIL import Image
import os

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Enterprise Fraud Detection Intelligence System",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# PATH CONFIGURATION
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CHARTS_DIR = os.path.join(
    BASE_DIR,
    "charts"
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Fraud Intelligence System")

st.sidebar.markdown("""
## Dashboard Sections

- Executive Overview
- Fraud Analytics
- Model Performance
- Explainable AI
- Risk Segmentation
- Fraud Simulator
- Business Intelligence
""")

st.sidebar.divider()

st.sidebar.markdown("""
## Project Information

- IEEE-CIS Fraud Detection
- XGBoost Fraud Intelligence
- SHAP Explainability
- Enterprise Risk Analytics
- Fraud Segmentation System
""")

# =========================================================
# HEADER
# =========================================================

st.title("Enterprise Fraud Detection Intelligence System")

st.markdown("""
Advanced enterprise fraud intelligence platform powered by machine learning,
Explainable AI, operational risk segmentation, and fraud analytics.
""")

# =========================================================
# EXECUTIVE METRICS
# =========================================================

st.header("Executive Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Transactions",
    "590K+"
)

col2.metric(
    "Fraud Rate",
    "3.5%"
)

col3.metric(
    "Best ROC-AUC",
    "89.7%"
)

col4.metric(
    "High Risk Fraud",
    "95.7%"
)

st.divider()

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Fraud Analytics",
    "Model Performance",
    "Explainable AI",
    "Risk Intelligence",
    "Fraud Simulator"
])

# =========================================================
# TAB 1 — FRAUD ANALYTICS
# =========================================================

with tab1:

    st.header("Fraud Analytics & Dataset Intelligence")

    st.markdown("""
    This section analyzes fraud behavior patterns,
    transaction anomalies, and dataset intelligence.
    """)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Fraud Distribution")

        fraud_img = Image.open(
            os.path.join(
                CHARTS_DIR,
                "fraud_distribution.png"
            )
        )

        st.image(
            fraud_img,
            use_container_width=True
        )

    with col2:

        st.subheader("Product Fraud Risk")

        product_img = Image.open(
            os.path.join(
                CHARTS_DIR,
                "product_fraud_risk.png"
            )
        )

        st.image(
            product_img,
            use_container_width=True
        )

    st.subheader("Transaction Amount Risk Analysis")

    amount_img = Image.open(
        os.path.join(
            CHARTS_DIR,
            "transaction_amount_risk.png"
        )
    )

    st.image(
        amount_img,
        use_container_width=True
    )

    st.subheader("Missing Values Analysis")

    missing_img = Image.open(
        os.path.join(
            CHARTS_DIR,
            "missing_values_analysis.png"
        )
    )

    st.image(
        missing_img,
        use_container_width=True
    )

# =========================================================
# TAB 2 — MODEL PERFORMANCE
# =========================================================

with tab2:

    st.header("Machine Learning Model Performance")

    metrics_df = pd.DataFrame({

        "Model": [
            "Logistic Regression",
            "Random Forest",
            "XGBoost"
        ],

        "Accuracy": [
            0.741,
            0.924,
            0.922
        ],

        "Precision": [
            0.192,
            0.882,
            0.858
        ],

        "Recall": [
            0.331,
            0.458,
            0.455
        ],

        "F1-Score": [
            0.243,
            0.603,
            0.594
        ],

        "ROC-AUC": [
            0.601,
            0.889,
            0.897
        ]
    })

    st.dataframe(
        metrics_df,
        use_container_width=True
    )

    st.subheader("Model Comparison")

    model_img = Image.open(
        os.path.join(
            CHARTS_DIR,
            "model_comparison.png"
        )
    )

    st.image(
        model_img,
        use_container_width=True
    )

    st.success(
        "XGBoost achieved the strongest fraud detection performance."
    )

# =========================================================
# TAB 3 — EXPLAINABLE AI
# =========================================================

with tab3:

    st.header("Explainable AI & Fraud Intelligence")

    st.markdown("""
    SHAP Explainability identifies which variables most strongly
    influenced fraud predictions.
    """)

    shap_img = Image.open(
        os.path.join(
            CHARTS_DIR,
            "shap_summary.png"
        )
    )

    st.image(
        shap_img,
        use_container_width=True
    )

    st.subheader("Top Fraud Risk Features")

    feature_img = Image.open(
        os.path.join(
            CHARTS_DIR,
            "top_fraud_features.png"
        )
    )

    st.image(
        feature_img,
        use_container_width=True
    )

    st.info("""
    Key fraud drivers included:
    - V257
    - V258
    - V201
    - Transaction behavior variables
    - Email intelligence patterns
    """)

# =========================================================
# TAB 4 — RISK INTELLIGENCE
# =========================================================

with tab4:

    st.header("Fraud Risk Intelligence")

    col1, col2 = st.columns(2)

    with col1:

        risk_img = Image.open(
            os.path.join(
                CHARTS_DIR,
                "risk_segmentation.png"
            )
        )

        st.image(
            risk_img,
            use_container_width=True
        )

    with col2:

        risk_rate_img = Image.open(
            os.path.join(
                CHARTS_DIR,
                "risk_level_fraud_rate.png"
            )
        )

        st.image(
            risk_rate_img,
            use_container_width=True
        )

    st.warning("""
    High-risk transactions demonstrated significantly elevated
    fraud probability requiring immediate analyst review.
    """)

# =========================================================
# TAB 5 — FRAUD SIMULATOR
# =========================================================

with tab5:

    st.header("Interactive Fraud Risk Simulator")

    transaction_amt = st.slider(
        "Transaction Amount",
        1,
        5000,
        500
    )

    product_code = st.selectbox(
        "Product Code",
        ["W", "C", "H", "R", "S"]
    )

    email_risk = st.selectbox(
        "Email Domain Risk",
        ["Low", "Medium", "High"]
    )

    card_risk = st.selectbox(
        "Card Risk",
        ["Low", "Medium", "High"]
    )

    risk_score = 0

    if transaction_amt > 2000:
        risk_score += 30

    if product_code == "C":
        risk_score += 30

    if email_risk == "High":
        risk_score += 20

    if card_risk == "High":
        risk_score += 20

    if st.button("Analyze Fraud Risk"):

        st.subheader("Fraud Risk Analysis")

        st.metric(
            "Predicted Fraud Probability",
            f"{risk_score}%"
        )

        if risk_score >= 75:

            st.error(
                "High Risk Transaction"
            )

        elif risk_score >= 40:

            st.warning(
                "Medium Risk Transaction"
            )

        else:

            st.success(
                "Low Risk Transaction"
            )

# =========================================================
# BUSINESS INTELLIGENCE
# =========================================================

st.divider()

st.header("Operational Fraud Intelligence Insights")

st.markdown("""
### Key Business Insights

- XGBoost demonstrated highest fraud discrimination capability.
- SHAP Explainability improved fraud transparency.
- Product category C showed elevated fraud exposure.
- Risk segmentation improved operational prioritization.
- Fraud analytics supported intelligent monitoring workflows.

### Technical Highlights

- Enterprise Fraud Detection
- Explainable AI using SHAP
- XGBoost Intelligence Modeling
- Fraud Risk Segmentation
- Interactive Dashboard Deployment
- Operational Fraud Analytics
""")

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Developed by Palakurthi Venkatesh Goud | AI & Data Analytics"
)
