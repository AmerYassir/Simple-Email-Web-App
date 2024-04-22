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

