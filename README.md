📝 Project Description – REST API with Flask + HTML/CSS
Objective

The goal of this project is to create a REST API using Flask that manages user data, and also provide a simple frontend (HTML + CSS + JS) to interact with the API without needing external tools like Postman.

Tools & Technologies

Python – Backend programming language

Flask – Web framework to build API endpoints

HTML & CSS – For frontend structure and styling

JavaScript (Fetch API) – To send API requests from the webpage

In-Memory Dictionary – To store user data

Features

REST API Endpoints

GET /users → Fetch all users

POST /users → Create a new user

PUT /users/<id> → Update existing user

DELETE /users/<id> → Delete a user

Frontend (index.html)

Add new users through a form

View the list of users dynamically

Styled with CSS for better presentation

Data Storage

Users are stored in an in-memory dictionary (temporary storage, resets when server restarts).

Each user has an ID, name, and age.

Workflow

Run python app.py → Flask server starts at http://127.0.0.1:5000/.

Open the browser → The HTML page loads.

Enter Name and Age, click Add User → Data is sent to Flask via POST /users.

Flask updates the dictionary and reloads the updated user list.

Users can also be managed via Postman or Curl using the API routes.

Outcome

Learned API development fundamentals.

Understood how Flask routes map to CRUD operations.

Built a mini full-stack project combining Python backend and HTML/CSS frontend.

✨ This project demonstrates both backend (Flask API) and frontend integration with API calls, which is a key step in learning full-stack development.


<img width="785" height="455" alt="image" src="https://github.com/user-attachments/assets/78a7d7bb-fa80-4016-b80f-908d72901861" />
