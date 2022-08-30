# importing modules
from console_color import *
from student import Student

# creating database
student_database = []


# welcome screen menu
def welcome_screen():
    print(BANANA_YELLOW, '**** Welcome To NIIT Student Management System ****')
    user_input = int(input('1. Add Student\n'
                           '2. View all student details\n'
                           '3. Search for Student Info\n'
                           '4. Delete Student Info\n'
                           '5. Update Student Info\n'
                           '6. About System\n'
                           '7. Exit Application\n\n'
                           'Please Provide Your Request: '))
    user_options(user_input)


# user_options function
def user_options(user_input):
    if user_input == 1:
        response = 'yes'
        while response == 'yes':
            student_info = add_student_info()
            user_ans = input(BLUE + 'Do You Want to save info?(y/n): ').lower()
            if user_ans == 'y':
                student_database.append(student_info)
                print(LIGHT_GREEN, f'{student_info.get_first_name()} '
                                   f'{student_info.get_middle_name()} '
                                   f'{student_info.get_last_name()} added SUCCESSFULLY !!!')
            elif user_ans == 'n':
                user_ans = input('Are You Sure?(y/n): ').lower()
                if user_ans == 'y':
                    welcome_screen()
                else:
                    student_database.append(student_info)
            else:
                welcome_screen()
            response = input('Do You Have another Student?(yes/no): ').lower()
        welcome_screen()
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    elif user_input == 5:
        pass
    elif user_input == 6:
        about_us()
    elif user_input == 7:
        close_program()
    else:
        invalid_request()


# about_us function
def about_us():
    print(LIGHT_BLUE, '**** This System Keep track Of Student Details ****')
    welcome_screen()


# close_program function
def close_program():
    print(LIGHT_BLUE, 'Thank You For Using NIIT SMS')
    exit(1)


# invalid_request function
def invalid_request():
    print(RED, 'Invalid Request, Try again!!!')
    welcome_screen()


# add a new student
def add_student_info():
    print(BANANA_YELLOW, '**** Fill Details Below To Add Student ****', WHITE)
    sid = input('Student ID: ')
    f_name = input('First Name: ')
    m_name = input('Middle Name: ')
    l_name = input('last Name: ')
    dob = input('Date Of Birth e.g(dd-mm-yyyy): ')
    course = input('Course: ')
    duration = input('Duration: ')

    # creating student object
    student_info = Student(sid, f_name, m_name, l_name, dob, course, duration)
    return student_info

# calling functions
welcome_screen()
