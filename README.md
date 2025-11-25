# 📊 Model 2 – Demand Elasticity & Pricing Scenario Simulator  
### Python (Statsmodels) + Power BI Dashboard + Store Clustering  

This repository contains a complete **pricing & demand analytics system**, combining  
**Python-based Log Elasticity Modeling** with a fully interactive **Power BI Scenario Simulator**.

It is designed for retail, FMCG, e-commerce, and any business where **price, promotion, and footfall** impact revenue.

# 🔧 Key Features

### ✅ **1. Log-Elasticity Demand Model (Python, Statsmodels)**
- Estimates **price elasticity of demand**
- Captures effects of:
  - Price change (log-log regression)
  - Footfall
  - Promotions (binary)
  - Store fixed-effects (optional)
- Produces:
  - Baseline predictions  
  - Elasticity coefficients  
  - Daily sales forecasts  

### ✅ **2. Scenario Simulator (Python → Power BI)**
Python generates all scenarios:

| Variable | Range |
|---------|--------|
| PriceChange | –30% → +30% |
| FootfallChange | –10% / 0 / +10% |
| PromoOverride | 0 / 1 |

For *every combination*, model predicts:

- `Sales_Pred`
- `Revenue_Pred`
- `ABV_Scn` (Average Basket Value)
- `ScenarioID`

Output is saved as:
data/scenarios/model2_scenarios.csv

Power BI uses this file to allow **real-time scenario testing**.

### ✅ **3. Store-Level Segmentation (Clustering)**
KMeans algorithm identifies distinct store groups:

- **High elasticity stores** – sensitive to price drops  
- **Inelastic stores** – stable demand  
- **Promo-dependent stores** – discount-driven traffic  

Output saved as:
data/segments/store_segments.csv

### ✅ **4. Power BI Dashboard (Final Output)**  
Interactive retail pricing dashboard showing:

- Price elasticity KPIs  
- Scenario simulator (price slider / promo toggle)  
- Daily sales & revenue trend  
- Store comparison  
- ABV dynamics  
- Executive summary insights  

File:
powerbi/Model2_Dashboard.pbix

# 🧠 Technical Architecture

Python Pipeline
│
├── data/raw/ → train.csv, store.csv
├── scripts/
│ ├── demand_model.py (log elasticity model)
│ ├── scenario_simulator.py (single scenario engine)
│ ├── scenario_generator.py (grid generator)
│ └── store_clustering.py (KMeans segmentation)
│
├── data/scenarios/ → model2_scenarios.csv
├── data/segments/ → store_segments.csv
└── powerbi/ → Interactive dashboard

# 🚀 How to Run Locally

### 1. Create environment  
```bash
pip install -r requirements.txt
2. Generate elasticity model + scenario outputs
python scripts/scenario_generator.py
Result (CSV):
data/scenarios/model2_scenarios.csv
3. Generate store segments
python scripts/store_clustering.py
4. Load Power BI
powerbi/Model2_Dashboard.pbix
Replace dataset path if needed.

🖼 Power BI Dashboard – Screenshots
Full Dashboard Overview
KPI Cards
Scenario Controls (Slicers)
Sales Trend by Date
Store Comparison
Scenario Table (Debug View)

💼 Business Impact
💰 Pricing insights
Identify price points that maximize revenue
Detect stores that respond differently to price

🛒 Promo Optimization
Quantify promotion impact on sales & ABV
Avoid “over-discounting” low-value customers

🏬 Store Segmentation
High-elasticity vs inelastic store grouping
Tailored pricing by cluster

📉 Risk Analysis
Revenue downside for price increases
Footfall sensitivity evaluation

🎯 Executive-ready
This project includes a CFO summary, dashboard commentary, and actionable pricing recommendations.

🌐 Author
Ahmet Ünlü
Data Analyst | Retail Analytics | Pricing Models | Power BI | Python
📍 NRW, Germany
🔗 LinkedIn: (https://www.linkedin.com/in/ahmet-unlu-115121237/)
