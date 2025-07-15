# 💸 Loan Eligibility Predictor

A Machine Learning-based project to predict loan eligibility using user demographic and financial data.  
This project uses **RandomForestClassifier** and is deployed via **Streamlit** to provide a simple, user-friendly interface.  
Supports both **English and Spanish** languages.

---

## 🚀 Demo
### 🎯 [How it Works]
1️⃣ User provides details like Gender, Income, Dependents, etc.  
2️⃣ Model processes inputs (scaled & encoded).  
3️⃣ Prediction shows whether **Loan is Approved or Rejected**.  
4️⃣ Output supports **English / Spanish**.



## 📂 Project Structure
│
├── loan_data_1000.csv # Sample Dataset (1000 Rows)
├── loan_model.pkl # Trained ML Model (RandomForest)
├── scaler.pkl # Preprocessing Scaler (StandardScaler)
├── app.py # Streamlit App for Deployment
└── requirements.txt # Python Dependencies


---

## 🛠️ Tech Stack / Libraries
| Tool        | Purpose                |
|-------------|------------------------|
| **Python**  | Programming Language    |
| **Pandas**  | Data Handling / Analysis |
| **Scikit-learn** | Machine Learning Model |
| **Joblib**  | Model Saving & Loading  |
| **Streamlit** | Web App UI             |
| **Numpy**   | Numerical Processing    |

---

## 📊 Dataset Columns (loan_data_1000.csv)
| Feature           | Description               |
|-------------------|----------------------------|
| Gender            | Male / Female               |
| Married           | Yes / No                    |
| Dependents        | 0 / 1 / 2 / 3+              |
| Education         | Graduate / Not Graduate     |
| Self_Employed     | Yes / No                    |
| ApplicantIncome   | Numeric                     |
| CoapplicantIncome | Numeric                     |
| LoanAmount        | Numeric (in thousands ₹)     |
| Loan_Amount_Term  | Loan term in months (360/180...) |
| Credit_History    | 1.0 = Good, 0.0 = Bad       |
| Property_Area     | Urban / Rural / Semiurban    |
| Loan_Status       | Y (Approved) / N (Rejected) |

---

## 📥 Installation & Running Locally

### 🔹 1️⃣ Clone This Repository:
```bash
git clone https://github.com/your-username/Loan_Eligibility_Predictor_Project.git
cd Loan_Eligibility_Predictor_Project

## 📊 Dataset
| Feature           | Description               |
|-------------------|----------------------------|
| Gender            | Male / Female               |
| Married           | Yes / No                    |
| Dependents        | 0 / 1 / 2 / 3+              |
| Education         | Graduate / Not Graduate     |
| Self_Employed     | Yes / No                    |
| ApplicantIncome   | Numeric                     |
| CoapplicantIncome | Numeric                     |
| LoanAmount        | Numeric (in thousands ₹)     |
| Loan_Amount_Term  | Loan term in months (360/180...) |
| Credit_History    | 1.0 = Good, 0.0 = Bad       |
| Property_Area     | Urban / Rural / Semiurban    |
| Loan_Status       | Y (Approved) / N (Rejected) |

## 📥 Installation & Running Locally

### 🔹 1️⃣ Clone This Repository:
```bash
git clone https://github.com/your-username/Loan_Eligibility_Predictor_Project.git
cd Loan_Eligibility_Predictor_Project

pip install -r requirements.txt
