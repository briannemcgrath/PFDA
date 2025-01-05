# Programming for Data Analytics Project Repository 

This repository contains code and resoruces related to project carried out for the Programming for Data Analytics module. 

## Project Overview: 
This project aims to demonstrate my skills in data analysis, showcasing techniques and tools I've learned thoughout the module. The analysis is based on a [bank transaction dataset](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection/data) which includes transaction records and customer details. The main goal of this project is to identify patterns that may indicate potentially fraudulent behaviour. 

## Dataset Overview: 

The dataset, linked above, contains the following features: 
- **TransactionID:** Unique identifier for each transaction.
- **AccountID:** Unique identifier for the customer's account. 
- **TransactionAmount:** Amount ($) involved in the transaction. 
- **TransactionDate:** Date and time the transaction took place. 
- **Location:** Location in which the transaction was made. 
- **DeviceID:** Device used for the transaction. 
- **IP Address:** IP address in which the transaction originiated. 
- **MerchantID:** ID of the merchant involved in the transaction. 
- **CustomerAge:** Age of the customer making the transaction. 
- **TransactionDuration:** Duration of the transaction. 
- **LoginAttempts:** Number of login attempts before a successful transaction. 
- **AccountBalance:** Balance in the customer's account at the time of the transaction. 
- **PreviousTransactionDate:** The date of the previous transaction made by the customer.  

## Prerequisites/How to Run: 
Before running the code, ensure you have the following: 
- Python 
- Required libraries: 
    - `pandas` 
    - `numpy` 
    - `matplotlib`
    - `seaborn`
    - `skikit-learn`
    - `sqlite3`(Built-in with Python)
- Clone this repository and run the Jupyter Notebook `project.ipynb`. 

The notebook contains information on loading the dataset, performing exploratory data analysis, applying machine learning models for anomaly detection, and storing anomalies in an SQLite database for querying. 

## **References:**

### **Visualisation:**
- https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html (Stacked Bar Charts)
- https://seaborn.pydata.org/generated/seaborn.barplot.html (Bar Plots)

### **Pandas:**
- https://www.slingacademy.com/article/pandas-dataframe-grouping-rows-by-day-of-the-week/ (Grouping Rows by Day of the Week)
- https://www.statology.org/pandas-group-by-hour/ (Grouping Data by Hour)

### **Interquartile Range (IQR):**
- https://en.wikipedia.org/wiki/Interquartile_range (Overview)
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html (IQR in pandas)

## **Future Work:**
- **Lack of Labeled Fraud Data:** The model currently uses unsupervised anomaly detection techniques (due to lack of labels in the original dataset). Future work could involve incorporating labeld fraud data to train a predictive model. 
- **Feature enhancement**: Further exploration of additional features could improve the detection of fraudulent transactions.

## Acknowledgements: 
This repository was developed as part of coursework for the Higher Diploma in Science in Computing in Data Analytics with Atlantic Technological University. Special thanks to lecturer Andrew Beatty for guidance and support. 

**by Brianne McGrath**