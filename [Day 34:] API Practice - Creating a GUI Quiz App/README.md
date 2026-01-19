# Day 34: API Practice - Creating a GUI Quiz App

## Project: Trivia Quiz GUI App

### Description
A graphical trivia quiz application that fetches questions from the Open Trivia Database API. Features a clean GUI with true/false questions, score tracking, and visual feedback for correct/incorrect answers. Demonstrates combining APIs with Tkinter GUI.

### What I Learned
- Fetching data from APIs
- Parsing API responses
- HTML entity decoding (`html.unescape()`)
- Type hinting in Python
- Combining API data with GUI
- OOP design with multiple classes
- Visual feedback in Tkinter

### How to Run
```bash
python3 main.py
```

### Features
- Questions from Open Trivia API
- True/False quiz format
- Score tracking
- Visual feedback (green/red)
- 10 questions per game
- Clean, modern UI
- API parameter customization

### Open Trivia Database API

#### API Endpoint
```
https://opentdb.com/api.php
```

#### Parameters
```python
parameters = {
    "amount": 10,
    "type": "boolean",  # True/False questions
    "category": 18,     # Computer Science
}

response = requests.get("https://opentdb.com/api.php",
                       params=parameters)
data = response.json()
questions = data["results"]
```

### API Response Format
```json
{
    "results": [
        {
            "category": "Science: Computers",
            "type": "boolean",
            "difficulty": "easy",
            "question": "HTML stands for Hypertext Markup Language.",
            "correct_answer": "True",
            "incorrect_answers": ["False"]
        }
    ]
}
```

### HTML Entity Decoding
```python
import html

question_text = "What&#039;s the capital of France?"
clean_text = html.unescape(question_text)
# "What's the capital of France?"
```

### Type Hinting
```python
def check_answer(self, user_answer: str) -> bool:
    correct_answer = self.current_question.answer
    if user_answer.lower() == correct_answer.lower():
        self.score += 1
        return True
    else:
        return False
```

### Project Structure

```
Day34_Quiz/
├── main.py
├── question_model.py
├── data.py
├── quiz_brain.py
├── ui.py
└── images/
    ├── true.png
    └── false.png
```

### Classes

#### Question Model
```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

#### Data Fetching
```python
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php",
                       params=parameters)
data = response.json()
question_data = data["results"]
```

#### Quiz Brain (Logic)
```python
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
```

#### UI Class
```python
from tkinter import *

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        # Score label
        self.score_label = Label(text="Score: 0")

        # Question canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Question",
            font=("Arial", 20, "italic")
        )

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img,
                                  command=self.true_pressed)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img,
                                   command=self.false_pressed)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
```

### Visual Feedback
- Green background: Correct answer
- Red background: Wrong answer
- Feedback shows for 1 second then loads next question

### Key Concepts
- **API Integration**: Fetching real-time quiz questions
- **HTML Entities**: Decoding special characters
- **Type Hints**: Documenting expected types
- **MVC Pattern**: Separating model, logic, and UI
- **Canvas Background**: Visual feedback
- **Button Commands**: Connecting UI to logic

### Learning Focus
Building a complete application that combines external API data with a polished GUI interface, demonstrating real-world app development practices.
