
# IMPORTING THE  LIBRARIES

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import tkinter as tk
from tkinter import messagebox


# LOADING THE DATASET 

try:
    data = pd.read_csv(r"C:\Users\pranj/Spam detection\spam.csv", encoding='latin-1')
except:
    print("Error: Make sure spam.csv is in the same folder!")
    exit()

# KEEPING ONLY THE USEFUL COLUMNS FROM THE DATASET
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

# Converting the spam words into numbers as the model can't understand the text
data['label'] = data['label'].map({'ham': 0, 'spam': 1})


# Split the data from dataset

X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label'], test_size=0.2, random_state=42
)


# MODEL PIPELINE

model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])


# TRAINING THE  MODEL

model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy*100:.2f}%")


# PREDICTION FUNCTION: SPAM OR NOT

def predict_spam(message):
    if message.strip() == "":
        return "Please enter a message"
    
    result = model.predict([message])[0]
    return "IT'S A SPAM!! " if result == 1 else "NOT SPAM "


# TKINTER GUI

def check_message():
    msg = entry.get()
    result = predict_spam(msg)
    output_label.config(text="Result: " + result)

def clear_text():
    entry.delete(0, tk.END)
    output_label.config(text="")

# Create window
root = tk.Tk()
root.title("Spam Email Detector")
root.geometry("500x350")

# Title
title_label = tk.Label(root, text="Spam Detection System", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input box
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Buttons
check_btn = tk.Button(root, text="Check Spam", command=check_message, bg="blue", fg="white")
check_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear", command=clear_text)
clear_btn.pack(pady=5)

# Output
output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack(pady=20)

# Run app
root.mainloop()