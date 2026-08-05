# Loan Approval Prediction using Machine Learning

## Project Overview

This project focuses on building a machine learning classification model that predicts whether a loan application will be approved or rejected based on applicant financial and personal information.

The project demonstrates the fundamental machine learning workflow, including data preprocessing, feature selection, model training, evaluation, and comparison of different classification algorithms.

The main objective is to understand how machine learning models learn from historical data and use those patterns to make predictions on new loan applications.

---

# Problem Statement

Loan approval decisions involve analyzing multiple factors such as income, credit score, loan amount, and financial assets.

This project aims to develop a predictive model that can assist in classifying loan applications as:

- Approved
- Rejected

The model is trained using historical loan application data to identify patterns that influence loan approval decisions.

---

# Dataset

The dataset contains information about loan applicants and their financial details.

## Features

| Feature | Description |
|---------|-------------|
| loan_id | Unique identifier for each loan application |
| no_of_dependents | Number of dependents of the applicant |
| education | Applicant education level |
| self_employed | Employment status of the applicant |
| income_annum | Applicant annual income |
| loan_amount | Requested loan amount |
| loan_term | Loan repayment period |
| cibil_score | Applicant credit score |
| residential_assets_value | Value of residential assets |
| commercial_assets_value | Value of commercial assets |
| luxury_assets_value | Value of luxury assets |
| bank_asset_value | Value of bank assets |

## Target Variable

`loan_status`

The model predicts whether the loan application is:

- Approved
- Rejected

---

# Technologies Used

## Programming Language

- Python

## Libraries

- Pandas - Used for data loading, cleaning, and manipulation
- Scikit-learn - Used for machine learning model development, training, and evaluation

---

# Machine Learning Workflow

The project follows a standard machine learning workflow:
