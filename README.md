# Online Course Platform - Mini

**A minimalist Django-based learning management system**  
*"Bonsoir, Elliot here. This is my clean, efficient course platform with exam functionality - no bloat, just what works."*

## Key Features

- **Secure authentication** (Django auth system)
- **Course & lesson management** (CRUD operations)
- **Exam system** (Questions, choices, submissions)
- **Progress tracking** (Enrollments, completions)
- **Clean UI** (Tailwind CSS)

## Technical Stack

| Component       | Technology          |
|-----------------|---------------------|
| Backend        | Django 4.2          |
| Database       | SQLite (default)    |
| Frontend       | Tailwind CSS        |
| Authentication | Django auth         |
| Deployment     | Docker-ready        |

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/online_course_mini.git
cd online_course_mini
```

2. **Set up environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

3. **Configure database**
```bash
python manage.py migrate
python manage.py createsuperuser
```

4. **Run development server**
```bash
python manage.py runserver
```

## Project Structure

```
online_course_mini/
├── courses/               # Main application
│   ├── models.py          # Database schema
│   ├── views.py           # Business logic
│   ├── urls.py            # Routing
│   └── templates/         # UI components
├── online_course_mini/    # Project config
└── README.md              # This document
```

## Security Notes

- CSRF protection enabled
- Password hashing (PBKDF2)
- SQL injection protection
- XSS safeguards

*"I don't make insecure systems. That's how they get you."*

## Contribution

This is a personal project. No external contributions accepted.

## License

MIT License - *"Because the world needs more open knowledge."*
