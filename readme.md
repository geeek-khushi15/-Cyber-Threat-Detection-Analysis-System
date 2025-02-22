A machine learning-based project to analyze network logs, visualize attack patterns, and predict cyber threats.

📌 Project Overview
This project processes network traffic logs, identifies attack categories, and trains a Random Forest model to predict cyber attacks. It includes data preprocessing, visualization, model training, and prediction.

📂 Project Structure
bash
Copy
Edit
📁 DATA ANALYTICS PROJECT/
│── 📄 cyber_logs.csv                # Raw network logs dataset  
│── 📄 preprocessed_data.csv          # Cleaned and processed dataset  
│── 📄 data_analysis.py               # Exploratory Data Analysis (EDA)  
│── 📄 visualization.py               # Plots for attack trends  
│── 📄 preprocess.py                  # Data cleaning and feature engineering  
│── 📄 train_model.py                  # ML model training (Random Forest)  
│── 📄 predict.py                      # Predict attack categories on new data  
│── 📄 test_model.py                   # Model evaluation metrics  
│── 📂 models/                         # Trained model storage  
│── 📄 README.md                       # Project documentation  
🔧 Setup & Installation
1️⃣ Install Dependencies
sh
Copy
Edit
pip install pandas numpy matplotlib seaborn scikit-learn joblib
2️⃣ Run Preprocessing
sh
Copy
Edit
python preprocess.py
3️⃣ Run Exploratory Data Analysis
sh
Copy
Edit
python data_analysis.py
4️⃣ Run Visualizations
sh
Copy
Edit
python visualization.py
5️⃣ Train the Machine Learning Model
sh
Copy
Edit
python train_model.py
6️⃣ Predict Attack Categories
sh
Copy
Edit
python predict.py
📊 Visualizations
The project includes data visualizations to understand attack trends:
✅ Attack Type Distribution
✅ Protocol vs Attack Type
✅ Top Source & Destination Ports Attacked
✅ Correlation Heatmap

🛠️ Technologies Used
Python 🐍
Pandas, NumPy for data processing
Matplotlib, Seaborn for visualization
Scikit-Learn for machine learning
Joblib for model serialization
📌 Sample Prediction Output
Src_IP	Dst_IP	Protocol	Predicted Attack
192.168.1.1	10.0.0.1	TCP	Exploit
172.16.0.2	192.168.0.5	UDP	DoS Attack
📥 Dataset
The dataset cyber_logs.csv contains network traffic logs, including features like:

Source & Destination IPs
Protocols (TCP, UDP, ICMP)
Attack Categories (DoS, Exploit, Fuzzers, etc.)

📌 Contributing
Feel free to fork this repo and submit pull requests. Any improvements or feature additions are welcome!

🔗 Connect with Me
📧 Email: khushibarole15@gmail.com
