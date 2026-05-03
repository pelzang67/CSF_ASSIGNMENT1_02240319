def searchStudent():
    sid = input("Enter Student ID to search: ")
    for s in students:
        if s['ID'] == sid:
            print(f"Found: {s['ID']} | {s['Name']} | {s['Age']} | {s['Marks']}")
            return
    print("Student not found.")
