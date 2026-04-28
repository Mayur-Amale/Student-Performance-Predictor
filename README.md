# Student-Performance-Predictor (GradeX)

Student Performance Predictor is a full-stack machine learning application that estimates student exam scores based on study habits and academic factors. It combines a regression model with a Flask API backend and a Node.js/Express frontend server to deliver real-time predictions, data tracking, and actionable insights for improving performance.

## Project Structure

```
Student-Performance-Predictor/
├── frontend/              
│   ├── pages/             
│   ├── css/               
│   ├── js/                
│   └── assets/            
├── backend/               
│   ├── server.js          
│   ├── routes/             
│   ├── ml/                
│   └── utils/             
├── ml/                     
│   └── data/              
├── database/              
├── package.json            
├── requirements.txt       
└── README.md
```

## Getting Started

### Backend (Node.js)
```bash
npm install
npm run dev
```

## 🧠 Features

* 📊 Predict student performance based on input data
* 🖥️ User-friendly web interface
* ⚡ Real-time prediction using trained ML model
* 📈 Helps identify weak/at-risk students

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Backend:** Flask
* **Machine Learning:** Scikit-learn
* **Data Handling:** Pandas, NumPy
* **Frontend:** HTML, CSS

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/karanbhilare58/Student-Performance-Predictor.git
cd Student-Performance-Predictor
```

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Dataset Information

The dataset includes features such as:

* Gender
* Parental level of education
* Study time
* Test preparation course
* Previous scores (Math, Reading, Writing)

These features are commonly used in student performance prediction models. ([GitHub][2])

---

## 🤖 Machine Learning Model

* Model Type: Regression / Classification (depending on your implementation)
* Algorithms Used:

  * Linear Regression / Random Forest / Decision Tree (update based on your model)
* Evaluation Metrics:

  * Mean Squared Error (MSE)
  * R² Score

## 🔥 Future Improvements

* Add more advanced models (XGBoost, Neural Networks)
* Improve UI/UX design
* Deploy project online (Render / Railway)
* Add real-time analytics dashboard

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.


## 📄 License

This project is for educational purposes only.
