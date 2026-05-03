def calculateStatistics():
    if not students:
        print("No records to calculate.")
        return
    marks = [s['Marks'] for s in students]  # List comprehension
    print(f"Highest: {max(marks)}")
    print(f"Lowest: {min(marks)}")
    print(f"Average: {sum(marks)/len(marks):.2f}")
