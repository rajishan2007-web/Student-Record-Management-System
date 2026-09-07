# 🎓 Student Record Management System

[![GitHub Repository](https://img.shields.io/badge/GitHub-Student--Record--Management--System-blue?style=flat&logo=github)](https://github.com/rajishan2007-web/Student-Record-Management-System)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-Supabase%20PostgreSQL-3ECF8E?style=flat&logo=supabase&logoColor=white)](https://supabase.com/)
[![UI](https://img.shields.io/badge/GUI-Tkinter%20Dark%20Theme-000000?style=flat)](https://docs.python.org/3/library/tkinter.html)

A sleek, modern, dark-themed **Student Record Management System** built in Python with `Tkinter` and powered by a cloud-hosted **Supabase PostgreSQL** database. 

🔗 **GitHub Repository:** [https://github.com/rajishan2007-web/Student-Record-Management-System](https://github.com/rajishan2007-web/Student-Record-Management-System)

---

## ✨ Key Features

- 🎨 **Modern Dark Aesthetics**: Custom dark theme (`#0c0c0c`) with minimalist typography and UI controls.
- ⚡ **Fade-in Animation**: Smooth window opacity transition on launch.
- ☁️ **Cloud Database**: Directly connected to **Supabase PostgreSQL** for real-time data persistence.
- 📝 **Full CRUD Operations**:
  - **Create**: Add new student records with name, course, marks, and attendance %.
  - **Read**: View all student records in a structured tabular list.
  - **Update**: Modify existing student information seamlessly.
  - **Delete**: Remove student records from the database.
- 🔍 **Live Search**: Instant student filtering by name using PostgreSQL `ILIKE` queries.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.x |
| **GUI Framework** | Tkinter |
| **Database** | PostgreSQL (Hosted on Supabase) |
| **DB Driver** | `psycopg2-binary` |

---

## 📋 Database Schema

The application automatically creates the required table on startup if it does not exist:

```sql
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    course VARCHAR(50),
    marks INT,
    attendance INT
);
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/rajishan2007-web/Student-Record-Management-System.git
cd Student-Record-Management-System
```

### 2. Install Dependencies
```bash
pip install psycopg2-binary
```

### 3. Run the Application
```bash
python main.py
```

---

## 👤 Author

Developed by **[rajishan2007-web](https://github.com/rajishan2007-web)**
- **GitHub**: [@rajishan2007-web](https://github.com/rajishan2007-web)
- **Repository**: [Student-Record-Management-System](https://github.com/rajishan2007-web/Student-Record-Management-System)