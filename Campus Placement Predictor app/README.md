# 🎓 Campus Placement Predictor

A Machine Learning web application that predicts whether a student is likely to be placed based on academic performance and skill-related parameters.

Built with **Python**, **Scikit-learn**, **Streamlit**, **Docker**, and deployed on **Render**.

---

## 🚀 Live Demo

🔗 https://campus-placement-predictor-aog2.onrender.com

---

## 📌 Features

- 🎯 Predicts placement chances instantly
- 📊 Random Forest Machine Learning Model
- 🎓 Uses student academic & skill data
- 🖥️ Interactive Streamlit Interface
- 🐳 Dockerized Application
- ☁️ Deployed on Render
- ⚡ Fast and User-Friendly

---

## 📂 Dataset

The model is trained using a student placement dataset containing the following features:

| Feature | Description |
|----------|-------------|
| CGPA | Student's CGPA |
| Communication Skills | Communication score |
| Resume Score | Resume quality |
| Coding Score | Coding proficiency |
| Attendance | Attendance Percentage |
| Placed | Target Variable (0/1) |

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Docker
- Git & GitHub
- Render

---

## 📁 Project Structure

```
Campus-Placement-Predictor/
│
├── app.py
├── train_model.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── data/
│   └── student_placement_data.csv
│
├── model/
│   └── placement_model.pkl
│
├── assets/
├── pages/
└── utils/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/dvshriram-dvs/Campus-Placement-Predictor.git
```

Move into the project directory

```bash
cd Campus-Placement-Predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🐳 Run with Docker

Build Docker Image

```bash
docker build -t placement-predictor .
```

Run Docker Container

```bash
docker run -p 8501:8501 placement-predictor
```

Open

```
http://localhost:8501
```

---

## 📈 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Workflow:

- Data Collection
- Data Preprocessing
- Feature Selection
- Model Training
- Model Evaluation
- Prediction
- Deployment

---

## ☁️ Deployment

The application is deployed on **Render** using Docker.

---

## 👨‍💻 Author

**D V Shriram**
Student at VIT Bhopal University
GitHub: https://github.com/dvshriram-dvs
Live Deployment URL: https://campus-placement-predictor-aog2.onrender.com

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikitlearn)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![Render](https://img.shields.io/badge/Hosted%20on-Render-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-MIT-green)
