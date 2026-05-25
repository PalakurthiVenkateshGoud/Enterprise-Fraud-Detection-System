# Enterprise Fraud Detection Intelligence System

## Overview

This project presents an end-to-end Enterprise Fraud Detection Intelligence System developed using the IEEE-CIS Fraud Detection dataset. The system combines machine learning, Explainable AI, operational risk segmentation, and interactive dashboarding to identify fraudulent financial transactions and generate actionable fraud intelligence insights.

The project was designed to simulate a real-world enterprise fraud analytics workflow involving data preprocessing, fraud behavior analysis, predictive modeling, explainability, and risk intelligence visualization.

---

## Key Features

- Fraud Detection using Machine Learning
- Explainable AI using SHAP
- Enterprise Risk Segmentation
- XGBoost Fraud Intelligence Modeling
- Fraud Analytics Dashboard using Streamlit
- Fraud Risk Simulator
- Operational Fraud Insights
- Interactive Data Visualization

---

## Dataset Information

Dataset Used:
IEEE-CIS Fraud Detection Dataset

Files Used:
- train_transaction.csv
- train_identity.csv

Dataset Source:
Kaggle – IEEE-CIS Fraud Detection Competition

The transaction and identity datasets were merged using the `TransactionID` column to create a unified fraud intelligence dataset.

---

## Technologies Used

### Programming Language
- Python

### Libraries & Frameworks
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP
- Streamlit
- Imbalanced-learn
- Pillow

---

## Project Structure

```plaintext
FraudDetection_[Palakurthi Venkatesh Goud]/

│
├── charts/
│   ├── fraud_distribution.png
│   ├── missing_values_analysis.png
│   ├── model_comparison.png
│   ├── product_fraud_risk.png
│   ├── risk_level_fraud_rate.png
│   ├── risk_segmentation.png
│   ├── shap_summary.png
│   ├── top_fraud_features.png
│   └── transaction_amount_risk.png
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── train_transaction.csv
│   └── train_identity.csv
│
├── models/
│
├── outputs/
│
├── summary/
│   └── summary.pdf
│
├── analysis.ipynb
├── requirements.txt
└── README.md
```

---

## Exploratory Data Analysis

The project includes extensive fraud analytics and exploratory data analysis:

- Fraud vs Non-Fraud Distribution
- Product-wise Fraud Risk Analysis
- Transaction Amount Risk Analysis
- Missing Value Intelligence
- Fraud Risk Segmentation

---

## Machine Learning Models

The following models were implemented and evaluated:

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|------|------|------|------|------|------|
| Logistic Regression | 0.741 | 0.192 | 0.331 | 0.243 | 0.601 |
| Random Forest | 0.924 | 0.882 | 0.458 | 0.603 | 0.889 |
| XGBoost | 0.922 | 0.858 | 0.455 | 0.594 | 0.897 |

### Best Performing Model
XGBoost achieved the strongest fraud detection capability with the highest ROC-AUC score and effective fraud discrimination performance.

---

## Explainable AI using SHAP

SHAP (SHapley Additive exPlanations) was implemented to improve model transparency and identify the most influential fraud-driving features.

### Key Explainability Insights

- Behavioral transaction variables strongly influenced fraud prediction
- Product category risk significantly impacted model output
- Transaction anomalies contributed to high-risk classification
- Explainable AI improved operational transparency

---

## Fraud Risk Segmentation

Transactions were categorized into:

- Low Risk
- Medium Risk
- High Risk

This risk segmentation framework helps prioritize fraud investigations and operational monitoring.

### Key Risk Insight

High-risk transactions demonstrated extremely elevated fraud probability compared to low-risk transactions.

---

## Streamlit Dashboard

An enterprise-level interactive fraud analytics dashboard was developed using Streamlit.

### Dashboard Features

- Executive KPI Metrics
- Fraud Analytics Visualizations
- Model Performance Evaluation
- Explainable AI Visualizations
- Fraud Risk Intelligence
- Interactive Fraud Simulator
- Operational Fraud Insights

---

## Business Impact

This project demonstrates how machine learning and Explainable AI can support:

- Fraud Prevention
- Financial Risk Reduction
- Operational Monitoring
- Intelligent Investigation Prioritization
- Enterprise Decision Support Systems

---

## How to Run the Project

### Step 1 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2 — Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Dashboard Preview

The dashboard provides:

- Fraud analytics intelligence
- SHAP explainability
- Model evaluation
- Risk segmentation
- Fraud simulation

---

## Conclusion

This project successfully demonstrates an enterprise-level fraud intelligence pipeline integrating machine learning, Explainable AI, operational analytics, and interactive dashboarding.

The system provides accurate fraud detection, interpretable predictions, and actionable risk intelligence suitable for real-world financial fraud analysis workflows.

---

## Live Dashboard

Streamlit Deployment:
https://enterprise-fraud-detection-system.streamlit.app/#fraud-distribution

## Developed By

Palakurthi Venkatesh Goud  
AI & Data Analytics Intern
