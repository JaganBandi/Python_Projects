import array as arr
def assign_grade(marks): 
    if marks >= 90:
        return "A"  
    elif marks >= 75: 
        return "B"  
    elif marks >= 50:  
        return "C"  
    else:  
        return "Fail"  

# Function to display all students (uses for loop + arrays)
def display_students(roll_numbers, marks):  # Define a function that prints each student's details
    print("\n--- Student Records ---")  # Print a header with a leading newline for spacing
    for i in range(len(roll_numbers)):  # Loop over indices from 0 to length-1 of the roll_numbers array
        # Access elements by index and compute grade on the fly
        print(f"Roll No: {roll_numbers[i]}, Marks: {marks[i]}, Grade: {assign_grade(marks[i])}")  # Print roll, marks, and grade

# Function to search a student by roll number (uses while loop)
def search_student(roll_numbers, marks, roll_no):  # Define a function to find and display a student's record
    i = 0  # Start index at 0
    while i < len(roll_numbers):  # Continue while index is within array bounds
        if roll_numbers[i] == roll_no:  # Check if current roll number matches the one being searched
            print(f"\nStudent Found → Roll No: {roll_numbers[i]}, Marks: {marks[i]}, Grade: {assign_grade(marks[i])}")  # Print the found student's details
            return  # Exit the function after finding the student
        i += 1  # Move to the next index
    print("\nStudent Not Found!")  # If loop ends without a match, inform the user

# -------------------------------
# Main Program entry that ties everything together
def main():  # Define the main function that runs the menu-driven program
    print("🎓 Student Management System 🎓")  # Display the application title

    # Create arrays of roll numbers and corresponding marks (fixed-type integer arrays)
    roll_numbers = arr.array('i', [101, 102, 103, 104, 105])  # Integer array of roll numbers
    marks = arr.array('i', [95, 76, 45, 88, 67])  # Integer array of marks aligned by index with roll_numbers

    while True:  # Infinite loop to keep showing the menu until the user chooses to exit
        print("\n--- MENU ---")  # Print menu header with spacing
        print("1. Display All Students")  # Option 1 description
        print("2. Search Student by Roll Number")  # Option 2 description
        print("3. Exit")  # Option 3 description

        try:  # Try block to safely parse numeric input for the menu choice
            choice = int(input("Enter your choice: "))  # Read user input as string and convert to integer
        except ValueError:  # If conversion fails (non-numeric input)
            print("Please enter a valid number!")  # Inform the user about invalid input
            continue  # Restart the loop to show the menu again

        if choice == 1:  # If user selected option 1
            display_students(roll_numbers, marks)  # Call function to list all students using a for loop
        elif choice == 2:  # If user selected option 2
            try:  # Try block to parse the roll number input
                roll_no = int(input("Enter Roll Number to search: "))  # Read and convert roll number to integer
            except ValueError:  # Handle non-numeric roll number input
                print("Please enter a valid roll number!")  # Inform the user about invalid input
                continue  # Go back to the menu
            search_student(roll_numbers, marks, roll_no)  # Call function to search using a while loop
        elif choice == 3:  # If user selected option 3
            print("Exiting... Thank you!")  # Friendly exit message
            break  # Break the while True loop to end the program
        else:  # If the choice is not 1, 2, or 3
            print("Invalid choice! Please try again.")  # Ask the user to select a valid option

# Standard Python idiom to run main() only when this file is executed directly
if __name__ == "__main__":  # Check if this script is the entry point
    main()  # Call the main function to start the program
