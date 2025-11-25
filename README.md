# 📊 Model 2 – Demand Elasticity & Pricing Scenario Simulator  
### Python (Statsmodels) + Power BI Dashboard + Store Clustering

This repository contains a complete **pricing & demand analytics system**, combining  
**Python-based Log Elasticity Modeling** with a fully interactive **Power BI Scenario Simulator**.

It is designed for retail, FMCG, e-commerce, and any business where **price, promotion, and footfall** impact revenue.

---

# 🔧 Key Features

### ✅ 1. Log-Elasticity Demand Model (Python, Statsmodels)

- Estimates **price elasticity of demand**
- Captures effects of:
  - Price change (log-log regression)
  - Footfall
  - Promotions
  - Store fixed-effects
- Produces:
  - Baseline predictions  
  - Elasticity coefficients  
  - Daily sales forecasts  

---

### ✅ 2. Scenario Simulator (Python → Power BI)

Python generates all combinations of scenarios automatically.

**Scenario inputs**

- `PriceChange`: –30% → +30%  
- `FootfallChange`: –10% / 0 / +10%  
- `PromoOverride`: 0 / 1  

For every scenario, the model outputs:

- `Sales_Pred`  
- `Revenue_Pred`  
- `ABV_Scn` (Average Basket Value)  
- `ScenarioID`  

Output file: `data/scenarios/model2_scenarios.csv`  

Power BI reads this file to enable **real-time pricing scenarios**.

---

### ✅ 3. Store-Level Segmentation (Clustering)

KMeans identifies store groups:

- High elasticity stores  
- Inelastic stores  
- Promo-driven stores  

Output: `data/segments/store_segments.csv`

---

### ✅ 4. Power BI Dashboard (Final Output)

Includes:

- Price elasticity KPIs  
- Scenario simulator (price slider / promo toggle)  
- Revenue & sales trends  
- Store comparison  
- ABV dynamics  
- CFO-ready insights  

Power BI file: `powerbi/Model2_Dashboard.pbix`

---

# 🧠 Technical Architecture

**Python pipeline structure**

- `data/raw/`
  - `train.csv`
  - `store.csv`
- `scripts/`
  - `demand_model.py` – log elasticity model
  - `scenario_simulator.py` – single scenario engine
  - `scenario_generator.py` – full scenario grid generator
  - `store_clustering.py` – KMeans segmentation
- `data/scenarios/`
  - `model2_scenarios.csv`
- `data/segments/`
  - `store_segments.csv`
- `powerbi/`
  - `Model2_Dashboard.pbix`
  - `screenshots/`

---

# 🚀 How to Run Locally

### 1. Install dependencies

Terminal / command line:

- `pip install -r requirements.txt`

### 2. Generate elasticity model + scenarios

- `python scripts/scenario_generator.py`  

Output: `data/scenarios/model2_scenarios.csv`

### 3. Generate store segments

- `python scripts/store_clustering.py`  

Output: `data/segments/store_segments.csv`

### 4. Open Power BI dashboard

- Open `powerbi/Model2_Dashboard.pbix`
- Update dataset paths if needed.

---

# 🖼 Power BI Dashboard – Screenshots

### Full Dashboard Overview  
![Dashboard Overview]

### KPI Cards  
![KPI Cards](powerbi/screenshots/kpi_cards.png)

### Scenario Controls (Slicers)  
![Slicers]

### Sales Trend by Date  
![Trend]

### Store Comparison  
![Store Comparison]

### Scenario Table (Debug View)  
![Table]

---

# 💼 Business Impact

### 💰 Pricing Insights

- Identify price points that maximize revenue  
- Detect store-level sensitivity differences  

### 🛒 Promo Optimization

- Measure uplift of promotions  
- Prevent margin loss from over-discounting  

### 🏬 Store Segmentation

- High vs low elasticity stores  
- Cluster-based pricing strategies  

### 📉 Risk Analysis

- Revenue downside of price increases  
- Footfall dependence  

### 🎯 Executive-Ready Dashboard

Includes CFO summary and clear business recommendations.

---

# 🌐 Author

**Ahmet Ünlü**  
Data Analyst · Retail Analytics · Pricing Models · Power BI · Python  
📍 NRW, Germany  
🔗 LinkedIn: https://www.linkedin.com/in/ahmet-unlu-115121237/

---

# 📄 License

MIT License

