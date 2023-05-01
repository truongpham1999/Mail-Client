#### Video Demo:  <https://youtu.be/Wo_7S0V_cec>

# Project Overview
This email client project is a web application that allows users to register, log in, send, receive, and reply emails, and manage their accounts. The application is built using the Flask web framework, SQLite for database management, and Bootstrap for styling. In this README.md file, we will discuss the purpose and contents of each file in the project and outline the design choices made throughout the development process.

## File Structuree
### 1. app.py
This file contains the main server logic and routes for the email client. It imports necessary libraries, sets up the Flask application, and defines routes for handling user actions such as registration, login, email viewing, email composition, and sending emails. The file also initializes the database and handles user session management.

### 2. helpers.py
The "helpers.py" file contains utility functions used throughout the application. These functions include **'apology()'**, which renders an apology message as a response to the user in case of an error, and **'login_required()'**, a decorator to enforce user authentication for specific routes.

### 3. styles.css
This file contains the styling for the email client. It defines the appearance and layout of various elements, such as the navbar, compose input, and compose body. The file also includes media queries for responsiveness on different screen sizes.

### 4. project.db
The "project.db" file is an SQLite database that contains two tables: "users" and "emails".

1. The "users" table stores information about registered users of the email client. It has the following columns:

    **'id'**: An integer primary key that uniquely identifies each user.
    **'username'**: A text column that stores the username of the user.
    **'hash'**: A text column that stores the hashed password of the user.
2. The "emails" table stores information about the emails sent and received by users of the email client. It has the following columns:

    **'id'**: An integer primary key that uniquely identifies each email.
    **'sender'**: A text column that stores the email address of the sender.
    **'recipient'**: A text column that stores the email address of the recipient.
    **'subject'**: A text column that stores the subject of the email.
    **'body'**: A text column that stores the body of the email.
    **'timestamp'**: A text column that stores the date and time the email was sent.
The use of SQLite provides a lightweight and efficient solution for data storage, which is well-suited for a small-scale application like this email client.

### 5. HTML Templates
#### 1. layout.html
This is the base template for all the other templates in the project. It defines the common structure and elements, such as the navbar and page title. Other templates extend this base template and fill in their specific content.

#### 2. index.html
This template displays the user's inbox, listing received emails. Each email is displayed along with its sender, subject, timestamp, and a button to view the email.

#### 3. compose.html
The "compose.html" template provides a form for composing and sending new emails. Users can enter the recipient's email address, a subject, and the email body.

#### 4. reply.html
This template is similar to "compose.html" but is used specifically for replying to an existing email. The form is pre-filled with the original sender's email address and the subject, allowing the user to focus on composing the reply.

#### 5. login.html
The "login.html" template provides a form for users to log in to their accounts. It contains input fields for username and password, as well as a login button.

#### 6. register.html
This template is used for user registration, allowing new users to create an account. The form includes fields for email, password, and password confirmation.

#### 7. sent.html
The "sent.html" template displays a list of sent emails, similar to the "index.html" template. Each email includes the recipient, subject, timestamp, and a button to view the sent email.

#### 8. sent_email_viewing.html
This template displays the details of a sent email, including the recipient, subject, timestamp, and email body.

#### 9. apology.html
The "apology.html" template is used to display error messages and apologies to users. It takes a message and an HTTP status code as input and presents them as a meme-like image.

#### 10. logout.html
This template is displayed when a user logs out of their account. It shows a message informing the user that they have successfully logged out and provides a link to the login page so the user can log back in if they wish.

## Design Choices
When implementing the email client, several design choices were made to enhance user experience and ensure code maintainability:

1. The use of a base template, "layout.html", to keep the HTML structure consistent across all pages and simplify the management of common elements.

2. The inclusion of responsive design in the "styles.css" file to ensure a seamless experience on various screen sizes.

3. The separation of utility functions into a dedicated "helpers.py" file, promoting code reusability and modularity.

4. The use of Flask's template inheritance system to extend the base template and customize content for each page, resulting in a clean and organized codebase.

5. The decision to use the Flask micro-framework allowed for a lightweight and flexible implementation, while still providing the necessary functionality for the email client.

6. The use of media queries in "styles.css" ensures that the email client's layout and design adapt to different screen sizes and devices, providing a consistent user experience.

7. The choice to create separate templates for replying to emails and composing new emails improves the user experience by pre-filling relevant information and maintaining a clear distinction between the two actions.

8. The use of the "helpers.py" file to define the **'login_required'** decorator allows for easy enforcement of authentication on specific routes, ensuring that only authenticated users can access certain parts of the application.

9. The use of the "apology.html" template to display error messages in a humorous and friendly manner can help ease user frustration when encountering issues.

10. The choice to use Bootstrap as a CSS framework provides a solid foundation for the email client's design and ensures compatibility across various browsers and devices.

## Conclusion
This email client project demonstrates a simple but functional implementation using the Flask web framework. It allows users to register, log in, send and receive emails, and manage their accounts. The project's modular design and clear organization make it easy to maintain and expand upon in the future.

By explaining the purpose of each file and the design choices made throughout the project, this README.md file serves as a comprehensive guide for anyone looking to understand, modify, or expand the email client's functionality.