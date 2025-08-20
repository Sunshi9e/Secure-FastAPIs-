# 🔐 Secure FastAPI Mini Projects

This repository contains 4 beginner-friendly FastAPI projects, each focused on implementing different levels of authentication & security.
They are designed as small, independent apps — perfect for learning step by step.

---

## Projects Overview

### 1. Job Application Tracker API

- Per-user secure access with simple tokens.

- Users can only view their own job applications.

### 2. Notes API with JWT Authentication

- Full JWT-based authentication.

- Users can log in, add notes, and view only their own notes.

### 3. Secure Shopping Cart API

- Role-based access control (Admin vs. Customer).

- Admins manage products, customers manage their own cart.

### 4. Secure Student Portal API

- User registration & login with password hashing.

- Students can securely view their own grades.

## How to Use

- Each project is located in its own folder (`job_tracker/`, `notes_api/`, `shopping_api/`, `student_portal/`).

- Every project has a detailed README with setup instructions.

- To try one:

```bash
cd <project_name>
```
- Follow the `README.md` instruction to install necessary dependencies.
     
- next start the app

```bash
uvicorn main:app --reload
```

## Purpose

These projects build up from basic token **authentication → JWT → role-based access → password hashing**,
helping you learn FastAPI authentication step by step.
