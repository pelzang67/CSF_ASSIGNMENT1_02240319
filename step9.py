while True:
    displayMenu()
    choice = input("Enter your choice: ")
    if choice == "1":
        addStudent()
    elif choice == "2":
        displayStudents()
    elif choice == "3":
        searchStudent()
    elif choice == "4":
        calculateStatistics()
    elif choice == "5":
        saveToFile()
    elif choice == "6":
        loadFromFile()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
