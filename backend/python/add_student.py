#!/usr/bin/env python3
import sys
import python_db

# — your MySQL/Turing credentials:
HOST, USER, PW, DB = 'localhost', 'hbraddy', 'eeHa9ohv', 'hbraddy'

def main():
    if len(sys.argv) != 6:
        print("Usage: add_student.py <Name> <WantsAC> <WantsDining> <WantsKitchen> <WantsPrivateBathroom>")
        sys.exit(1)

    name, ac, dining, kitchen, pb = sys.argv[1:]

    # Open DB
    python_db.open_database(HOST, USER, PW, DB)

    # Generate StudentId
    sid = python_db.nextId('Student')

    # Build VALUES string in Student column order
    # Note: StudentId,Name,WantsAC,WantsDining,WantsKitchen,WantsPrivateBathroom
    values = f"'{sid}','{name}',{ac},{dining},{kitchen},{pb}"

    # Insert
    python_db.insert('Student', values)

    # Show updated table
    output = python_db.executeSelect('SELECT * FROM Student;')
    print(output)

    python_db.close_db()

if __name__ == '__main__':
    main()

