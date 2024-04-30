# Email Web App

A basic web application for sending and receiving emails.

## Table of Contents

- [Installation](#Installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)
- [Contact](#contact)
- [Project_Checklist](#Project_Checklist)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AmerYassir/Simple-Email-Web-App/.git
    ```

2. Install dependencies:

    ```bash
    pip install flask
    pip install sqlit3
    pip install scikit-learn>=1.3.2
    pip install nltk>=3.8.1
    pip install pandas>=1.5.1
    pip install numpy>=1.23.4
    pip install joblib>=1.4.0
    pip install xgboost>=2.0.3
    pip install spam-detector-ai>=2.1.13
    ```
## Configuration
1. Start the server:

    ```bash
    flask --app main.py run
    ```
    in case you want to work in debug mode
    ```bash
    flask --app main.py --debug run
    ```

2. Open your web browser and go to `http://localhost:5000 or http://127.0.0.1:5000/` to access the application.

## Usage

1. Sign up for an account or log in if you already have one.
2. Compose a new email by clicking on the "Write Email" button.
3. Enter the recipient's email address, subject, and message content.
4. Click the "Send" button to send the email.
5. Check your inbox for received emails or move it to (trash/spam).
6. Check Sent to see your sent emails or delete it permanently for you and reciveir.
7. Check Trash to view and retrieve deleted emails.
8. Check Spam to see your spam emails or retrive it to your inbox.
9. Click on an emails to view its contents.


## Contributing

Contributions are always welcome! Even though I'm the only contributor at the moment, your feedback, suggestions, and bug reports are highly appreciated.

If you'd like to contribute to this project, feel free to:

- Open an issue to report bugs, request features, or discuss ideas.
- Submit pull requests for bug fixes or enhancements.
- Provide feedback on existing features or documentation.

Thank you for considering contributing to this project!


## Credits

### Contributors

- [Amer Yasser](https://github.com/AmerYassir/): Contributed code for all the project.

### Special Thanks

- [Remote.Coders](https://remotecoders.org/): Provided funding or resources to support the development of this project.

### Libraries Used

- [Flask](https://flask.palletsprojects.com/): Used for building the web application.
- [SQLite](https://www.sqlite.org/): Used for local database storage.
- [scikit-learn](https://scikit-learn.org/): Used for machine learning algorithms.
- [NLTK](https://www.nltk.org/): Used for natural language processing tasks.
- [pandas](https://pandas.pydata.org/): Used for data manipulation and analysis.
- [NumPy](https://numpy.org/): Used for numerical computing.
- [joblib](https://joblib.readthedocs.io/): Used for parallel computing in scikit-learn.
- [XGBoost](https://xgboost.readthedocs.io/): Used for gradient boosting algorithms.
- [spam-detector-ai](https://github.com/adamspd/spam-detection-project/tree/main): Used in spam detecting.

## Contacts
Amer.yassir.abdaljalil@gmail.com

https://github.com/AmerYassir/

https://www.linkedin.com/in/amer-yasser-964250217/



## Project_Checklist
- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard
Library other than the random module.
 Please provide the name of the module you are using in your
app.
 - Module name:'re'
- [x] It contains at least one class written by you that has
both properties and methods. It uses `__init__()` to let the
class initialize the object's attributes (note that
`__init__()` doesn't count as a method). This includes
instantiating the class and using the methods in your app.
Please provide below the file name and the line number(s) of
at least one example of a class definition in your code as
well as the names of two properties and two methods.
 - File name for the class definition:'data_writer'
 - Line number(s) for the class definition: (13:76)
 - Name of two properties:'db_name','msg_count'
 - Name of two methods:'write_user','write_message'
 - File name and line numbers where the methods are used:'main.py' (92,201) respectively
- [x] It makes use of JavaScript in the front end and uses the
localStorage of the web browser.
- [x] It uses modern JavaScript (for example, let and const
rather than var).
- [x] It makes use of the reading and writing to the same file
feature.
- [x] It contains conditional statements. Please provide below
the file name and the line number(s) of at least one example of a conditional statement in your code.
 - File name: main.py
 - Line number(s):38,49,70,88
- [x] It contains loops. Please provide below the file name
and the line number(s) of at least
 one example of a loop in your code.
 - File name:'main.py'
 - Line number(s):46
- [x] It lets the user enter a value in a text box at some
point.
 This value is received and processed by your back end
Python code.
- [x] It doesn't generate any error message even if the user
enters a wrong input.
- [x] It is styled using your own CSS.
- [x] The code follows the code and style conventions as
introduced in the course, is fully documented using comments
and doesn't contain unused or experimental code.
 In particular, the code should not use `print()` or
`console.log()` for any information the app user should see.
Instead, all user feedback needs to be visible in the
browser.
- [x] All exercises have been completed as per the
requirements and pushed to the respective GitHub repository.
