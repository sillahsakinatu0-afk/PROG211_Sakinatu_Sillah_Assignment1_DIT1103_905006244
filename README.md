# Student Learning Portal

**Module:** PROG211 - Object-Oriented Programming 1
**Domain:** Education (Student Learning Portal)
**Language:** Python 3 (no external libraries)

A small console program that records students, their course and their score,
built with Object-Oriented Programming concepts.

## Features
- Add student records
- Display all records
- Update a student's score
- Show the total number of students
- Automatic letter grade (A-F)

## OOP Concepts Used
| Concept | Where |
|---|---|
| Classes and objects | `Course`, `Student`, `StudentPortal` |
| Attributes | `student_id`, `display_name`, `course`, `score`, `code`, `title` |
| Object interaction | A `Student` holds a `Course` object; `StudentPortal` manages `Student` objects |
| Data structure | One dictionary in `StudentPortal` (student ID -> `Student`) |
| Tuple (optional) | `GRADE_BANDS` holds fixed grade boundaries |
| Instance methods | `update_score()`, `get_grade()`, `display_info()` |
| Class method | `Student.get_total_students()` (`@classmethod`) |
| Static method | `Student.is_valid_score()` (`@staticmethod`) |

## How It Aligns with Digital Public Goods (DPG) Standards
1. **Open-source:** The code is published on GitHub under the MIT License, so anyone can use, study and improve it.
2. **Inclusive and accessible:** It is a plain-text menu with clear messages and input checks. It needs no special hardware, internet or paid software.
3. **Privacy-respecting:** Only an auto-generated ID, a display name (a nickname is allowed) and a score are stored. No phone numbers, addresses or other sensitive personal data are collected, and nothing is saved to disk or sent over a network.
4. **Modular and reusable:** Each class has a single job (`Course`, `Student`, `StudentPortal`) and can be reused in other projects, such as a school app.

## How to Run
```bash
python student_portal.py
```
Choose `1` for a demo or `2` for the interactive portal.

## Example Usage (Demo)
**Input:** `1`

**Output:**
```
Added: Aminata
Added: Mohamed

===== STUDENT RECORDS =====
ID     : STU001
Name   : Aminata
Course : PROG211 - Object-Oriented Programming 1
Score  : 78  (Grade B)
----------------------------------------
ID     : STU002
Name   : Mohamed
Course : PROG211 - Object-Oriented Programming 1
Score  : 72  (Grade B)
----------------------------------------
Total students: 2
```

## Project Files
- `student_portal.py` - Python source code
- `README.md` - documentation
- `LICENSE` - MIT License

## Author
Your Name - Limkokwing University of Creative Technology, Sierra Leone
