# 💻 Laptop Price Predictor App

A Machine Learning web application that predicts laptop prices based on hardware specifications and configuration details.

This project was built as part of my learning journey in Machine Learning and deployment-oriented application development. The application uses a trained regression model along with a simple and interactive Streamlit frontend for real-time predictions.

---

## 🚀 Features

- Predict laptop prices based on user specifications
- Interactive Streamlit UI
- Machine Learning regression pipeline
- Real-time prediction generation
- Clean and beginner-friendly project structure

---

## 🧠 Machine Learning Workflow

The project follows a complete ML workflow:

1. Data Cleaning & Preprocessing
2. Feature Engineering
3. Exploratory Data Analysis
4. Model Training
5. Regression Pipeline Creation
6. Model Serialization using Joblib
7. Frontend Integration with Streamlit

---

## Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn

### Frontend
- Streamlit

### Model Serialization
- Joblib

---

## Project Structure

```bash
laptop-price-predictor/
│
├── app.py
├── ML
|   ├── pipe.joblib
|   ├── laptop_price_predictor.ipynb
|   └── df.joblib
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SanishCode21/Laptop-Price-Predictor-App.git

cd laptop-price-predictor
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

## Input Features

The model predicts laptop prices using features such as:

- Brand
- Laptop Type
- RAM
- Weight
- Touchscreen Support
- IPS Display
- Screen Size
- Screen Resolution
- CPU Brand
- HDD Storage
- SSD Storage
- GPU Brand
- Operating System

---

## Learning Objectives

This project helped me understand:

- End-to-end ML workflow
- Regression model pipelines
- Model deployment basics
- Frontend integration with ML models
- Real-world feature preprocessing
- User interaction handling in Streamlit

---

## Future Improvements

Planned improvements for future versions:

- Docker containerization
- Cloud deployment
- Better UI/UX
- Model performance optimization
- API integration using FastAPI
- CI/CD pipeline integration

---

## Note

This project was built primarily for learning and experimentation purposes to strengthen my understanding of Machine Learning application development and deployment workflows.

---

## 👨‍💻 Author

Sanish Kumar



If you found this project helpful or interesting, feel free to connect or provide feedback.