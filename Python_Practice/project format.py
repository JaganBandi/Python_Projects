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

def display_students(roll_numbers, marks):
    print("\n--- Student Records ---")  
    for i in range(len(roll_numbers)):  
        print(f"Roll No: {roll_numbers[i]}, Marks: {marks[i]}, Grade: {assign_grade(marks[i])}")  
def search_student(roll_numbers, marks, roll_no): 
    i = 0  
    while i < len(roll_numbers): 
        if roll_numbers[i] == roll_no: 
            print(f"\nStudent Found → Roll No: {roll_numbers[i]}, Marks: {marks[i]}, Grade: {assign_grade(marks[i])}")  # Print the found student's details
            return  
        i += 1  
    print("\nStudent Not Found!")  


def main(): 
    print("🎓 Student Management System 🎓") 
    roll_numbers = arr.array('i', [101, 102, 103, 104, 105]) 
    marks = arr.array('i', [95, 76, 45, 88, 67]) 

    while True:  
        print("\n--- MENU ---") 
        print("1. Display All Students") 
        print("2. Search Student by Roll Number") 
        print("3. Exit") 

        try: 
            choice = int(input("Enter your choice: "))  
        except ValueError:  
            print("Please enter a valid number!")  
            continue  

        if choice == 1:
            display_students(roll_numbers, marks)  
        elif choice == 2:  
            try:  
                roll_no = int(input("Enter Roll Number to search: ")) 
            except ValueError:  
                print("Please enter a valid roll number!")  
                continue  
            search_student(roll_numbers, marks, roll_no)  
        elif choice == 3:  
            print("Exiting... Thank you!")
            break  
        else:  
            print("Invalid choice! Please try again.") 
if __name__ == "__main__": 
main()  