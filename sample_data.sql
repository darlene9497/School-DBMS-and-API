USE school_db;

-- Insert teachers
INSERT INTO teachers (full_name, email, hire_date) VALUES
('Dedan Okware', 'dedan.okware@school.edu', '2020-01-15'),
('Gerald Macherechedze', 'gerald.macherechedze@school.edu', '2021-06-10'),
('Evans Mutuku', 'evans.mutuku@school.edu', '2022-11-02');

-- Insert courses
INSERT INTO courses (course_name, description, teacher_id) VALUES
('Web Development', 'Equip learners with the skills to build and maintain websites and web applications', 1),
('Database Design', 'Analyze real-world business scenarios and identify data requirements', 2),
('Python', 'A project-driven course to equip you with essential programming skills to build real-world applications with Python', 3);

-- Insert students
INSERT INTO students (first_name, last_name, date_of_birth, gender, email, phone) VALUES
('Darlene', 'Nyambura', '2005-03-20', 'Female', 'darlene@student.edu', '0712345678'),
('Brolin', 'Kinyanjui', '2004-07-14', 'Male', 'brolin@student.edu', '0798765432'),
('Sydney', 'Charles', '2001-11-01', 'Other', 'sydney@student.edu', '+254112233445');

-- Insert enrollments
INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1),
(1, 2),
(3, 2),
(3, 3),
(2, 1),
(2, 2);

-- Insert grades
INSERT INTO grades (enrollment_id, grade, graded_at) VALUES
(1, 'A', '2024-12-01'),
(2, 'B+', '2024-12-01'),
(3, 'A-', '2024-12-01'),
(4, 'B', '2024-12-01'),
(5, 'C+', '2024-12-01'),
(6, 'B-', '2024-12-01');
