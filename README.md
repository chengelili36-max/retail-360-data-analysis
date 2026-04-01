# retail-360-data-analysis
End-to-end retail data analysis with Python &amp; Tableau
# 📊 Retail 360: Customer Insight & Inventory Risk Control

🔗 **[👉 Click Here to View the Interactive Dashboard on Tableau Public](https://public.tableau.com/views/TheRetailPulseRetailBusinessHealthMonitor/Dashboard1?:language=en-US&:sid=&:redirect=auth&publish=yes&showOnboarding=true&:display_count=n&:origin=viz_share_link)**

![Dashboard Screenshot]<img width="1535" height="877" alt="Screenshot 2026-04-01 at 4 54 56 PM" src="https://github.com/user-attachments/assets/de44e33e-82e8-4fc4-96ba-5c5d910a3df6" />

## 📝 Project Overview 
In the highly competitive retail industry, understanding customer value and preventing inventory stockouts are critical for sustainable growth. This project analyzes a retail dataset to identify high-value customer segments using the RFM model and establishes a dynamic safety stock alert system to bridge the gap between frontend sales and backend supply chain management.

## 🛠️ Tech Stack 
* **Data Processing & ETL:** Python (Pandas, Numpy)
* **Data Visualization & BI:** Tableau
* **Core Models:** RFM Analysis (Recency, Frequency, Monetary)

## 💡 Key Business Insights 

1. **Customer Segmentation **
   * **Insight:** The "Potential Customers" segment makes up the largest proportion of the user base, rather than "Core Customers."
   * **Action:** Shift marketing budget priority to nurture this potential segment via targeted loyalty programs to drive conversion into core, high-LTV (Life Time Value) users.
2. **Supply Chain Risk Control **
   * **Insight:** Developed a dynamic Bullet Graph with calculated safety thresholds. Identified that the `Beauty` category consumption has breached the safety stock line (800 units).
   * **Action:** Trigger immediate restocking protocols for the Beauty category to prevent out-of-stock events and subsequent revenue loss.
3. **Performance Monitoring **
   * **Insight:** Implemented a Dual-Axis trend chart to monitor Monthly Revenue alongside MoM (Month-over-Month) growth rate, providing management with a clear pulse of business performance.

## 📂 Repository Structure
* `data_preprocessing.ipynb`: Python script for data cleaning, aggregation, and RFM score calculation.
* `Retail_Dashboard.twbx`: Packaged Tableau workbook containing the interactive dashboard.
* `requirements.txt`: Python environment dependencies.

---
*Created by [Chenge Li] | Data Analyst*
