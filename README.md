# 🛍️ Customer Segmentation

A Streamlit web app that groups customers into segments using **K-Means clustering**. Upload a dataset, and the app finds the best number of clusters automatically with the **elbow method** and shows the result on a scatter chart.

> **Note:** This is a practice project built for learning.

<!-- Add a screenshot of the app here:
![App screenshot](Images/screenshot.png)
-->

## 📌 About the Project

Businesses often want to understand what kinds of customers they have. This app takes customer data (for example, annual income and spending score), groups similar customers together, and shows the groups visually, so you can see patterns such as high-income big spenders or low-income careful spenders.

## ✨ Features

- Upload your own dataset as **CSV or Excel (.xlsx)**
- Choose which columns to cluster on
- The best number of clusters (K) is found **automatically** using the elbow method
- Shows the data table with the cluster label for each customer
- Interactive scatter chart colored by cluster

## ⚙️ How It Works

1. **Upload** a CSV or Excel file.
2. **Select features** (columns) to use for clustering.
3. **Find K:** `elbow.py` trains K-Means for K = 1 to 10, records the WCSS (within-cluster sum of squares) for each, and uses the `kneed` library to locate the "elbow" point where adding more clusters stops helping much.
4. **Train the final model** with that K and assign a cluster label to every row.
5. **Visualize** the clusters on a scatter chart.

## 📊 Dataset

The app is designed for the **Mall Customers** dataset (available on Kaggle). By default it uses these two columns:

- `Annual Income (k$)`
- `Spending Score (1-100)`

Other numeric datasets can work too, as long as they contain those column names (see Limitations).

## 🗂️ Project Structure

```
customer-segmentation/
├── app.py              # Streamlit app
├── elbow.py            # Elbow method to find the best K
├── requirements.txt    # Python dependencies
├── Images/             # App logo
└── README.md
```

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rajdeep-M/customer-segmentation.git
   cd customer-segmentation
   ```

2. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

The app opens in your browser at `http://localhost:8501`.

## 💡 How to Use

1. Click **Browse files** and upload your dataset.
2. Keep the default features or choose your own.
3. View the table of labeled customers and the cluster scatter chart.

## ⚠️ Limitations

- The scatter chart currently plots `Annual Income (k$)` against `Spending Score (1-100)`, so it expects those columns to be present.
- Features are not scaled before clustering. K-Means is distance-based, so columns with large values (like income) can dominate columns with small values.
- Clustering is unsupervised, so there is no accuracy score. The clusters should be judged by whether they make business sense.

## 🔭 Possible Improvements

- Scale features with `StandardScaler` before clustering
- Let the user choose the chart's X and Y columns
- Add silhouette score to evaluate cluster quality
- Show a summary of each cluster (average income, average spending)

## 🛠️ Built With

Python · Pandas · Scikit-learn · Kneed · Streamlit · Openpyxl

## 👤 Author

**Rajdeep**