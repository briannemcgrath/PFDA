# Programming for Data Analytics Project Repository 

This repository contains code and resources related to project carried out for the Programming for Data Analytics module. 

## Project Overview: 
This project aims to demonstrate my skills in data analysis, showcasing techniques and tools I've learned throughout the module. The analysis is based on a [bank transaction dataset](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection/data) which includes transaction records and customer details. 

The main goal of this project is to analyse customers spending habits and identify patterns that may indicate potentially fraudulent behaviour. 

## Dataset Overview: 

The dataset, linked above, contains the following features: 
- **TransactionID:** Unique identifier for each transaction.
- **AccountID:** Unique identifier for the customer's account. 
- **TransactionAmount:** Amount ($) involved in the transaction. 
- **TransactionDate:** Date and time the transaction took place. 
- **Location:** Location in which the transaction was made. 
- **DeviceID:** Device used for the transaction. 
- **IP Address:** IP address in which the transaction originated. 
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
- Clone this repository and run the Jupyter Notebook `project.ipynb`- this is where the analysis and code are implemented. 

The notebook contains information on loading the dataset, performing exploratory data analysis, applying machine learning models for anomaly detection, and storing anomalies in an SQLite database for querying. 

### **Installation:**
To install the necessary dependencies, create a virtual environment and use the following command in bash:

pip install -r requirements.txt

## **References:**

### **Data Cleaning & Preprocessing:**
- https://www.kdnuggets.com/2023/08/7-steps-mastering-data-cleaning-preprocessing-techniques.html(Overview for Cleaning and Preprocessing)

### **Regular Expression:**
- https://docs.python.org/3/library/re.html (Regular Expression Operations)

### **Visualisation:**
- https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html (Stacked Bar Charts)
- https://seaborn.pydata.org/generated/seaborn.barplot.html (Bar Plots)
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html (Pie Charts)

### **Pandas:**
- https://www.slingacademy.com/article/pandas-dataframe-grouping-rows-by-day-of-the-week/ (Grouping Rows by Day of the Week)
- https://www.statology.org/pandas-group-by-hour/ (Grouping Data by Hour)

### **Interquartile Range (IQR):**
- https://en.wikipedia.org/wiki/Interquartile_range (Overview of IQR)
- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html (IQR in pandas)

### **Machine Learning:**
- https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.IsolationForest.html (Isolation Forest)
- https://scikit-learn.org/dev/auto_examples/ensemble/plot_isolation_forest.html (Isolation Forest Example)
- https://www.analyticsvidhya.com/blog/2021/07/anomaly-detection-using-isolation-forest-a-complete-guide/ (Anomaly Detection using Isolation Forest)

### **SQLite:**
- https://www.w3schools.com/sql/default.asp (Overview of SQL)
- https://www.w3schools.com/python/python_mysql_getstarted.asp (SQL in Python )
- https://www.simplilearn.com/tutorials/sql-tutorial/what-is-sql (Guide on SQL Basics)

## **Next Steps:**
- Incorporating **labeled fraud data** would allow for supervised machine learning models to be developed, improving the accuracy of fraud detection.
- Further exploration of **additional features** could enhance the model’s ability to identify fraudulent transactions.
- **Model refinement**: Experimenting with more advanced anomaly detection techniques such as Autoencoders or Isolation Forest hyperparameter tuning could yield even better results.

## **Known Issues:**
- The model was built using unsupervised anomaly detection, which might lead to false positives/negatives without labeled fraud data.
- The time-based analysis was limited by the availability of data during bank hours.

## Acknowledgements: 
This repository was developed as part of coursework for the Higher Diploma in Science in Computing in Data Analytics with Atlantic Technological University. Special thanks to lecturer Andrew Beatty for guidance and support. 

**by Brianne McGrath**