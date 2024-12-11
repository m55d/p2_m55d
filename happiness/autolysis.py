import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import numpy as np
from scipy import stats

# Set the token directly
os.environ["AIPROXY_TOKEN"] = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjMwMDAyMzJAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.f3-QmDAJOy6xG0QcKXRiP0Q4N3Irc5WIZI6x-UgvDAI"

# Load the CSV file
file_path = r'C:\Users\HP8CG\OneDrive\Desktop\tds p2\happiness.csv'  # Replace with your actual file path

df = pd.read_csv(file_path, encoding='ISO-8859-1')


# 1. Summary Statistics
summary_stats = df.describe()

# 2. Missing Values
missing_values = df.isnull().sum()

# 3. Handle Non-Numeric Columns: Drop or convert them
# Drop non-numeric columns
df_numeric = df.select_dtypes(include=[np.number])

# 4. Handle Missing Values: Drop or Impute (here we'll drop rows with NaN values)
df_numeric = df_numeric.dropna()

# 5. Outlier Detection using Z-Score
z_scores = np.abs(stats.zscore(df_numeric))
outliers = (z_scores > 3).sum(axis=0)

# # 6. Clustering using KMeans
# kmeans = KMeans(n_clusters=3)  # You can adjust the number of clusters
# df['Cluster'] = kmeans.fit_predict(df_numeric)

# 7. Correlation Matrix Calculation (if possible)
try:
    # Calculate correlation matrix only for numeric columns
    correlation_matrix = df_numeric.corr()
except Exception as e:
    print(f"Error calculating correlation matrix: {e}")
    correlation_matrix = None  # Set to None if error occurs

# Visualizations
# Visualization 1: Correlation Heatmap (only if correlation matrix is calculated)
if correlation_matrix is not None:
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.savefig('correlation_heatmap.png')  # Save as PNG
    plt.close()

# Visualization 2: Histogram of all numeric columns
plt.figure(figsize=(12, 8))
df_numeric.hist(bins=30, figsize=(12, 8))
plt.suptitle("Histograms of Numeric Columns")
plt.savefig('histograms.png')  # Save as PNG
plt.close()

# # Visualization 3: Clustering result - Scatter plot of the first two numeric columns
# plt.figure(figsize=(8, 6))
# sns.scatterplot(x=df_numeric.iloc[:, 0], y=df_numeric.iloc[:, 1], hue='Cluster', palette='Set1')
# plt.title("Clustering of Data (KMeans)")
# plt.savefig('clustering.png')  # Save as PNG
# plt.close()

# Save the results to a CSV and MD
summary_stats.to_csv('summary_statistics.csv')
missing_values.to_csv('missing_values.csv')

# Create README.md
with open('README.md', 'w') as file:
    file.write("# Data Analysis Report\n\n")
    file.write("## Summary Statistics\n")
    file.write(summary_stats.to_markdown())
    file.write("\n\n")
    
    file.write("## Missing Values\n")
    file.write(missing_values.to_markdown())
    file.write("\n\n")
    
    if correlation_matrix is not None:
        file.write("## Correlation Heatmap\n")
        file.write("![Correlation Heatmap](correlation_heatmap.png)\n")
        file.write("\n\n")
    
    file.write("## Histograms\n")
    file.write("![Histograms](histograms.png)\n")
    file.write("\n\n")
    
    # file.write("## Clustering Results\n")
    # file.write("![Clustering](clustering.png)\n")
    # file.write("\n\n")
    
    file.write("## Conclusion\n")
    file.write("The analysis provides insight into the dataset's correlations, distributions, and outliers. The clustering analysis suggests potential groupings that could be useful for further analysis.")

print("Analysis complete. Results saved to PNG files and README.md.")
