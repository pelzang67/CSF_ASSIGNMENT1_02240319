def saveToFile():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['ID']},{s['Name']},{s['Age']},{s['Marks']}\n")
    print("Records saved to file.")
