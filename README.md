# Email Web App

A basic web application for sending and receiving emails.

## Table of Contents

- [Installation](#Installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Contact](#contact)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AmerYassir/Simple-Email-Web-App/.git
    ```

3. Install dependencies:

    ```bash
    pip install flask
    pip install sqlit3
    ```

4. Start the server:

    ```bash
    flask --app main.py run
    ```
    in case you want to work in debug mode
    ```bash
    flask --app main.py --debug run
    ```

6. Open your web browser and go to `http://localhost:5000 or http://127.0.0.1:5000/` to access the application.

## Usage

1. Sign up for an account or log in if you already have one.
2. Compose a new email by clicking on the "Write Email" button.
3. Enter the recipient's email address, subject, and message content.
4. Click the "Send" button to send the email.
5. Check your inbox for received emails.
6. Click on an email to view its contents.
<!--
## Configuration

The application uses environment variables for configuration. Create a `.env` file in the root directory and provide the following variables:

- `EMAIL_HOST`: The SMTP server hostname.
- `EMAIL_PORT`: The SMTP server port.
- `EMAIL_USERNAME`: Your email account username.
- `EMAIL_PASSWORD`: Your email account password.
- `DATABASE_URL`: URL for the database connection.

Example `.env` file:
-->

## Project Checklist
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
 - Line number(s) for the class definition: 13:51
 - Name of two properties:'db_name','msg_count'
 - Name of two methods:'write_user','write_message'
 - File name and line numbers where the methods are used:'main.py' 52,131 respectively
- [x] It makes use of JavaScript in the front end and uses the
localStorage of the web browser.
- [x] It uses modern JavaScript (for example, let and const
rather than var).
- [x] It makes use of the reading and writing to the same file
feature.
- [x] It contains conditional statements. Please provide below
the file name and the line number(s) of at least one example of a conditional statement in your code.
 - File name: main.py
 - Line number(s):65,67,124
- [x] It contains loops. Please provide below the file name
and the line number(s) of at least
 one example of a loop in your code.
 - File name:'main.py'
 - Line number(s):103
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
