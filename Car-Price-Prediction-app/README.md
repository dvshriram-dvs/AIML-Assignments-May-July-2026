
# 🚗 Car Value Predictor

A Machine Learning-powered web application that estimates the resale value of a used car based on vehicle specifications and ownership details. The application uses a trained Random Forest Regression model and provides instant price predictions through an interactive Flask-based web interface.

---

## 👨‍💻 Developer

* **Name:** D V Shriram
* **Registration Number:** 23MIM10044
* **Program:** Integrated M.Tech in Artificial Intelligence
* **University:** VIT Bhopal University

---

## 🔗 Project Links

* **GitHub Repository:** https://github.com/dvshriram-dvs/Car-Value-Predictor-app.git
* **Live Deployment URL:** https://car-value-predictor-app.onrender.com

---

## 🛠️ Technologies Used

### Programming Language

* Python 3

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Web Development

* Flask
* HTML5
* CSS3

### Deployment & Tools

* Git
* GitHub
* Render
* Pickle

---

## 📂 Project Structure

```text
Car-price-predictor/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train.py
├── car_price_model.pkl
├── requirements.txt
├── Procfile
└── README.md
```

---

## 📊 Project Overview

This application predicts the expected resale value of a car using historical vehicle data. Users provide information such as:

* Present Price
* Kilometers Driven
* Fuel Type
* Seller Type
* Transmission Type
* Number of Previous Owners
* Vehicle Age

The trained machine learning model processes these inputs and generates an estimated selling price instantly.

---

## 🤖 Machine Learning Model

**Algorithm Used:** Random Forest Regressor

### Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Serialization
7. Flask Integration
8. Real-Time Prediction

---

## ⚙️ Local Installation

### Clone the Repository

```bash
git clone https://github.com/dvshriram-dvs/Car-price-predictor.git
cd Car-price-predictor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📈 Features

* Real-time car price prediction
* Interactive web interface
* Machine Learning-based valuation
* Responsive design
* Fast prediction results
* Easy deployment support

---

## 🚀 Future Improvements

* User authentication
* Prediction history tracking
* Advanced visual analytics
* Multiple model comparison
* API integration
* Mobile-first dashboard

---

## 📄 License

This project is developed for educational and academic purposes.

---

## ⭐ Author

**D V Shriram**
23MIM10044
Integrated M.Tech in Artificial Intelligence
VIT Bhopal University

