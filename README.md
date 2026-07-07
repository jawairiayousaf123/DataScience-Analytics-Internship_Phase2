# Term Deposit Subscription Prediction

## 🎯 Task Objective
The primary objective of this project is to build an explanatory predictive modeling framework to determine which bank customers are highly likely to accept a term deposit marketing offer. By utilizing historical demographic, financial, and campaign transaction footprints from the Bank Marketing Dataset, this project helps the bank move away from broad cold-calling strategies toward data-driven targeting. This maximizes consumer marketing conversion rates while dropping operational outbound calling costs.

---

## 🛠️ Approach & Methodology

The repository implements a structured, end-to-end data science and machine learning pipeline:

1. **Dataset Integrity Verification:**
   * Loaded the comprehensive dataset consisting of 45,211 rows and 17 features.
   * Conducted full schema audits and verified target label properties, revealing a heavily imbalanced conversion baseline (~11.7% "yes" responses).

2. **Exploratory Data Analysis (EDA):**
   * Generated distribution and frequency profiles across target variables, continuous features (`age`, `duration`), and categorical attributes (`job`, `marital`).
   * Evaluated direct interactions between customer job categories and success behaviors to isolate high-conversion corporate demographics.

3. **Data Preparation & Structural Preprocessing:**
   * Automated text-to-numeric transformations using `LabelEncoder` across all nominal characteristics while mapping the target variable `y` into binary fields ($0$ for 'no', $1$ for 'yes').
   * Partitioned the feature space ($X$) from the target space ($y$) and executed a robust **80/20 train-test split** to ensure reliable model validation.

4. **Classifier Optimization & Comparative Metrics:**
   * Trained and optimized a **Random Forest Classifier** to handle complex, non-linear relationships within the customer data.
   * Critically assessed performance metrics including precision, recall, and multi-dimensional confusion matrices to look past baseline accuracy biases.

5. **Business Value Feature Extraction:**
   * Extracted internal model weights (`model.feature_importances_`) to map and rank exactly which operational attributes carry the heaviest decision-making weight for term deposit conversions.

---

## 📊 Results and Insights

### 1. Model Diagnostic Performance Summary
The Random Forest model demonstrated robust predictive power with an **AUC-ROC score of 0.93**, effectively distinguishing between potential subscribers and non-subscribers.
* **Overcoming Imbalance:** By focusing on the AUC-ROC metric rather than simple accuracy, the model successfully captures the nuances of the minority "yes" class.
* **High Reliability:** The model's ability to minimize false negatives ensures that the marketing team captures a significant majority of interested leads.

### 2. Strategic Feature Weights & Business Insights
Evaluating the feature importance scores yielded highly actionable bank operational strategies:

1. **The 'Golden Minute' (`duration`):** The duration of the phone call is overwhelmingly the strongest predictor of customer conversion. Sales agents must be trained with engaging call hooks to prolong connectivity, as lengthier, high-quality interactions strongly correlate with customer acceptance.
2. **Financial Capacity (`balance`):** Customers with higher account balances demonstrate a greater propensity to invest in term deposits, suggesting that financial liquidity is a key driver for product adoption.
3. **Historical Loyalty (`poutcome_success`):** Customers who had a successful outcome in previous marketing campaigns are significantly more likely to subscribe again. Future campaigns should prioritize these historical leads to maximize ROI.

---

## 📁 Repository File Structure
* `bank-full.csv` - Complete production source dataset containing 45,211 interactions.
* `Term_Deposit.ipynb` - Comment-supported Jupyter Notebook documenting all cleaning scripts, visual distributions, classification metrics, and importance plots.
* `README.md` - Executive summary documentation.
