# 📧 Spam Email Detection using Machine Learning

## 🚀 Project Overview

This project is a beginner-friendly **AI/ML application** that detects whether a message is **Spam** or **Not Spam (Ham)**.

It uses:

* A **Naive Bayes Machine Learning model**
* A **Linear Search algorithm** for keyword detection
* A simple **Tkinter GUI** for user interaction

The system learns from a dataset and predicts whether a message is spam based on patterns in text.

---

## 🧠 Features

* ✅ Detects spam messages using Machine Learning
* 🔍 Keyword-based detection using Linear Search
* 💻 Simple GUI using Tkinter
* ⚡ Fast and easy to use
* 📊 Uses real dataset (Kaggle SMS Spam Collection)

---

## 📂 Project Structure

```
SpamDetectionProject/
│
├── main.py          # Main Python code
├── spam.csv         # Dataset file
└── README.md        # Project documentation
```

---

## ⚙️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Tkinter

---

## 📥 Installation & Setup

Follow these steps to run the project:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/spam-detection-project.git
cd spam-detection-project
```

---

### 2️⃣ Install Required Libraries

```bash
pip install pandas scikit-learn
```

> Tkinter usually comes pre-installed with Python.

---

### 3️⃣ Add Dataset

Download the dataset from Kaggle:

* **SMS Spam Collection Dataset**

Place the file:

```
spam.csv
```

in the project folder.

---

### 4️⃣ Run the Project

```bash
python main.py
```

---

## 🖥️ How to Use

1. Run the program
2. A window will open
3. Enter a message in the input box
4. Click **"Check Spam"**
5. View the result

---

## 📊 Example

**Input:**

```
Congratulations! You have won a free prize!
```

**Output:**

```
IT'S A SPAM!! (Detected by Keyword Search)
```

---

**Input:**

```
Hey, are we meeting today?
```

**Output:**

```
NOT SPAM ✅
```

---

## 🧠 How It Works

1. The system first checks for common spam keywords using **Linear Search**
2. If no keyword is found, it uses a **Machine Learning model**
3. The model converts text into numbers using **CountVectorizer / TF-IDF**
4. The **Naive Bayes algorithm** predicts whether the message is spam

---

## 📚 Concepts Used

* Artificial Intelligence
* Machine Learning
* Supervised Learning
* Classification
* Naive Bayes Algorithm
* Feature Extraction (Bag of Words / TF-IDF)
* Linear Search Algorithm

---

## ⚠️ Limitations

* Depends on dataset quality
* May not detect advanced spam messages
* Keyword search is basic

---



## ⭐ Acknowledgements

* Kaggle for dataset
* Scikit-learn documentation
* Python community

## 📸 Project Outputs

| ❌ Spam Output | ✅ Not Spam Output |
|---------------|------------------|
| ![](https://github.com/pranjal291407/SPAM-DETECTION-TOOL-AI-ML-PROJECT/blob/main/SAMPLE%20OUTPUTS/SPAM%20OUTPUT.png) | ![](https://github.com/pranjal291407/SPAM-DETECTION-TOOL-AI-ML-PROJECT/blob/main/SAMPLE%20OUTPUTS/NOT%20SPAM%20OUTPUT.png) |

---
