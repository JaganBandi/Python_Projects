import array as arr  # Import array module (for fixed-type arrays, unlike Python lists)

# -------------------------------
# Function to assign grade (if-elif-else)
def assign_grade(marks):  # Function receives marks and returns a grade
    if marks >= 90:  # Condition 1: marks ≥ 90
        return "A"  # Return Grade A
    elif marks >= 75:  # Condition 2: marks ≥ 75
        return "B"  # Return Grade B
    elif marks >= 50:  # Condition 3: marks ≥ 50
        return "C"  # Return Grade C
    else:  # If none of the above conditions are true
        return "Fail"  # Return Fail

# -------------------------------
# Function to display all students (uses for loop + arrays)
def display_students(roll_numbers, marks):  # Takes roll_numbers & marks arrays
    print("\n--- Student Records ---")  # Print header
    for i in range(len(roll_numbers)):  # Loop through all students by index
        print(f"Roll No: {roll_numbers[i]}, Marks: {marks[i]}, Grade: {assign_grade(marks[i])}")  
        # Print roll number, marks, and grade assigned by assign_grade()

# -------------------------------
# Function to search student (uses while loop)
def search_student(roll_numbers, marks, roll_no):  # Search by roll_no
    i = 0  # Start index
    while i < len(roll_numbers):  # Continue while index is in bounds
        if roll_numbers[i] == roll_no:  # If current roll matches search key
            print(f"\nStudent Found → Roll No: {roll_numbers[i]}, Marks: {marks[i]}, Grade: {assign_grade(marks[i])}")  
            # Print student details
            return  # Exit function after finding student
        i += 1  # Increment index
    print("\nStudent Not Found!")  # If loop finishes without finding student

# -------------------------------
# Function to insert a new student
def insert_student(roll_numbers, marks, roll_no, mark):  # Add new roll & marks
    if roll_no in roll_numbers:  # Prevent duplicate roll numbers
        print("Error: Roll number already exists!")  
        return  
    roll_numbers.append(roll_no)  # Add new roll number to array
    marks.append(mark)  # Add corresponding marks to marks array
    print(f"Student with Roll No {roll_no} inserted successfully.")  

# -------------------------------
# Function to delete a student
def delete_student(roll_numbers, marks, roll_no):  # Remove student by roll no
    if roll_no in roll_numbers:  # Check if roll exists
        index = roll_numbers.index(roll_no)  # Get index of roll number
        roll_numbers.pop(index)  # Remove roll number from array
        marks.pop(index)  # Remove marks at same index
        print(f"Student with Roll No {roll_no} deleted successfully.")  
    else:
        print("Error: Roll number not found!")  

# -------------------------------
# Main Program (Menu-driven)
def main():  
    print("🎓 Student Management System 🎓")  

    # Initial data stored in arrays
    roll_numbers = arr.array('i', [101, 102, 103, 104, 105])  # Integer array of roll numbers
    marks = arr.array('i', [95, 76, 45, 88, 67])  # Integer array of marks

    while True:  # Infinite loop for menu until user exits
        print("\n--- MENU ---")  
        print("1. Display All Students")  
        print("2. Search Student by Roll Number")  
        print("3. Insert New Student")  
        print("4. Delete Student")  
        print("5. Exit")  

        try:
            choice = int(input("Enter your choice: "))  # Take menu option input
        except ValueError:  # Handle invalid input
            print("Please enter a valid number!")  
            continue  

        if choice == 1:  # Option 1 → Display students
            display_students(roll_numbers, marks)  
        elif choice == 2:  # Option 2 → Search student
            try:
                roll_no = int(input("Enter Roll Number to search: "))  
            except ValueError:
                print("Invalid roll number!")  
                continue  
            search_student(roll_numbers, marks, roll_no)  
        elif choice == 3:  # Option 3 → Insert student
            try:
                roll_no = int(input("Enter New Roll Number: "))  
                mark = int(input("Enter Marks: "))  
            except ValueError:
                print("Invalid input! Roll number and marks must be integers.")  
                continue  
            insert_student(roll_numbers, marks, roll_no, mark)  
        elif choice == 4:  # Option 4 → Delete student
            try:
                roll_no = int(input("Enter Roll Number to delete: "))  
            except ValueError:
                print("Invalid roll number!")  
                continue  
            delete_student(roll_numbers, marks, roll_no)  
        elif choice == 5:  # Option 5 → Exit
            print("Exiting... Thank you!")  
            break  # Break loop to exit
        else:
            print("Invalid choice! Please try again.")  

# -------------------------------
# Run main only if file is executed directly
if __name__ == "__main__":  
    main()  
