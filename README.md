# Healthcare Patient Risk Stratification

> **Analysing patient diagnostic patterns across demographic cohorts to build risk stratification models that support clinical decision-making.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-11557c?style=flat)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production%20Ready-22c55e?style=flat)

<br>

## The problem

Healthcare providers sit on enormous volumes of patient data but lack tools to proactively identify at-risk individuals before conditions escalate. Manual chart reviews are slow, inconsistent, and don't scale. This project builds a data-driven risk stratification engine that analyses diagnostic patterns, demographic factors, and medical history to classify patients by risk level — giving clinicians a prioritised list of who needs attention most.

<br>

## Key results

| Metric | Outcome |
|--------|---------|
| Diseases analysed | 10+ diagnostic categories |
| Risk tiers produced | Low / Medium / High |
| Demographic factors modelled | Age, gender, region, comorbidities |
| Model accuracy | Classification F1 > 0.84 |
| Clinical use case | Supports triage and preventive care planning |

<br>

## System architecture

```
Raw patient records (CSV)
        │
        ▼
┌─────────────────────┐
│  Data ingestion &   │  ← Patient demographics, diagnoses,
│  preprocessing      │    vitals, visit history
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Exploratory        │  ← Disease frequency, age distribution,
│  data analysis      │    comorbidity mapping, missing data audit
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Feature engineering│  ← Risk score proxies, comorbidity count,
│                     │    visit frequency, demographic encoding
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Risk classification│  ← Logistic Regression, Random Forest,
│  model              │    Decision Tree — cross-validated
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Insight report     │  ← Risk tier output, visualisations,
│                     │    demographic breakdowns
└─────────────────────┘
```

<br>

## Project structure

```
healthcare-patient-data-analysis/
│
├── data/
│   ├── raw/                        # Original patient datasets
│   └── processed/                  # Cleaned, encoded data
│
├── notebooks/
│   ├── 01_eda.ipynb                # Disease and demographic exploration
│   ├── 02_feature_engineering.ipynb
│   └── 03_risk_model.ipynb
│
├── src/
│   ├── preprocess.py               # Data cleaning pipeline
│   ├── features.py                 # Feature engineering logic
│   ├── model.py                    # Training and evaluation
│   └── visualise.py                # Chart generation utilities
│
├── outputs/
│   └── risk_stratification_report.pdf
│
├── requirements.txt
└── README.md
```

<br>

## Quickstart

```bash
git clone https://github.com/sinchanamuddi/Cognetix_Healthcare_Patient_Data-Analysis.git
cd Cognetix_Healthcare_Patient_Data-Analysis
pip install -r requirements.txt
python src/preprocess.py --input data/raw/patients.csv
python src/model.py
python src/visualise.py
```

<br>

## How it works

### 1. Data preprocessing
- Null value handling with imputation for vitals and flagging for missing diagnoses
- Categorical encoding for disease types, gender, and region
- Normalisation of continuous variables (age, BMI, visit count)
- Train / validation / test split stratified by risk class

### 2. Exploratory data analysis
- Disease frequency distribution across age groups
- Comorbidity heatmap showing which conditions co-occur most
- Gender and regional breakdowns of high-risk patients
- Correlation matrix of clinical features vs risk outcome

### 3. Feature engineering
- Comorbidity count per patient (sum of concurrent diagnoses)
- Visit frequency ratio (recent vs historical)
- Age-risk tier proxy encoded from clinical domain knowledge
- Binary flags for high-signal conditions (diabetes, hypertension, etc.)

### 4. Model selection

| Model | F1 Score | Precision | Recall |
|-------|----------|-----------|--------|
| Logistic Regression (baseline) | 0.76 | 0.74 | 0.78 |
| Decision Tree | 0.80 | 0.79 | 0.81 |
| Random Forest | 0.84 | 0.83 | 0.85 |

Random Forest selected as final model for its balance of accuracy and interpretability via feature importance scores.

### 5. Risk stratification output
Each patient receives a risk tier (Low / Medium / High) with top contributing features driving their score, recommended follow-up priority, and cohort comparison against similar demographic groups.

<br>

## Dependencies

```
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
matplotlib==3.7.2
seaborn==0.12.2
joblib==1.3.2
```

<br>

## What I learned

- **Domain knowledge accelerates feature engineering.** Knowing that diabetes and hypertension together signal high risk let me build a comorbidity flag that outperformed raw numeric features alone.
- **Class imbalance is the silent killer in healthcare ML.** Most patients are low-risk. Without stratified splitting and weighted loss functions, models just predict low risk for everyone and achieve deceptive accuracy.
- **Interpretability matters more than accuracy in clinical contexts.** A 0.84 F1 Random Forest is only useful if a clinician can understand why a patient was flagged — feature importance charts were as important as the model itself.

<br>

## Roadmap

- [ ] Survival analysis for time-to-event risk modelling
- [ ] SHAP values for per-patient explainability
- [ ] Integration with EHR APIs
- [ ] Streamlit dashboard for clinical team use
- [ ] Longitudinal tracking — risk score changes over time

<br>

## Author

**Sinchana M** — ML Engineer and GenAI Systems Builder

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/sinchana-m-sd)
[![Email](https://img.shields.io/badge/Email-sinchanamuddi%40gmail.com-EA4335?style=flat&logo=gmail)](mailto:sinchanamuddi@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-sinchanamuddi.github.io-000?style=flat&logo=github)](https://sinchanamuddi.github.io)

*If this project was useful to you, a ⭐ on GitHub goes a long way!*
