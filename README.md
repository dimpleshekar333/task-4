# Breast Cancer Data Analysis

This project performs basic **data exploration** and **visualization**
on a breast cancer dataset using Python. The analysis includes
understanding dataset structure, handling missing data, statistical
summaries, and visualizing feature relationships.

## 📂 Dataset

-   **File:** `data (1).csv`\
-   The dataset contains various features related to breast cancer
    diagnoses.\
-   The **target variable** is `diagnosis`, which indicates whether the
    tumor is **Benign (B)** or **Malignant (M)**.

------------------------------------------------------------------------

## 🛠️ Requirements

Make sure you have the following Python libraries installed:

``` bash
pip install pandas matplotlib seaborn
```

------------------------------------------------------------------------

## 📜 Code Workflow

### 1. **Import Libraries**

``` python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

### 2. **Load Dataset**

``` python
file_path = r"C:\Users\Dimple.S\Downloads\data (1).csv"
df = pd.read_csv(file_path)
```

### 3. **Data Cleaning**

-   Dropped any empty or unnecessary columns (e.g., `Unnamed: 32`).\
-   Checked for missing values and basic dataset info.

### 4. **Exploratory Data Analysis (EDA)**

-   **Dataset Shape & Columns:** Displays dataset dimensions and feature
    names.\
-   **Missing Values:** Checks for null values in the dataset.\
-   **Class Distribution:** Counts the number of benign and malignant
    cases.\
-   **Statistical Summary:** Displays mean, standard deviation, and
    other stats for numerical columns.

### 5. **Visualization**

-   **Count Plot:** Distribution of diagnoses (Benign vs Malignant).\
-   **Correlation Heatmap:** Shows relationships between features using
    a heatmap.

------------------------------------------------------------------------

## 📊 Sample Outputs

### Diagnosis Distribution

Shows how many tumors are **benign** vs **malignant**.

### Correlation Heatmap

Helps identify highly correlated features for further analysis.

------------------------------------------------------------------------

## 🚀 How to Run

1.  Save the script as `breast_cancer_analysis.py`.\
2.  Place `data (1).csv` in the specified path or update `file_path`.\
3.  Run the script:

``` bash
python breast_cancer_analysis.py
```

4.  Visualizations will appear as pop-ups.

------------------------------------------------------------------------

## 📌 Next Steps

-   Perform **feature engineering** for better insights.\
-   Build a **classification model** using algorithms like **Logistic
    Regression** or **Random Forest**.\
-   Evaluate model performance using metrics like **accuracy**,
    **precision**, and **recall**.
