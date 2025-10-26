#!/usr/bin/env python3
import python_db

# — your MySQL/Turing credentials:
HOST, USER, PW, DB = 'localhost', 'hbraddy', 'seed_db.py', 'hbraddy'

def seed():
    python_db.open_database(HOST, USER, PW, DB)

    # 3 sample buildings
    python_db.executeUpdate(
        "INSERT INTO Building (Name, Address, HasAC, HasDining) VALUES "
        "('Alpha Hall','123 College Ave',1,0),"
        "('Beta Hall','456 University St',1,1),"
        "('Gamma Hall','789 Campus Rd',0,0);"
    )

    # 3 rooms each
    rooms = [
      (1,'101',2,0,0),(1,'102',2,1,0),(1,'103',1,1,1),
      (2,'201',2,1,1),(2,'202',1,0,0),(2,'203',2,0,1),
      (3,'301',1,0,0),(3,'302',2,1,0),(3,'303',2,0,0)
    ]
    for b, r, nb, pb, kt in rooms:
        python_db.executeUpdate(
            f"INSERT INTO Room VALUES ({b},'{r}',{nb},{pb},{kt});"
        )

    # 3 students
    students = [
      ('Alice',1,0,0,0),
      ('Bob',0,1,0,1),
      ('Carol',1,1,1,1)
    ]
    for name, ac, dn, kt, pb in students:
        python_db.executeUpdate(
            f"INSERT INTO Student (Name, WantsAC, WantsDining, WantsKitchen, WantsPrivateBathroom) "
            f"VALUES ('{name}',{ac},{dn},{kt},{pb});"
        )

    python_db.close_db()
    print('Seeding complete.')

if __name__ == '__main__':
    seed()


