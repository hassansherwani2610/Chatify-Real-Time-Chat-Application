DCN-2 Project: Flask-Based Real-Time Chat Application

University Submission

Course: Data Communication & Networking – II (DCN-2)

Project Type: Semester Project

Backend Framework: Flask (Python)

Frontend: HTML, CSS, JavaScript

Database: SQLite


Students:

Hassan Sherwani (B22110006055)

Muhammad Junaid (B22110006098)

Syed Shabih Haider Naqvi (B22110006164)

Abdur Rahman Siddiqui (B22110006006)


Submission Platform: GitHub


📝 Abstract

This project is a real-time web-based chat application developed using Flask (Python) as part of the DCN-2 (Data Communication & Networking – II) course.

The project demonstrates the practical implementation of client–server communication, HTTP-based request–response models, session management, and real-time message handling using a lightweight web framework.

Authenticated users can communicate through a web interface while applying fundamental networking concepts taught in DCN-2.


🎯 Objectives

✔ To implement a client–server communication model using Flask

✔ To understand HTTP request and response flow

✔ To apply DCN-2 networking concepts in a real-world web application

✔ To manage user sessions and authentication

✔ To design a modular and structured Flask application


⭐ Key Features

🔐 User Authentication (Login & Signup)

👤 Session-Based User Management

💬 One-to-One Chat System

💾 Persistent Message Storage (SQLite)

📱 Clean and Responsive User Interface

🧩 Modular Flask Application Structure


🛠 Technologies Used

🔙 Backend

Python 3

Flask

Gunicorn (Deployment Configuration)


🎨 Frontend

HTML5

CSS3

JavaScript


🗄 Database

SQLite3


🧰 Tools & Libraries

Flask Sessions

Jinja2 Templates

Git & GitHub


🧱 System Architecture

The application follows a client–server architecture:

🖥 Client: Web browser handling UI and user interaction

⚙ Server: Flask application processing requests and responses

🗄 Database: SQLite for storing user data and chat messages

All communication occurs over HTTP, aligning with DCN-2 protocol concepts.


📡 DCN-2 Concepts Applied

📌 Client–Server Architecture

📌 HTTP Protocol

📌 Request–Response Communication

📌 Session Management

📌 Data Persistence

📌 Network-Based Application Design


📂 Project Structure
Chat_Web_App-main

│
├── myapp
│   ├── static
│   │   ├── auth.css
│   │   └── chat.css
│   ├── templates
│   ├── config.py
│   └── database.py
│
├── instance
│   └── database.db
│
├── gunicorn_config.py
├── .env
└── run.py


⚙ Installation & Setup

✅ Prerequisites

Python 3.9 or above

pip (Python Package Manager)

Git


🚀 Setup Instructions

git clone <repository-url>

cd Chat_Web_App-main

python -m venv venv

venv\Scripts\activate   # On Windows

pip install -r requirements.txt

python run.py


🌐 The application will run on:

http://127.0.0.1:5000/


📖 Usage Instructions

1️⃣ Open the application in a web browser

2️⃣ Register a new user account

3️⃣ Log in using valid credentials

4️⃣ Start chatting with other users

5️⃣ Messages are securely stored in the database


🧪 Testing

✔ Manual testing through web browser

✔ Authentication flow verified

✔ Database operations tested successfully


⚠ Limitations

❌ No group chat functionality

❌ No message encryption

❌ Basic UI styling


🚀 Future Enhancements

✨ Group Chat Support

🔐 Message Encryption

🎨 Improved UI/UX

☁ Deployment on Cloud Platform


📜 Academic Declaration

This project is developed strictly for academic purposes as part of the DCN-2 course.
All work submitted is original and complies with university academic integrity policies.




