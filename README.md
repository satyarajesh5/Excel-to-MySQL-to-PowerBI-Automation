# 📊 Automating Data Updates from Excel to Power BI using Python, MySQL, and Task Scheduler

This project automates the entire process of updating Power BI dashboards from an Excel source by leveraging Python scripts, MySQL as a structured data warehouse, and Windows Task Scheduler.

---

## 🚀 Workflow Overview

1. ✅ Maintain a master dataset in **Excel**
2. 🐍 A **Python script** reads the Excel file, transforms it with `pandas`, and pushes it to **MySQL**
3. 🕒 **Windows Task Scheduler** automates the script execution at scheduled intervals
4. 📊 **Power BI** connects to MySQL and reflects the latest data upon refresh

---

## 🔧 Tools & Technologies

- Python (pandas, SQLAlchemy)
- MySQL
- Power BI (Power Query)
- Windows Task Scheduler
- Excel

---

## 🔄 How the Automation Works

![Flow_Chart](https://github.com/user-attachments/assets/aaee5c03-c5a5-46df-8093-857497ec84ba)

---

## 📌 Process Breakdown

![Representation](https://github.com/user-attachments/assets/5823fded-6d2d-4e98-a9e5-ea30f354f2e5)

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `ExceltoDB.py` | Python script that reads Excel and uploads to MySQL |
| `Master_Sample.xlsx` | Sample Excel file format |
| `images/` | Visuals used in documentation |
