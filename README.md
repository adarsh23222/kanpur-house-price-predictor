# 🏠 Kanpur House Price Predictor

A Machine Learning web app to predict residential property prices in Kanpur, UP.

## 🔗 Live Demo
👉 [Click Here to Try the App](https://kanpur-house-price-predictor.onrender.com)

## 📊 Model Performance
| Model | R² Score | MAE |
|---|---|---|
| Linear Regression | 0.9458 | 6.80L |
| Random Forest | 0.9445 | 4.92L |
| XGBoost | 0.9129 | 5.72L |
| **Tuned RF (Final)** | **0.9496** | **5.07L** |

## 🛠️ Tech Stack
- **Scraping:** Playwright, BeautifulSoup
- **ML:** Scikit-learn, XGBoost, Pandas, NumPy
- **Web App:** Streamlit
- **Deployment:** Render.com

## 📁 Project Structure
kanpur-house-price-predictor/
├── app.py                  # Streamlit web app
├── kanpur_house_model.pkl  # Trained ML model
├── localities.json         # Kanpur localities list
├── locality_mean.json      # Locality price encoding
├── feature_cols.json       # Feature columns
├── requirements.txt        # Dependencies
└── runtime.txt             # Python version

## 🚀 How to Run Locally
pip install -r requirements.txt
streamlit run app.py

## 👨‍💻 About
Built as an end-to-end ML project — from web scraping to deployment.

