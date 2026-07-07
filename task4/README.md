# 🏦 Loan Default Risk Prediction & Cost Optimization

## 🎯 Task Objective
The objective of this project is to predict the likelihood of a loan default using the Home Credit Default Risk dataset and optimize the decision threshold based on a cost-benefit analysis to minimize total business loss.

## 🛠️ Approach & Methodology
1.  **Data Cleaning & Preprocessing:** Handled missing values using median imputation and performed label encoding for categorical variables.
2.  **Binary Classification:** Trained a `LogisticRegression` model with `StandardScaler` to handle data scaling and convergence issues.
3.  **Cost-Based Optimization:** Defined a cost function where False Negatives (missed defaults) are more costly than False Positives (rejected good customers), identifying an optimal threshold of **0.10**.
4.  **Performance Evaluation:** Validated the model using AUC-ROC, Precision-Recall curves, and a Confusion Matrix to ensure robust risk identification.

## 📊 Business Interpretation
*   **Optimal Threshold (0.10):** By lowering the threshold to 0.10, the bank prioritizes identifying actual defaulters (Recall), effectively mitigating high-impact financial losses.
*   **Key Drivers:** Analysis shows that `AMT_CREDIT` and `AMT_GOODS_PRICE` are the strongest predictors of default risk.
*   **Result:** The model achieved an **AUC Score of 0.74**, serving as a strategic asset for data-driven credit risk management.

## 📁 Repository File Structure
* `Loan_Default_Analysis.ipynb` - The complete pipeline including EDA, modeling, and cost optimization.
* `README.md` - Project documentation.

## 💾 Data Availability
* Due to the large size of the `application_train.csv` dataset, it is not included in this repository. 
* You can download the dataset from the original **(https://www.kaggle.com/c/home-credit-default-risk/data)**.

## 🚀 How to Run
1. Clone this repository.
2. Download the `application_train.csv` file from the link above and place it in the same directory as the notebook.
3. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
