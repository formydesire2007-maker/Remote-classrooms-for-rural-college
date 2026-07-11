-- ==========================================
-- Remote Classroom for Rural Colleges
-- Database Schema
-- ==========================================


-- Create Users Table

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(120) UNIQUE NOT NULL,

    password VARCHAR(255) NOT NULL,

    college VARCHAR(150),

    role VARCHAR(50) DEFAULT 'student',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



-- Create Lectures Table

CREATE TABLE IF NOT EXISTS lectures (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title VARCHAR(200) NOT NULL,

    subject VARCHAR(100),

    faculty_name VARCHAR(100),

    lecture_file VARCHAR(255),

    transcript TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



-- Create Quiz Table

CREATE TABLE IF NOT EXISTS quizzes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    topic VARCHAR(200),

    difficulty VARCHAR(50),

    questions TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



-- Create Translation History Table

CREATE TABLE IF NOT EXISTS translations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    source_text TEXT,

    translated_text TEXT,

    language_direction VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



-- Create Chat History Table

CREATE TABLE IF NOT EXISTS chat_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    question TEXT,

    answer TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(user_id)
    REFERENCES users(id)

);