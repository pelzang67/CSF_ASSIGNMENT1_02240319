def addStudent():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = int(input("Enter Marks: "))
    
    # Validation
    if 0 <= marks <= 100:
        students.append({"ID": sid, "Name": name, "Age": age, "Marks": marks})
        print("Student added successfully.")
    else:
        print("Invalid marks! Must be between 0 and 100.")
