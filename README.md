# ADHD Detection Using Machine Learning (Flask Web App)

## 📌 Project Overview
This project demonstrates an end-to-end machine learning workflow to detect ADHD tendencies using behavioural data.  
It covers data preprocessing, model training, evaluation, and deployment using a Flask web application.

## 🚀 Features
- Tested and compared multiple ML models:
  - Decision Tree
  - Random Forest
  - Support Vector Machine (SVM)
- Achieved **90% accuracy** using an optimised SVM model
- Built a basic **Flask web app** for user input and prediction
- Includes preprocessing, model training notebook, and saved model file

## 📁 Project Structure
ADHD-Detection/
│── ADHD.csv # Dataset
│── adhd.ipynb # Notebook with analysis + model training
│── deploy.py # Flask application
│── finalized_model.sav # Saved trained SVM model
│── README.md # Project documentation

markdown
Copy code

## ⚙️ Tech Stack
- Python (Pandas, NumPy, Scikit-learn)
- Flask
- Jupyter Notebook
- Machine Learning Classification Models (SVM, RF, DT)

## 🧠 Model Summary
The SVM classifier performed best after model comparison and tuning.  
The final model was saved using Pickle and loaded inside the Flask backend for real-time prediction.

## ▶️ How to Run the App
1. Install dependencies:
pip install -r requirements.txt

markdown
Copy code
2. Run the Flask app:
python deploy.py

markdown
Copy code
3. Visit the app in your browser:
http://127.0.0.1:5000/

markdown
Copy code

## 📈 Future Improvements
- Improve the frontend UI (HTML/CSS)
- Add more behavioural input features
- Deploy on Render/Heroku/Azure for live use
- Add a proper dataset description and feature explanation

## 👩‍💻 Author
**Simeen Sohel**  
GitHub: https://github.com/Simeen-Sohel