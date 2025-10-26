#!/usr/bin/env python3
import sys
import python_db

# — your MySQL/Turing credentials:
HOST, USER, PW, DB = 'localhost', 'hbraddy', 'eeHa9ohv', 'hbraddy'

def main():
    # Expect exactly 3 args after the script name
    if len(sys.argv) != 4:
        print("Usage: assign_room.py <StudentId> <BuildingId> <RoomNumber>")
        sys.exit(1)

    sid, bid, roomno = sys.argv[1:]
    python_db.open_database(HOST, USER, PW, DB)

    # 1) Fetch the student's wants
    student_q = (
        "SELECT WantsAC, WantsDining, WantsKitchen, WantsPrivateBathroom "
        f"FROM Student WHERE StudentId = {sid};"
    )
    student = python_db.cursor.execute(student_q) or python_db.cursor.fetchone()
    cursor = python_db.cursor
    cursor.execute(student_q)
    want_ac, want_dining, want_kitchen, want_pb = cursor.fetchone()

    # 2) Fetch the room's attributes
    room_q = (
        "SELECT HasAC, HasDining, HasKitchen, PrivateBathrooms "
        f"FROM Room WHERE BuildingId = {bid} AND RoomNumber = '{roomno}';"
    )
    cursor.execute(room_q)
    room = cursor.fetchone()
    if not room:
        print(f"Error: Room {bid}-{roomno} does not exist.")
        python_db.close_db()
        sys.exit(1)
    has_ac, has_dining, has_kitchen, has_pb = room

    # 3) Validate each want against the room
    errors = []
    if want_ac     and not has_ac:     errors.append("AC")
    if want_dining and not has_dining: errors.append("Dining")
    if want_kitchen and not has_kitchen: errors.append("Kitchen")
    if want_pb     and not has_pb:     errors.append("Private bath")

    if errors:
        print("Cannot assign: room lacks " + ", ".join(errors))
        python_db.close_db()
        sys.exit(1)

    # 4) Do the assignment
    # Note: Assignment(StudentId,BuildingId,RoomNumber)
    python_db.insert('Assignment', f"{sid},{bid},'{roomno}'")

    # 5) Show all assignments for this student
    out_q = (
      "SELECT A.StudentId, S.Name, A.BuildingId, A.RoomNumber "
      "FROM Assignment A "
      "JOIN Student S ON A.StudentId=S.StudentId "
      f"WHERE A.StudentId={sid};"
    )
    print(python_db.executeSelect(out_q))

    python_db.close_db()

if __name__ == '__main__':
    main()
