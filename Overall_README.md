
# Autolysis: Automated Data Analysis, Visualization, and Storytelling

Autolysis is a Python-based tool that automates data analysis, generates visualizations, and narrates a story from any given dataset in CSV format. The script performs essential exploratory data analysis (EDA), creates meaningful visualizations, and uses an LLM (Large Language Model) to generate a narrative describing the insights, patterns, and recommendations from the analysis.

## Key Features
- **Data Analysis**: Automatically performs basic statistical analysis, including detecting missing values, generating summary statistics, and calculating correlations.
- **Visualization**: Generates charts such as correlation matrices and histograms to help visualize trends and patterns in the data.
- **Storytelling**: Leverages GPT-4o-Mini to generate a compelling story based on the analysis, summarizing key findings and offering recommendations.
- **Markdown Output**: Outputs a README file with both the narrative and visualizations to help communicate the insights.

## How It Works
### 1. Data Loading and Analysis
The script begins by loading the provided CSV file and performing an initial analysis:
- Summary statistics (mean, median, std deviation, etc.)
- Detection of missing or null values
- Correlation analysis between numerical features

### 2. Visualization Generation
- The script generates charts to visually represent relationships in the data.
    - A **heatmap** of the correlation matrix to visualize how numerical variables relate to each other.
    - **Histograms** of numerical columns to show distributions.

### 3. Storytelling
- The analysis results are fed into an AI model (GPT-4o-Mini), which then generates a detailed narrative that:
    - Describes the dataset and its key statistics.
    - Highlights significant findings from the analysis.
    - Offers actionable insights or recommendations for further investigation.

### 4. Output
- **README.md**: Contains a summary of the analysis, the AI-generated narrative, and visualizations.
- **Charts**: Saves the generated charts as PNG images in the output directory.
  
## Example Workflow
To run the tool, simply use the following command:

```bash
uv run autolysis.py dataset.csv
```

This will generate:
- **README.md**: A markdown file with the analysis and insights.
- **PNG images**: Visualizations such as correlation matrices and distribution histograms.

## Example Output
The script outputs:
- **Data Analysis**: A summary of key statistics and missing values.
- **Charts**:
  - A correlation matrix heatmap.
  - Distributions of numerical columns via histograms.
- **Generated Narrative**: A text-based summary that provides insights and recommendations based on the data.

## Requirements
Before running the script, make sure you have the following libraries installed:
- pandas
- seaborn
- matplotlib
- numpy

You can install the required libraries using pip:
```bash
pip install pandas seaborn matplotlib numpy openai
```

### Notes:
- The script uses the **OpenAI GPT-4o-Mini** API for generating narratives.
- Ensure that the **AIPROXY_TOKEN** environment variable is set to authenticate the API connection.

## Conclusion
Autolysis is a powerful tool for anyone looking to quickly analyze data, generate visualizations, and understand the insights hidden within their datasets. By combining traditional statistical analysis with AI-driven storytelling, this script offers a comprehensive and automated approach to data exploration and reporting.

---

This README captures the essence of what the project does, how it works, and provides usage instructions. It also clearly explains the steps involved in the process and gives a detailed description of the output files generated.
