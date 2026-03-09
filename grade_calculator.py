# Start an infinite loop to keep the program running
while True:
    print("\n--- Student Grade System ---")
    print("(Type 'Exit' as the name to stop the program)")
    
    # 1. Ask for the student's name
    name = input("Enter the student's name: ")

    # 2. Check if the user wants to stop the program
    # .lower() ensures it works if they type 'exit', 'EXIT', or 'Exit'
    if name.lower() == "exit":
        print("Exiting program. Goodbye!")
        break  # This exits the while loop immediately

    # 3. Ask for marks for three subjects
    # We use float() to allow decimal marks
    mark1 = float(input("Enter marks for Subject 1: "))
    mark2 = float(input("Enter marks for Subject 2: "))
    mark3 = float(input("Enter marks for Subject 3: "))

    # 4. Calculate the average mark
    average = (mark1 + mark2 + mark3) / 3

    # 5. Assign grades based on the average
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # 6. Display the output in the requested formatted style
    print("\n------------------------------")
    print(f"Name : {name}")
    print(f"Average : {average:.1f}") # .1f shows one decimal place
    print(f"Grade : {grade}")
    print("------------------------------")