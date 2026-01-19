# Day 17: The Quiz Project & The Benefits of OOP

## Project: Quiz Game

### Description
An interactive quiz game built using Object-Oriented Programming principles. The quiz pulls questions from a question bank, tracks the score, and provides feedback. This project demonstrates creating your own classes and working with object instances.

### What I Learned
- Creating custom classes from scratch
- Class design and architecture
- Working with multiple objects
- Class initialization with `__init__`
- Instance attributes
- Method implementation
- Iterating through object collections
- OOP benefits in real applications

### How to Run
```bash
cd "Day17Project_Quiz"
python3 [main_file].py
```

### Features
- Multiple choice questions
- Score tracking
- Question progression
- Immediate feedback
- Final score display
- Extensible question bank

### Classes Implemented

#### 1. Question Class
```python
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
```

#### 2. QuizBrain Class
```python
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        # Present next question

    def check_answer(self, user_answer, correct_answer):
        # Verify and update score

    def still_has_questions(self):
        # Check if quiz continues
```

### How It Works
1. Question objects are created from question data
2. QuizBrain manages the quiz flow
3. Questions are presented one at a time
4. User provides answers
5. Immediate feedback on correctness
6. Score tracked throughout
7. Final results displayed

### Key Concepts
- **Class Design**: Planning class structure before coding
- **Instance Attributes**: Each object has its own data
- **Methods**: Defining behavior for objects
- **Object Initialization**: Setting up objects with `__init__`
- **Separation of Concerns**: Each class has one responsibility

### Files
- `day17.py`: Practice exercises
- Project folder with quiz implementation
- Question data file
- Question and QuizBrain class files

### Example Gameplay
```
Q.1: Python is a programming language. (True/False): True
You got it right!
The correct answer was: True.
Your current score is: 1/1

Q.2: Java and JavaScript are the same. (True/False): False
You got it right!
The correct answer was: False.
Your current score is: 2/2

You've completed the quiz!
Your final score was: 2/2
```

### Learning Focus
Designing and implementing your own classes to solve real problems, demonstrating OOP's power in organizing complex logic.
