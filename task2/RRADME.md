# Mall Customer Segmentation Using Unsupervised Learning

## 🎯 Task Objective
The goal of this project is to perform customer segmentation on the Mall Customers dataset. By applying unsupervised learning techniques, we aim to group customers based on their annual income and spending patterns, enabling the development of personalized marketing strategies for each segment.

---

## 🛠️ Approach & Methodology

1. **Exploratory Data Analysis (EDA):**
   * Conducted univariate and bivariate analysis on `Annual Income` and `Spending Score` to identify patterns.
   * Visualized the correlation between features to verify the necessity of clustering.

2. **K-Means Clustering:**
   * Used the **Elbow Method** to determine the optimal number of clusters ($k=5$).
   * Executed the K-Means algorithm to group customers into distinct segments based on behavioral similarity.

3. **Dimensionality Reduction (PCA):**
   * Utilized **Principal Component Analysis (PCA)** to reduce the feature space.
   * Successfully visualized high-dimensional clusters in a 2D plot, confirming distinct separation between customer segments.

4. **Business Insight Generation:**
   * Calculated cluster means to derive actionable business strategies for each specific customer profile.

---

## 📊 Marketing Strategies per Segment

| Cluster | Characteristics | Proposed Marketing Strategy |
| :--- | :--- | :--- |
| **Cluster 1 & 3** | High Income | **Premium Loyalty Programs:** Exclusive early access and personalized high-end offers. |
| **Cluster 2** | Low Income, High Spending | **Installment Plans:** Promotion of credit options and frequent, smaller value deals. |
| **Cluster 0** | Mid-Range | **Standard Campaigns:** Balanced promotions to maintain engagement. |
| **Cluster 4** | Low Income, Low Spending | **Budget-Conscious:** Value-based marketing and entry-level product promotions. |

---

## 📁 Repository File Structure
* `Mall_Customers.csv` - The original customer dataset.
* `Mall_Customer.ipynb` - Notebook containing the full pipeline, from EDA to PCA visualization.
* `README.md` - Project documentation.
