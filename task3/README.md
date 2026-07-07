# ⚡ Energy Load Forecasting Using Machine Learning

## 🎯 Task Objective
The goal of this project is to perform short-term load forecasting on the Household Power Consumption dataset. By applying both statistical and machine learning techniques, we aim to predict "Global Active Power" and identify consumption patterns, enabling efficient energy management and grid optimization.

---

## 🛠️ Approach & Methodology

1. **Data Preprocessing:**
    * Cleaned raw time-series data by handling missing values (`?`) and resampling to a consistent **hourly frequency**.
    * Converted multi-variate data into a numeric format and utilized **forward-fill** to ensure data continuity.

2. **Feature Engineering:**
    * Extracted temporal features (`hour`, `dayofweek`) to capture daily and weekly cycles.
    * Created binary indicators (`is_weekend`) to distinguish between varying consumer behaviors during weekdays and weekends.

3. **Model Development & Training:**
    * **ARIMA:** Applied for baseline linear time-series forecasting.
    * **Prophet:** Leveraged for seasonal decomposition and trend analysis.
    * **XGBoost:** Implemented as an ensemble learning approach to capture complex, non-linear dependencies in energy load.

4. **Evaluation & Visualization:**
    * Compared models using **Mean Absolute Error (MAE)** and **Root Mean Square Error (RMSE)**.
    * Visualized Actual vs. Forecasted usage to confirm the model's predictive reliability.

---

## 📊 Performance Summary

| Model | MAE | Key Strength |
| :--- | :--- | :--- |
| **XGBoost** | **0.5046** | High precision in tracking rapid load fluctuations. |
| **Prophet** | - | Strong performance in capturing seasonal trends. |
| **ARIMA** | - | Effective baseline for stable linear trends. |

---

## 📁 Repository File Structure
* `household_power_consumption.txt` - The original raw energy consumption dataset.
* `Energy_Forecasting.ipynb` - Notebook containing the full pipeline, from data cleaning to model comparison and visualization.
* `README.md` - Project documentation and implementation guidelines.

## 💾 Dataset Information
* **Source**: Sourced from the UCI Machine Learning Repository (Individual household electric power consumption Data Set).
* **Scale**: Contains over 2 million measurements collected over nearly 4 years (2006–2010).
* **Note on Large Files**: Due to the file size, it is recommended to store the dataset in Google Drive and mount it to your notebook environment for seamless access.
