# 🏠 RoomMatch

A full-stack roommate matching web application that helps users find compatible roommates based on lifestyle preferences such as cleanliness, noise tolerance, sleep schedule, and study habits.

RoomMatch combines Python, PHP, and SQLite to handle data processing, storage, and user interface interactions — creating a simple yet functional platform for pairing compatible roommates.

---

## Overview

RoomMatch was built to streamline the process of matching students or tenants with roommates who share similar living preferences.
It allows users to input their personal habits and preferences, then uses backend logic to identify the best potential matches based on compatibility scores.

---

## Core Features

Roommate Matching Algorithm: Calculates compatibility using user input and preference weighting.
Database Integration: Stores user profiles and preferences using SQLite for quick data access.
Interactive Frontend: Simple HTML and PHP forms for user input and displaying match results.
Dynamic Backend Logic: Python and PHP scripts handle data insertion, querying, and match generation.
Seamless Integration: Combines Python’s backend logic with PHP’s web handling to simulate a full-stack flow.

---

## Tech Stack

Frontend -	HTML, CSS, PHP	- User interface for inputting roommate preferences and displaying matches.
Backend -	Python, PHP	- Core matching logic, data validation, and communication with the database.
Database -	SQLite - Lightweight and embedded database to store user and preference data.

---

## How It Works

Users enter their name, email, and lifestyle preferences through an HTML/PHP form.
Submitted data is validated and stored in the SQLite database.
Python scripts analyze user attributes and calculate compatibility scores.
The system outputs roommate matches ranked by similarity score.

Example logic (simplified):

if abs(user1.noise - user2.noise) < 2 and abs(user1.cleanliness - user2.cleanliness) < 2:
    compatibility = "High"
else:
    compatibility = "Low"

---

## File Overview

- index.html	Main landing page for user input.
- add_student.py / add_student.php	Scripts for adding new user data into the database.
- assign_room.py / assign_room.php	Core matching logic and result display.
- python_db.py	Database connection and query handling (SQLite).
- seed_db.py	Initializes the database with sample users for testing.
- hello.py / hello.html	Example test endpoints used during setup.

---

## Example Workflow

User Registration:

A new user submits their name, major, and preferences via form.
Data is stored using add_student.py.

Match Generation:

assign_room.py fetches all user data and runs a comparison algorithm.
Compatible pairs are printed or displayed via PHP templates.

Database Operations:

SQLite handles persistent storage of users and scores.
The schema can be easily extended to include new attributes like roommate requests or lease duration.

---

## Lessons Learned

- Building full-stack systems that integrate multiple languages and data layers.
- Using Python and PHP together to manage both backend computation and frontend serving.
- Structuring a lightweight web application without relying on frameworks.
- Handling database persistence and CRUD operations through both Python scripts and PHP forms.


## Author

Hunter Braddy
B.S. Computer Science, University of Arkansas
Concentration: Cybersecurity | Minor: Mathematics


## License

This project is open source under the MIT License.
See the LICENSE file for more details.
