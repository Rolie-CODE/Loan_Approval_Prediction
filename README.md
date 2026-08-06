# Loan Approval Prediction API using Machine Learning

## Project Overview

This project is a machine learning-powered loan approval prediction system that predicts whether a loan application is likely to be approved or rejected based on applicant financial and personal information.

The project started as a machine learning classification experiment and was extended into a REST API that allows external applications to send loan application details and receive predictions in real time.

The goal of this project is to understand the complete machine learning workflow, from data preprocessing and model training to deploying a trained model as an API.

---

# Project Goal

The final goal of this project is to build a Loan Approval Prediction API that allows users or applications to submit applicant information and receive an automated loan approval prediction.

The completed system consists of:

- A trained machine learning classification model
- Data preprocessing and feature handling
- Model evaluation and comparison
- Saved machine learning model
- FastAPI backend service
- Prediction endpoint for real-time predictions

---

# System Workflow


User/Application
|
↓
Send Loan Information
|
↓
FastAPI Prediction API
|
↓
Load Trained Machine Learning Model
|
↓
Generate Prediction
|
↓
Return Loan Approval Result


---

# Dataset

The dataset contains historical loan application records with applicant financial information.

## Features

| Feature | Description |
|---------|-------------|
| no_of_dependents | Number of dependents |
| education | Education level |
| self_employed | Employment status |
| income_annum | Annual income |
| loan_amount | Requested loan amount |
| loan_term | Loan repayment period |
| cibil_score | Credit score |
| residential_assets_value | Residential asset value |
| commercial_assets_value | Commercial asset value |
| luxury_assets_value | Luxury asset value |
| bank_asset_value | Bank asset value |

## Target Variable

`loan_status`

The model predicts the loan application outcome.

---

# Technologies Used

## Programming Language

- Python

## Libraries

- Pandas - Data loading, cleaning, and manipulation
- Scikit-learn - Machine learning model training and evaluation
- FastAPI - Building the prediction API
- Uvicorn - Running the API server
- Pickle - Saving and loading trained models

---

# Machine Learning Process

The project follows the machine learning workflow:


Load Dataset
|
↓
Clean Data
|
↓
Process Categorical Features
|
↓
Separate Features and Target
|
↓
Split Training and Testing Data
|
↓
Train Classification Models
|
↓
Evaluate Performance
|
↓
Save Best Model
|
↓
Deploy Model Through API


---

# Data Preprocessing

Before training the models, the dataset was prepared by:

## Cleaning Data

- Removing unnecessary spaces from column names
- Ensuring consistent feature names

Example:


" loan_status"


was converted into:


"loan_status"


---

## Handling Categorical Data

Categorical features were converted into numerical values so that machine learning algorithms could process them.

Processed categorical features include:

- Education
- Self-employed status
- Loan status

---

# Models Implemented

## Logistic Regression

Used as a baseline classification model.

Purpose:

- Establish initial performance
- Understand the relationship between input features and loan decisions

---

## Decision Tree Classifier

A tree-based classification algorithm that learns decision rules from historical loan data.

Example:


IF credit score is high
AND income is sufficient

THEN approve loan


Decision Trees are useful for datasets where relationships between features are not purely linear.

---

# Model Evaluation

The models were evaluated using accuracy score.

Accuracy measures how many predictions the model correctly classified.

Formula:


Accuracy = Correct Predictions / Total Predictions


---

# Model Results

| Model | Accuracy |
|------|----------|
| Logistic Regression | ~70% |
| Decision Tree | ~97% |

The Decision Tree model achieved higher accuracy on the test dataset and was selected for API integration.

Further evaluation is being performed to ensure the model is not relying on dataset imbalance and is making meaningful predictions.

---

# API Development

The trained model was converted into a REST API using FastAPI.

## Available Endpoint

### Prediction Endpoint


POST /predict


The endpoint accepts loan application information and returns a prediction.
