Saurav's Test Center
Saurav's Test Center is a Django-based web application for conducting online tests with a user-friendly interface. It supports user authentication, test-taking with a timer and question tracker, and optional feedback collection. The application features a sleek, dark-themed UI built with Tailwind CSS.
Features

User Authentication:
Register with first name, last name, email, password, and optional phone number.
Secure login and logout functionality.


Test Management:
View and start available tests (e.g., DSA Test with 45 questions, 60 minutes, 45 marks, no negative marking).
Instructions page with terms acceptance before starting a test.


Test Interface:
Single-question view with multiple-choice options.
Countdown timer (60 minutes) with auto-submission on expiry.
Question tracker displaying total, attempted, unattempted, and marked-for-review questions.
Navigation via "Previous," "Next," and "Submit Test" buttons.
Mark questions for review, visually indicated in the tracker.
Accurate question numbering (e.g., "Question 1 of 45").


Feedback System:
Optional feedback form with star ratings (1-5) for rating, experience, quality, and difficulty.
Option to skip feedback and return to the homepage.


Security & Usability:
Prevents browser back navigation after test submission.
Clears previous responses and feedback when restarting a test.
Error handling for invalid test or question IDs.
Responsive, futuristic UI with Tailwind CSS.


Admin Panel:
Manage tests, questions, user responses, and feedback at /admin/.


Data Population:
Script (populate_tests.py) to initialize the DSA test with 45 questions.



Project Structure
myexamproject/
├── examapp/
│   ├── migrations/
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── exam_tags.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── myexamproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   ├── base.html
│   ├── error.html
│   ├── feedback.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── test_instructions.html
│   ├── test_list.html
│   └── test_question.html
├── manage.py
├── populate_tests.py
└── requirements.txt

Prerequisites

Python 3.8+
Django 4.2
Git
Virtualenv (recommended)

Installation

Clone the Repository:
git clone https://github.com/<your-username>/sauravs-test-center.git
cd sauravs-test-center


Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Apply Migrations:
python manage.py makemigrations
python manage.py migrate


Create a Superuser:
python manage.py createsuperuser


Populate Test Data:
python manage.py shell
exec(open('populate_tests.py').read())


Collect Static Files:
python manage.py collectstatic


Run the Server:
python manage.py runserver

Access at http://localhost:8000.


Usage

Register/Login:
Register at /register/ or log in at /login/.


Start a Test:
View tests at /tests/.
Select a test, accept terms on the instructions page, and proceed.


Take the Test:
Answer questions, use the tracker to navigate, and mark questions for review.
Submit the test manually or wait for the timer to expire.


Provide Feedback:
Optionally submit star ratings or skip feedback.


Admin Access:
Manage data at /admin/ using superuser credentials.



Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

License
This project is licensed under the MIT License.
Contact
For issues or suggestions, please open an issue on GitHub or contact [your-email@example.com].
