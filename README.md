 🕒 Time Log - Team Lead Activity Tracker (KQ TL Log)

This is a web-based **Time Logging and User Management System** built using Django. It’s designed to help **team leads track task submissions, view team reports**, and manage users effectively. It includes features like dashboard analytics, role-based access, grid views, and dynamic UI components.

---

## 🚀 Features

- 🧑‍💼 Team lead dashboard with data insights
- 📝 Log task activities with update/edit/delete functionality
- 📊 Visual graph view of submitted data
- 👥 Role-based user management (Team Lead, Member, etc.)
- 🧩 Modular UI with reusable components (sidebar, dropdowns, etc.)
- 📁 Dynamic template rendering using Django template tags

---

## 🛠️ Tech Stack

| Layer         | Tools / Technologies             |
|---------------|----------------------------------|
| Frontend      | HTML, CSS, JavaScript, Bootstrap |
| Backend       | Python, Django                   |
| Database      | SQLite (Django default)          |
| Auth & Views  | Django Auth, Django Views        |
| Environment   | Python venv (`timeLogVenv`)      |

---

## 🗂️ Project Structure

timelog/
├── TimeLog/ # Django project settings
├── TimeLogApp/ # Main app
│ ├── components/ # Reusable UI pieces (sidebar, dropdowns, etc.)
│ ├── templates/ # Templates and layout files
│ ├── template_tags/ # Custom Django template filters (if any)
│ ├── migrations/ # Database migrations
│ ├── views.py # App views
│ ├── models.py # Database models
│ └── urls.py # App URLs
├── manage.py
├── requirements.txt
└── timeLogVenv/ # Python virtual environment

yaml
Copy
Edit

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Harinisenthilkumar/kq_tl_log.git
   cd kq_tl_log
Create and activate virtual environment

bash
Copy
Edit
python3 -m venv timeLogVenv
source timeLogVenv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run migrations

bash
Copy
Edit
python manage.py migrate
Start the server

bash
Copy
Edit
python manage.py runserver
Open your browser and go to:
👉 http://127.0.0.1:8000/

