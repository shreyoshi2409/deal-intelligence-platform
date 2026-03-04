# Deal Intelligence

## Introduction

Deal Intelligence is a data-driven application designed to streamline and enhance the process of deal analysis and management. The repository provides tools and scripts for data extraction, transformation, and visualization, primarily focused on financial transactions, market analytics, and risk evaluation. The project leverages Python, Jupyter Notebooks, and a suite of data science libraries to deliver actionable insights from raw deal data.

**Deal Intelligence Dashboard Overview**

The Deal Intelligence Dashboard is an AI-powered tool for sales teams. It analyzes deals in real time to support decisions. It enhances traditional CRM systems by generating follow-up emails, assessing deal risk, and providing actionable insights.

**Key Capabilities**

- AI-generated personalized follow-up emails  
- Risk scoring and win probability  
- Deal decay detection  
- Explainable reasoning  
- Strategic recommendations  
- Session-level analytics  

**Features**

- **Deal Decay Detection**  
  - Flags deals with no recent contact and neutral or negative sentiment  
  - Warns when deals enter a decay phase  

- **Win Probability**  
  - Uses the formula `win_probability = 100 - risk_score`  
  - Indicates deal momentum  

- **Explainability Layer**  
  - Explains risk based on last contact  
  - Includes client sentiment  
  - Considers deal value  

- **Strategic Recommendations**  
  - High risk leads to urgent follow-up or escalation  
  - Medium risk leads to personalized follow-up  
  - High win probability leads to focus on closing  

- **Session-Level Analytics**  
  - Tracks deals analyzed  
  - Highlights high-risk deals  
  - Shows overall trends  

**Demo Scenarios**

- High Risk and Decay – Zoho CRM Africa Partner Integration  
- Low Risk and Momentum – Zoho CRM Startup Accelerator Program  
- Medium Risk – Zoho ERP India SME Expansion  

## Features

- Automated data extraction from various financial documents and sources.
- Data cleaning and transformation pipelines for consistent analysis.
- Visualization modules to represent key transaction metrics and risk factors.
- Interactive Jupyter Notebooks for exploratory analysis and reporting.
- Modular and extensible codebase for adding new data sources and analysis types.

## Requirements

- Python 3.x
- Jupyter Notebook
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- openpyxl
- Additional dependencies as specified in the repository files

All required packages should be installed via pip:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/shreyoshi2409/Deal-Intelligence.git
   cd Deal-Intelligence
   ```

2. **Install Dependencies**

   Install the required Python packages using the provided requirements file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Data Preparation**

   Place your data files (e.g., Excel, CSV, or other supported formats) in the appropriate input directory as indicated by the scripts or notebooks.

4. **Running Notebooks**

   Open the Jupyter Notebooks for interactive analysis:

   ```bash
   jupyter notebook
   ```

   Open the desired notebook (e.g., `Deal_Analysis.ipynb`) and follow the step-by-step instructions within the notebook to load data, process it, and generate visualizations.

5. **Executing Scripts**

   Some modules may be run directly as Python scripts. Refer to script-specific comments and docstrings for usage details. For example:

   ```bash
   python scripts/data_extraction.py
   ```

6. **Customizing Analysis**

   Modify notebook parameters or script configurations to adjust for your specific data sources, reporting needs, or analytical models.

7. **Viewing Results**

   Generated outputs, such as cleaned datasets and plots, are saved in designated output directories or displayed within the notebook interface for further review and interpretation.

---

For more details on specific modules, refer to in-line documentation and comments within the codebase.