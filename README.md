# 🌟 Student Stress Analytics AI

<div align="center">

### Predictive Intelligence Dashboard Powered by Machine Learning

A production-ready **Flask + Support Vector Classification (SVC)** web application designed to analyze student behavioral patterns and predict academic performance using real-time machine learning inference.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-Frontend-38B2AC.svg)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7.svg)

🚀 **Live Demo:** [Student Stress Predictor](https://student-lifestyle-and-stress-prediction.onrender.com)

</div>

---

## 📖 Overview

**Student Stress Analytics AI** is an intelligent predictive analytics platform that leverages a trained **Support Vector Classification (SVC)** model to evaluate student academic and behavioral factors. The application delivers instant predictions through a modern glassmorphic interface while maintaining production-grade deployment standards.

The system combines machine learning, responsive web technologies, and cloud deployment practices to create a real-world analytics solution suitable for educational institutions, research projects, and portfolio demonstrations.

---

## ✨ Key Features

### 🎨 Modern Glassmorphic Interface
- Elegant blurred-glass design elements
- Dynamic gradient backgrounds
- Smooth animations and transitions
- Professional dashboard experience

### 📱 Fully Responsive Design
- Optimized for desktop, tablet, and mobile devices
- Two-column adaptive layout
- Enhanced usability across screen sizes

### ⚡ Real-Time Predictions
- Instant model inference
- Dynamic result visualization
- Interactive user experience

### 🧠 Machine Learning Powered
- Support Vector Classification (SVC)
- Radial Basis Function (RBF) Kernel
- Multi-dimensional feature analysis
- Production-ready prediction pipeline

### 🎯 Demo Dataset Integration
- One-click sample data population
- Benchmark profile testing
- Easy model behavior demonstration

### ☁️ Cloud Deployment Ready
- Render-compatible configuration
- Gunicorn production server
- Lightweight deployment architecture

---

## 🏗️ System Architecture

```text
User Input
     │
     ▼
Flask Web Application
     │
     ▼
Data Validation & Processing
     │
     ▼
Support Vector Classifier (SVC)
     │
     ▼
Prediction Engine
     │
     ▼
Results Dashboard
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| **Backend** | Python, Flask |
| **Machine Learning** | Scikit-Learn, SVC (RBF Kernel) |
| **Data Processing** | NumPy, Pandas |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Styling** | Tailwind CSS |
| **Deployment** | Gunicorn, Render |
| **Model Storage** | Pickle (.pkl) |

---

## 📂 Project Structure

```text
Student-Performance-Analytics-AI/
│
├── app.py
├── requirements.txt
├── SVC_Model.pkl
│
└── README.md
```

### File Description

| File | Purpose |
|--------|---------|
| `app.py` | Flask backend application and user interface |
| `requirements.txt` | Python dependency manifest |
| `SVC_Model.pkl` | Trained Support Vector Classification model |
| `README.md` | Project documentation |

---

## 🔬 Model Benchmark Profiles

The application includes pre-validated benchmark profiles to demonstrate prediction behavior.

### Profile Comparison Matrix

| Feature Parameter | Profile A | Profile B |
|------------------|------------|------------|
| Enrollment Tracking Classification | Profile 1 | Profile 0 |
| Daily Sleep Hours | 7.0 | 6.0 |
| Daily Study Hours | 4.0 | 3.0 |
| Social Engagement Hours | 2.5 | 2.0 |
| Attendance Ratio (%) | 95% | 80% |
| Exam Pressure Exposure | 3 / 10 | 9 / 10 |
| Family Support Ecosystem | 4 / 10 | 7 / 10 |
| Academic Term Cycle Month | Month 5 | Month 2 |
| Expected Output | 0 | 1 |

---

## 📊 Input Features

The prediction model evaluates the following parameters:

| Feature | Description |
|----------|-------------|
| Enrollment Classification | Student enrollment category |
| Daily Sleep Hours | Average sleeping duration |
| Daily Study Hours | Average academic study time |
| Social Engagement Hours | Daily social interaction duration |
| Attendance Ratio | Attendance percentage |
| Exam Pressure Exposure | Academic stress level |
| Family Support Ecosystem | Family support score |
| Academic Term Cycle Month | Current academic cycle period |

---

## 🚀 Local Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/student-performance-analytics-ai.git

cd student-performance-analytics-ai
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run Application

```bash
python app.py
```

### 6️⃣ Open Browser

```text
http://127.0.0.1:5000
```

---

## ☁️ Deployment on Render

### Step 1: Push Code to GitHub

Ensure your repository contains:

```text
app.py
requirements.txt
SVC_Model.pkl
```

### Step 2: Create Web Service

1. Login to Render
2. Click **New +**
3. Select **Web Service**
4. Connect GitHub Repository

### Step 3: Configure Deployment

| Setting | Value |
|----------|--------|
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

### Step 4: Deploy

Click **Deploy Web Service** and wait for deployment completion.

---

## 📦 Required Dependencies

```text
Flask
gunicorn
numpy
pandas
scikit-learn
joblib
```

---

## 🎯 Prediction Workflow

```text
Student Inputs
      │
      ▼
Input Validation
      │
      ▼
Feature Processing
      │
      ▼
SVC Model Prediction
      │
      ▼
Classification Output
      │
      ▼
Dashboard Visualization
```

---

## 🔮 Future Enhancements

- User Authentication System
- Prediction History Tracking
- Advanced Analytics Dashboard
- Explainable AI Integration
- Model Performance Monitoring
- PDF Report Generation
- Power BI Connectivity
- Database Integration
- Multi-Model Comparison
- Automated Model Retraining

---

## 👩‍💻 Author

### Yogita Dokh

**Data Analyst & Machine Learning Developer**

This project was developed as a real-world machine learning deployment solution demonstrating:

- Machine Learning Engineering
- Flask Application Development
- Predictive Analytics
- Cloud Deployment
- Responsive UI Design
- Production ML Workflows

---

## 📜 License

This project is intended for educational, research, portfolio, and learning purposes.

Feel free to fork, modify, and extend the application for your own machine learning deployment projects.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star on GitHub!

**Built with Python, Flask, Scikit-Learn, and Tailwind CSS**

</div>
