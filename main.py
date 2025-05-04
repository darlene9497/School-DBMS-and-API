from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
import mysql.connector
from datetime import date

# initialize FastAPI app
app = FastAPI()

# connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",  # replace with your MySQL password
    database="school_db"
)
cursor = conn.cursor(dictionary=True)

# pydantic models
class Student(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    email: EmailStr
    phone: str

class Teacher(BaseModel):
    full_name: str
    email: EmailStr
    hire_date: date

class Course(BaseModel):
    course_name: str
    description: Optional[str] = None
    teacher_id: Optional[int] = None

class Enrollment(BaseModel):
    student_id: int
    course_id: int

class Grade(BaseModel):
    enrollment_id: int
    grade: str
    graded_at: Optional[date] = date.today()

# CRUD routes
# Create a new student
@app.post("/students/")
def create_student(student: Student):
    query = """
        INSERT INTO students (first_name, last_name, date_of_birth, gender, email, phone)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (student.first_name, student.last_name, student.date_of_birth, student.gender, student.email, student.phone))
    conn.commit()
    return {"message": "Student created successfully"}

# Get all students
@app.get("/students/")
def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

# Get a student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    student = cursor.fetchone()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update a student's details
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    query = """
        UPDATE students 
        SET first_name = %s, last_name = %s, date_of_birth = %s, gender = %s, email = %s, phone = %s
        WHERE student_id = %s
    """
    cursor.execute(query, (student.first_name, student.last_name, student.date_of_birth, student.gender, student.email, student.phone, student_id))
    conn.commit()
    return {"message": "Student updated successfully"}

# Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    return {"message": "Student deleted successfully"}

# Create a new teacher
@app.post("/teachers/")
def create_teacher(teacher: Teacher):
    query = """
        INSERT INTO teachers (full_name, email, hire_date)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (teacher.full_name, teacher.email, teacher.hire_date))
    conn.commit()
    return {"message": "Teacher created successfully"}

# Get all teachers
@app.get("/teachers/")
def get_teachers():
    cursor.execute("SELECT * FROM teachers")
    return cursor.fetchall()

# Get a teacher by ID
@app.get("/teachers/{teacher_id}")
def get_teacher(teacher_id: int):
    cursor.execute("SELECT * FROM teachers WHERE teacher_id = %s", (teacher_id,))
    teacher = cursor.fetchone()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

# Create a new course
@app.post("/courses/")
def create_course(course: Course):
    query = """
        INSERT INTO courses (course_name, description, teacher_id)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (course.course_name, course.description, course.teacher_id))
    conn.commit()
    return {"message": "Course created successfully"}

# Get all courses
@app.get("/courses/")
def get_courses():
    cursor.execute("SELECT * FROM courses")
    return cursor.fetchall()

# Create a new enrollment
@app.post("/enrollments/")
def create_enrollment(enrollment: Enrollment):
    query = """
        INSERT INTO enrollments (student_id, course_id)
        VALUES (%s, %s)
    """
    cursor.execute(query, (enrollment.student_id, enrollment.course_id))
    conn.commit()
    return {"message": "Enrollment created successfully"}

# Get all enrollments
@app.get("/enrollments/")
def get_enrollments():
    cursor.execute("""
        SELECT e.enrollment_id, s.first_name, s.last_name, c.course_name
        FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
        JOIN courses c ON e.course_id = c.course_id
    """)
    return cursor.fetchall()

# Assign a grade
@app.post("/grades/")
def create_grade(grade: Grade):
    query = """
        INSERT INTO grades (enrollment_id, grade, graded_at)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (grade.enrollment_id, grade.grade, grade.graded_at))
    conn.commit()
    return {"message": "Grade assigned successfully"}

# Get all grades
@app.get("/grades/")
def get_grades():
    cursor.execute("""
        SELECT g.grade_id, s.first_name, s.last_name, c.course_name, g.grade
        FROM grades g
        JOIN enrollments e ON g.enrollment_id = e.enrollment_id
        JOIN students s ON e.student_id = s.student_id
        JOIN courses c ON e.course_id = c.course_id
    """)
    return cursor.fetchall()

# Testing the API
# to run the FastAPI app, use: uvicorn main:app --reload
