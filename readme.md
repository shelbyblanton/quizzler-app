# Quizzler Application

## **[100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/)**

By Dr. Angela Yu

*Day 34 of 100:* API Practice: Creating a GUI Quiz App

## Project Specs

Using TkInter and Canvas to create a user interface (UI), then utilize the [Open Trivia Database API](https://opentdb.com/) to develop a quiz application that presents a series of statements to the user whom then has to guess whether the statement is **true** or **false**.

This application is written with Python 3.11.

<img src="https://github-readme.s3.us-west-1.amazonaws.com/Quizzler-start.png" alt="Quizzler App" width="300"/>

### Main Features
The application displays a trivia statement and the user has to guess if it is **true** by click on the green `√` button, or **false** by clicking on the red `x` button.

If the user guesses correctly, the screen will flash green for 1 second, add a point to the user's score, and then advance to the next question.

<img src="https://github-readme.s3.us-west-1.amazonaws.com/Quizzler-correct.png" alt="Quizzler App Correct Guess Response" width="200"/>

If the user guesses incorrectly, the screen will flash red for 1 second and then advance to the next question.

<img src="https://github-readme.s3.us-west-1.amazonaws.com/Quizzler-incorrect.png" alt="Quizzler App Incorrect Guess Response" width="200"/>

Once the app has advanced through all questions in the question bank, it displays "You have reached the end" to the user and disables both buttons.

<img src="https://github-readme.s3.us-west-1.amazonaws.com/Quizzler-end.png" alt="Quizzler App End of Game" width="200"/>

## Usage & Requirements

This project uses three libraries/packages:
- TkInter
- requests
- html

And uses 3 classes:
- Interface
- QuizBrain
- Question

And one data file:
- data.py

### Workflow
We first make a call to the Open Trivia Database API to retrieve the trivia questions by importing the `data.py` file into `main.py`:

```
from data import question_data
```

The `data.py` file call makes a `requests.get()` call to the API, converts the result to JSON, and then returns the data that we need to start the game:
```
def get_trivia_bank():
    response = requests.get(url="https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    data = response.json()
    return data['results']


question_data = get_trivia_bank()
```

Next we sort through the question bank and pull only the data we need (the question text and the correct answer), storing it in a list:

```angular2html
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
```

Lastly we send the filtered question data to the `QuizBrain` and start the `Interface` to begin the game:

```
quiz = QuizBrain(question_bank)
quiz_ui = Interface(quiz)
```

# Getting Started

All of the commands below should be typed into the Python terminal of your IDE (I use PyCharm for my Python Development).

First, clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:shelbyblanton/quizzler_app.git
    
Then open the project in PyCharm.
    
In the `question_model.py` file, click on the word `requests` in the import statement at the top of the page. Then click on the red exclamation point and click `Install package requests` to load the library:

![Install the requests library in the question_model file](https://github-readme.s3.us-west-1.amazonaws.com/package-install-requests.png)

**Setup is complete!** 

Click Run in PyCharm to see the app in action.


# Author & Credits

Programmed by **[M. Shelby Blanton](https://www.linkedin.com/in/shelbyblanton/)** under the instructional guidance of **[Dr. Angela Yu](https://www.udemy.com/user/4b4368a3-b5c8-4529-aa65-2056ec31f37e/)** via **[Udemy.com](udemy.com)**.
