import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Enterprise Fraud Intelligence System",
    page_icon="🛡️",
    layout="wide"
)

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("Fraud Intelligence System")

st.sidebar.markdown("""
### Dashboard Sections

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
### Project Information

- IEEE-CIS Fraud Detection
- XGBoost Intelligence Model
- Explainable AI using SHAP
- Enterprise Risk Segmentation
""")

# =========================================
# HEADER
# =========================================

st.title("Enterprise Fraud Detection Intelligence System")

st.markdown("""
Advanced fraud analytics platform powered by machine learning,
Explainable AI, operational risk segmentation, and enterprise intelligence.
""")

# =========================================
# KPI SECTION
# =========================================

st.subheader("Executive Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Dataset Size",
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

# =========================================
# TABS
# =========================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Fraud Analytics",
    "Model Performance",
    "Explainable AI",
    "Risk Intelligence",
    "Fraud Simulator"
])

# =========================================
# TAB 1 — FRAUD ANALYTICS
# =========================================

with tab1:

    st.header("Fraud Analytics & Dataset Intelligence")

    st.markdown("""
    This section analyzes fraud behavior patterns,
    transactional anomalies, and dataset characteristics.
    """)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Fraud Distribution")

        fraud_img = Image.open(
            "../charts/fraud_distribution.png"
        )

        st.image(
            fraud_img,
            use_container_width=True
        )

    with col2:

        st.subheader("Product Fraud Risk")

        product_img = Image.open(
            "../charts/product_fraud_risk.png"
        )

        st.image(
            product_img,
            use_container_width=True
        )

    st.subheader("Transaction Amount Risk Analysis")

    amount_img = Image.open(
        "../charts/transaction_amount_risk.png"
    )

    st.image(
        amount_img,
        use_container_width=True
    )

    st.subheader("Missing Values Analysis")

    missing_img = Image.open(
        "../charts/missing_values_analysis.png"
    )

    st.image(
        missing_img,
        use_container_width=True
    )

# =========================================
# TAB 2 — MODEL PERFORMANCE
# =========================================

with tab2:

    st.header("Machine Learning Performance")

    metrics = pd.DataFrame({

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
        metrics,
        use_container_width=True
    )

    st.subheader("Model Comparison Visualization")

    model_img = Image.open(
        "../charts/model_comparison.png"
    )

    st.image(
        model_img,
        use_container_width=True
    )

    st.markdown("""
    ### Why XGBoost Performed Best

    XGBoost achieved the strongest fraud discrimination
    capability due to its ability to capture nonlinear
    transaction behavior patterns and complex feature
    interactions common in financial fraud systems.
    """)

# =========================================
# TAB 3 — EXPLAINABLE AI
# =========================================

with tab3:

    st.header("Explainable AI & Fraud Intelligence")

    st.markdown("""
    SHAP explainability provides transparency into
    model predictions by identifying the features
    contributing most strongly to fraud classification.
    """)

    shap_img = Image.open(
        "../charts/shap_summary.png"
    )

    st.image(
        shap_img,
        caption="SHAP Feature Contribution Analysis",
        use_container_width=True
    )

    st.subheader("Top Fraud Risk Features")

    feature_img = Image.open(
        "../charts/top_fraud_features.png"
    )

    st.image(
        feature_img,
        use_container_width=True
    )

    st.markdown("""
    ### Key Explainability Insights

    - Behavioral transaction variables were dominant fraud drivers.
    - Email domain intelligence contributed strongly to fraud prediction.
    - Transaction frequency and anomaly variables influenced high-risk classification.
    - Explainable AI improves analyst trust and operational transparency.
    """)

# =========================================
# TAB 4 — RISK INTELLIGENCE
# =========================================

with tab4:

    st.header("Fraud Risk Intelligence")

    col1, col2 = st.columns(2)

    with col1:

        risk_img = Image.open(
            "../charts/risk_segmentation.png"
        )

        st.image(
            risk_img,
            use_container_width=True
        )

    with col2:

        risk_rate_img = Image.open(
            "../charts/risk_level_fraud_rate.png"
        )

        st.image(
            risk_rate_img,
            use_container_width=True
        )

    st.markdown("""
    ### Operational Risk Insights

    - High-risk transactions showed extremely elevated fraud probability.
    - Medium-risk transactions require secondary review workflows.
    - Low-risk transactions demonstrated significantly lower fraud exposure.
    - Risk segmentation enables efficient fraud investigation prioritization.
    """)

# =========================================
# TAB 5 — FRAUD SIMULATOR
# =========================================

with tab5:

    st.header("Interactive Fraud Risk Simulator")

    st.markdown("""
    Simulate fraud risk scoring using transaction characteristics.
    """)

    transaction_amt = st.slider(
        "Transaction Amount",
        1,
        5000,
        500
    )

    product_code = st.selectbox(
        "Product Code",
        ["W", "C", "H", "S", "R"]
    )

    email_risk = st.selectbox(
        "Email Domain Risk",
        ["Low", "Medium", "High"]
    )

    card_risk = st.selectbox(
        "Card Risk Level",
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

            st.error("High Risk Transaction")

        elif risk_score >= 40:

            st.warning("Medium Risk Transaction")

        else:

            st.success("Low Risk Transaction")

# =========================================
# BUSINESS IMPACT
# =========================================

st.divider()

st.header("Operational Fraud Intelligence Insights")

st.markdown("""
### Business Impact

This enterprise fraud intelligence system demonstrates how
machine learning and Explainable AI can support:

- fraud prevention
- operational monitoring
- financial risk reduction
- intelligent investigation prioritization
- enterprise risk management
- analyst decision support systems

### Technical Highlights

- XGBoost Fraud Intelligence Modeling
- Explainable AI using SHAP
- Risk Segmentation Framework
- Enterprise Dashboard Development
- Fraud Analytics & Visualization
- Operational Intelligence Reporting
""")

# =========================================
# DOWNLOAD SECTION
# =========================================

st.divider()

summary_text = """
Enterprise Fraud Detection Intelligence System

Key Highlights:
- XGBoost achieved highest ROC-AUC
- SHAP identified major fraud drivers
- High-risk transactions showed elevated fraud exposure
- Risk segmentation enabled operational prioritization
"""

st.download_button(
    label="Download Fraud Intelligence Summary",
    data=summary_text,
    file_name="fraud_intelligence_summary.txt"
)

# =========================================
# FOOTER
# =========================================

st.divider()

st.caption(
    "Developed by Palakurthi Venkatesh Goud | AI & Data Analytics Intern"
)