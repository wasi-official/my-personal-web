# Student Management System 🎓

A simple web application built with Flask and pandas to manage and display student information.

## Features
- 📊 View all students in a table format
- 👨‍🎓 Individual student profile pages
- 📈 Statistics dashboard (total students, average marks, average age)
- 🎨 Beautiful responsive design with Bootstrap
- 🏆 Automatic grade calculation

## Installation & Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open your browser and visit:**
   ```
   http://127.0.0.1:5000
   ```

## Usage

- **Home Page (`/`)**: View all students, statistics, and quick access links
- **Student Details (`/student/<name>`)**: View individual student information
  - Example: `http://127.0.0.1:5000/student/Ali`

## Project Structure
```
📁 your-project/
├── 📄 app.py              # Main Flask application
├── 📄 test.py             # Original pandas script
├── 📄 requirements.txt    # Dependencies
├── 📄 README.md           # This file
└── 📁 templates/
    ├── 📄 base.html       # Base template
    ├── 📄 index.html      # Home page
    └── 📄 student.html    # Student details page
```

## Current Students
- Ali (Age: 21, Marks: 85%)
- Sara (Age: 22, Marks: 92%)
- Hamza (Age: 20, Marks: 78%)

Enjoy your student management system! 🚀