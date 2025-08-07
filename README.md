# 🧮 Voice-Enabled Basic Calculator in Python

This is a **basic calculator** built in Python that takes two numbers and an arithmetic operation as input, performs the operation, and reads out "Operation complete" using a text-to-speech engine.

## 🚀 Features

- Supports four operations: **Addition**, **Subtraction**, **Multiplication**, and **Division**
- Uses **`input()`** to take user input from the console
- Integrates **`pyttsx3`** text-to-speech library to give voice feedback
- Simple and beginner-friendly Python code

## 🛠️ Technologies Used

- **Python 3**
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) for offline text-to-speech

## 📦 Installation

1. Make sure you have Python installed.
2. Install the `pyttsx3` package:

```bash
pip install pyttsx3
Clone or download this repository.
'''

Run the calculator script:

'''bash

python calculator.py

'''

💡 Sample Output


Enter first number:  5
Enter 2nd number:    2
Select operation(+,-,*,/): +
7
(You will also hear "Operation complete" via your speakers.)



#🔊 Why pyttsx3?
pyttsx3 works offline, unlike many text-to-speech tools that require internet access. It's lightweight and cross-platform.

📌 Future Improvements      
Add error handling for invalid inputs

GUI version using Tkinter or PyQt

Support more operations (exponents, modulo, etc.)

🧑‍💻 Author
Made with 💙 by a Python beginner exploring voice technology.



