# 📊 Sales Data Analysis Report

## 📌 Project Overview
This project focuses on analyzing a sales dataset using Python and pandas to extract meaningful insights such as total revenue, best-performing product, and key statistical metrics.

---

## 🎯 Objectives
- Calculate total sales revenue
- Identify the best-selling product
- Compute average, highest, and lowest sales
- Perform basic data cleaning and validation

---

## 🛠 Tools & Technologies Used
- Python
- Pandas Library

---

## ⚙️ Setup Instructions
1. Install Python on your system
2. Install pandas using the following command:
   pip install pandas
3. Place the dataset (`sales_data.csv`) in the project folder
4. Run the Python script:
   python sales_analysis.py

---

## 📂 Project Structure
sales-data-analysis/
│
├── sales_analysis.py # Main Python script
├── sales_data.csv # Dataset file
├── analysis_report.md # Project report
├── requirements.txt # Dependencies


---

## 🔍 Steps Performed

### 1. Data Loading
- Loaded the dataset using pandas:
  `pd.read_csv()`

### 2. Data Exploration
- Checked dataset shape (rows and columns)
- Viewed column names and data types
- Used `df.info()` to understand structure

### 3. Data Cleaning
- Checked for missing values using `isnull().sum()`
- No missing values were found
- Removed duplicate rows using `drop_duplicates()`

### 4. Data Analysis
- Calculated total sales using `sum()`
- Identified best-selling product using `groupby()` and `idxmax()`
- Calculated average sales using `mean()`
- Found highest and lowest sales using `max()` and `min()`

---

## 📊 Key Findings

- **Total Sales:** ₹12365048  
- **Best Selling Product:** Laptop  
- **Average Sales:** ₹123650.48  
- **Highest Sale:** ₹373932  
- **Lowest Sale:** ₹6540  

---

## 🧹 Data Cleaning Summary
The dataset was checked for missing values, and none were found. Duplicate rows were removed to ensure accuracy and consistency of data.

---

## 📌 How Requirements Were Met

- ✔ Used pandas for data loading and analysis  
- ✔ Handled missing values (validated dataset cleanliness)  
- ✔ Calculated more than 3 metrics (total, average, max, min, best product)  
- ✔ Created a structured and formatted report  
- ✔ Added clear explanations for each step  

---

## 📈 Conclusion
The analysis shows that **Laptop** is the top-performing product, generating the highest revenue. The dataset was clean and well-structured, making the analysis straightforward and reliable.

