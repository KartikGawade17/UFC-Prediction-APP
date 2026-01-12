# 🥊 UFC Fight Prediction App

🔗 **Live App:**  
https://ufc-prediction-app-62-kartik.streamlit.app/

🔗 **Live Power BI Dashboard**
https://app.powerbi.com/view?r=eyJrIjoiNjAzYmNkOTktYzllYy00NjU3LWI3M2EtMTgyZTBiNGIzZTYwIiwidCI6IjcxMWYwNjQxLTc5ODUtNDRlNS1iMjQwLWQyZTk5MjZhNTVjMyJ9

NOTE: You can also see power bi dashboard inside the app too.
---

## 📌 Project Overview

The **UFC Fight Prediction App** is an end-to-end data analytics and machine learning project designed to analyze historical UFC fight data and predict the probable winner between two fighters.

This project combines **data engineering, machine learning, and interactive visualization** into a single production-ready application.

---

## ⚙️ Tech Stack Used

- **Python**
- **BeautifulSoup** – for web scraping UFC fight data
- **Azure SQL Database** – centralized cloud database
- **Pandas & NumPy** – data cleaning and feature engineering
- **Scikit-learn / XGBoost** – machine learning model
- **Power BI** – analytical dashboard
- **Streamlit** – ML app deployment
- **GitHub** – version control and deployment

---

## 🗄️ Data Collection

- UFC fight data is **scraped manually using BeautifulSoup**
- Data includes:
  - Fighter names
  - Knockdowns, strikes, takedowns, submissions
  - Weight class, method, round, time
  - Fight outcomes
- Cleaned in **Local MySQL Database** and later stored in **Azure SQL Database**

---

## 🧠 Machine Learning Model

- Model trained using historical UFC fight statistics
- Feature engineering includes:
  - Average performance from recent fights
  - Reach and height advantages
  - Strikes per minute
  - Weight class and stance encoding
- Output:
  - Win probability for both fighters
  - Predicted winner with confidence score

---

## 📊 Power BI Dashboard

- Interactive analytical dashboard built in **Power BI**
- Insights include:
  - Fight outcomes by weight class
  - Fighter performance trends
  - Win/loss distributions
- Dashboard is embedded inside the Streamlit app

---

## 🌐 Streamlit Application Features

- Select two fighters and a weight class
- Predict fight outcome in real time
- Displays:
  - Win probability
  - Predicted winner
  - Model confidence
- Embedded Power BI dashboard for deeper analysis

---

## 🎯 Project Goals

- Apply **real-world data analytics** to combat sports
- Build a **cloud-based ML pipeline**
- Demonstrate end-to-end skills:
  - Data extraction
  - Database management
  - ML modeling
  - Dashboarding
  - Deployment

---

## 🚀 Future Enhancements

- Add live fight updates
- Improve model accuracy with advanced features
- Include fighter rankings and historical form
- Automate data ingestion pipeline

---

## 👤 Author

**Kartik Gawade**  
Data Analytics & Machine Learning Enthusiast  

---

⭐ *If you like this project, feel free to star the repository!*
