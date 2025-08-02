
# 🚦 Traffic Volume Predictor

Predict traffic flow using Machine Learning and real-world urban data.

![GitHub repo size](https://img.shields.io/github/repo-size/Harsh-Pratap/traffic-predictor?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/Harsh-Pratap/traffic-predictor?style=flat-square)
![GitHub license](https://img.shields.io/github/license/Harsh-Pratap/traffic-predictor?style=flat-square)

---

## 📌 Project Overview

**Traffic Volume Predictor** is a machine learning-powered web application that forecasts traffic congestion levels in urban areas. By leveraging historical traffic data, weather conditions, and time-based features, this project offers real-time traffic volume predictions that can help commuters, urban developers, and smart city planners make data-driven decisions.

> 🌆 Built with real-world datasets, machine learning models, and a user-friendly web interface.

---

## 🔍 Features

- ✅ Predicts traffic volume using environmental and temporal features
- ✅ Clean, responsive frontend for easy user input
- ✅ ML backend using trained regression models
- ✅ Built on real-world traffic, weather, and holiday datasets
- ✅ Modular codebase for easy extension and retraining

---

## 📊 Tech Stack

| Layer       | Tools / Frameworks                          |
|-------------|---------------------------------------------|
| **Frontend**| HTML, CSS, JavaScript                       |
| **Backend** | Python, Flask / FastAPI                     |
| **ML Model**| Scikit-learn, XGBoost                       |
| **Data**    | Traffic + Weather + US Federal Holidays     |
| **Hosting** | GitHub Pages (Frontend), Railway (Backend)  |

---

## 📁 Project Structure

```
traffic-volume-predictor/
├── model/ # Trained ML model files (.pkl)
├── node_modules/ # Node dependencies
├── public/ # Static frontend files
│ └── images/ # UI Images
├── predict.py # Python script for predictions
├── server.js # Node.js backend server
├── package.json # Node project config
├── package-lock.json # Lockfile
├── requirements.txt # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Harsh-Pratap/traffic-predictor.git
cd traffic-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Backend Server

```bash
cd backend
python app.py
```

### 4. Open the Frontend

Open the `frontend/index.html` file in your browser  
_or_ deploy it to GitHub Pages / Netlify for public access.

---

## 🧠 Machine Learning Model

- Model trained on real-world traffic datasets (e.g., PeMS, US DOT)
- Feature Engineering includes:
  - Hour of day, day of week, month, and US holidays
  - Weather features: temperature, rain, snow, cloud cover
- Algorithms used: Random Forest, XGBoost, Linear Regression
- Performance evaluated with:
  - MAE, RMSE, R² Score

---



## 💡 Use Cases

- Smart city traffic control systems
- Route planning and congestion avoidance
- Urban infrastructure analysis
- Event and holiday traffic forecasting

---

## 📚 References

- [PeMS California Traffic Data](https://pems.dot.ca.gov/)
- [NOAA Weather Dataset](https://www.ncdc.noaa.gov/)
- [US Holiday Data](https://www.timeanddate.com/holidays/us/)

---

## 🧑‍💻 Author

**Harsh Pratap**  
📫 harshpratap8396@gmmail.com.com  
🔗 [LinkedIn](https://linkedin.com/in/pratapharsh) 

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## ⭐ Acknowledgements

- Special thanks to my team for the support and contribution
- Inspired by real-world traffic challenges and smart city solutions
