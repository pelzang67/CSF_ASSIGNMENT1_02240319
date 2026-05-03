def displayStudents():
    if not students:  # Check if list is empty
        print("No records found.")
    else:
        for s in students:
            print(f"{s['ID']} | {s['Name']} | {s['Age']} | {s['Marks']}")
