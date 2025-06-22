# 📚 Student Academic Performance Prediction

> **Student Academic Performance Prediction** uses data science and machine learning to uncover how student habits influence academic success. This project processes real-world educational data, builds predictive models, and delivers actionable insights through an interactive Streamlit web app. It demonstrates end-to-end expertise in Python, data preprocessing, model development, visualization, and web deployment.

---

## 🎯 Objectives

- **Analyze Habits:** Identify links between study habits and academic results.
- **Visualize Insights:** Present findings with clear, interactive charts.
- **Predict Scores:** Use machine learning to forecast exam outcomes.
- **Engage Users:** Offer real-time, personalized feedback via a web interface.

---

## 📖 Dataset

- **Source:** Kaggle — *Student Habits vs Academic Performance*
- **Features:**  
          - *Numerical:* Study hours, attendance, sleep, mental health, screen time, exercise, age  
          - *Categorical:* Gender, part-time job, diet, parental education, internet, extracurriculars  
          - *Target:* Exam Score (0–100)
- **Preprocessing:** Cleaned data by removing missing values and duplicates.

---

## 🛠️ Project Structure

- **`notebook.ipynb`:**  
          Data cleaning, EDA (Seaborn/Matplotlib), model training (Scikit-learn), hyperparameter tuning, saves best model.
- **`app.py`:**  
          Streamlit web app for user input, prediction, and feedback.
- **`student_habits_performance.csv`:**  
          Dataset.
- **`best_student_performance_model.pkl`:**  
          Trained Model.

---

## 🔬 Methodology

- **Preprocessing:** Remove missing data, encode categories, train/test split (80/20).
- **EDA:** Summary stats, visualizations (histograms, heatmaps, scatter/box plots).
- **Modeling:** Train/tune multiple models, evaluate with RMSE/R², select best (Linear Regression).
- **Web App:** Real-time prediction and tailored feedback.

---

## 💾 Getting Started

1. **Prerequisites:**  
          - Python 3.8+  
          - Libraries: `pandas`, `numpy`, `seaborn`, `matplotlib`, `scikit-learn`, `joblib`, `streamlit`

2. **Setup:**  
          ```bash
          git clone https://github.com/nrjunejo/student-performance-prediction.git
          cd student-performance-prediction
          pip install -r requirements.txt
          ```
          - Download the Kaggle dataset and place `student_habits_performance.csv` in the project folder.

3. **Run Analysis:**  
          Open and run `notebook.ipynb` in Jupyter Notebook or VS Code to preprocess data, explore, and train models.

4. **Start the App:**  
          ```bash
          streamlit run app.py
          ```

## 🎉 Usage

- Run the analysis script to generate insights and train the model.
- Start the Streamlit app.
- Enter your details (study hours, attendance, etc.) using sliders/dropdowns.
- Click **"Predict Performance"** for your score and recommendations.

---

## 📈 Results

- **Key Insight:** Study hours and attendance most strongly predict exam scores.
- **Best Model:** Linear Regression delivers top accuracy.
- **App Value:** Immediate, actionable advice for students.

---

## 🌱 Future Work

- Add more lifestyle features (diet, extracurriculars).
- Integrate advanced models (e.g., XGBoost).
- Deploy app online.
- Embed dynamic visualizations in the app.

---

## 🔧 Why It Matters

This project blends data science and education to create real-world impact—solving meaningful problems, building accessible tools, and communicating insights clearly. It reflects a passion for learning, innovation, and academic excellence.

---

## 🙏 Acknowledgments

- **Dataset:** Kaggle — *Student Habits vs Academic Performance*
- **Tech:** Python, Pandas, Scikit-learn, Streamlit, Seaborn, Matplotlib
- **Purpose:** Personal skill development and technical demonstration.

---

## 📩 Contact

- **Email:** [noorullah.data@gmail.com](mailto:noorullah.data@gmail.com)
- **GitHub:** [nrjunejo](https://github.com/nrjunejo)
