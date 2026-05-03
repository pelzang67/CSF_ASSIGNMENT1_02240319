def loadFromFile():
    global students
    students = []
    try:
        with open("students.txt", "r") as f:
            for line in f:
                sid, name, age, marks = line.strip().split(",")
                students.append({"ID": sid, "Name": name, "Age": int(age), "Marks": int(marks)})
        print("Records loaded from file.")
    except FileNotFoundError:
        print("No file found.")
