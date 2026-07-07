# 📊 Executive Sales Dashboard

## 🎯 Task Objective
The goal of this project is to develop an interactive Business Intelligence (BI) dashboard to analyze the "Global Superstore" dataset. This tool enables stakeholders to gain real-time insights into regional sales performance, profitability, and customer behavior through dynamic filtering.

## 🛠️ Technical Approach
1. **Data Loading & Preprocessing:** 
   * Loaded the Global Superstore dataset using `pandas`.
   * Performed necessary encoding (`ISO-8859-1`) to handle special characters.
2. **Interactive Filtering:** 
   * Implemented sidebar filters for `Region`, `Category`, and `Sub-Category` to allow deep-dive analysis.
3. **Data Visualization:**
   * Calculated KPIs for Total Sales and Profit.
   * Developed interactive bar charts using `plotly.express` to visualize the top 5 performing customers.
4. **Deployment:** 
   * Built and deployed the dashboard using **Streamlit**, ensuring a responsive and user-friendly web interface.

## 📈 Dashboard Features
* **Dynamic Slicing:** Filter data instantly across multiple dimensions.
* **KPI Monitoring:** Real-time visibility of financial performance.
* **Customer Analysis:** Visual identification of top revenue-driving customers.

## 📁 Project Structure
* `app.py` - The main Python script containing the Streamlit dashboard code.
* `Global_Superstore2.csv` - The source dataset.
* `requirements.txt` - Configuration file listing dependencies (`streamlit`, `pandas`, `plotly`).
* `README.md` - Documentation for the project.

## 🚀 Accessing the Dashboard
* **Live Demo:**(https://jawairiayousaf123-datascience-analytics-interns-task5app-um4tg4.streamlit.app/)
* **Local Run:** 
  ```bash
  pip install streamlit pandas plotly
  streamlit run app.py
