from re import I
import sys 

def file_reader(filename):
    contents =[] # store the contents of the file

    try: # try to open the file
        with open(filename) as f:
            for line in f:
                # if line is empty strip it
                if line.strip():
                    contents.append(line.strip())
    except FileNotFoundError: # if the file is not found
        print("File not found: ", filename)
        sys.exit()
    except: # if the file is not readable
        print("File is not readable: ", filename)
        sys.exit()
    return contents
file_reader("input1.txt")
#print(file_reader("input.txt"))
    
    # your file_reader() code ends above here

''' This is where each exam is graded.
It is similar to wk10 class, but there are differences.
Hint: be sure to strip \n off the answers.
Remember: You also need to account for the name.
'''
def grade_exam(exam):
    # sanitize your inputs
    

    # initialize some necessary variables
    score = 0
    wrong = []
    per_point = 10
    




    # your grade_exam() code ends above here


''' This is where you print out the result.
Look at the output examples above.
You do not need to return anything from this function.
'''
def print_grade(student, score, wrong):
    # sanitize your inputs
    print(f"{student} + received {score} and got {wrong} wrong.")



    # your print_grade() code ends above here
    print("\n")
'''
Get input from the user. Ask for a file name or q to quit (while loop).
If the user enters a file name (i.e. not 'q'), call file_reader(user_input) to open the file.
If file_reader() returns False, print contents to the screen and ask for input again.
If file_reader() returns True, do grade_multiple_students(contents)
Repeat until the user enters q to quit.
'''

def get_input():
    # No inputs were provided to this function sanitize :)
    # initialize user_input to empty string
    user_input = ''
    # your get_input() code starts below here
    while True: 
        print("Type in q to quit.")
        user_input = input("Enter a file name: ")
        if (user_input == 'q'):
           exit()
        else: 
            contents, value = file_reader(user_input) #contents = list
            print(value)
            if (file_reader):
                grade_multiple_students(contents)
            else:
                print(f"Here is {contents}.") # and ask again...
        
    # your get_input() code ends above here



#### DO NOT MAKE ANY EDITS BELOW HERE
#
#''' This funciton is done for you...Do NOT change it
#BUT look at "name" ...
#HINT: maybe you have to consider that in your code in grade_exam...
#'''
#def grade_multiple_students(file_contents):
#    if not isinstance(file_contents, list):
#        return None
#    # this processes all the rows from your file_contents (file_contents must be a list)
#    for row in file_contents:
#        items = list(row.split(',')) # gets one character
#        name = items[0] 
#
#        # grade each student's exam (items is a list)
#        result_tuple = grade_exam(items)
#
#        # this calls print_grade with the student's name (str), score (int), and wrong questions (list)
#        print_grade(name, result_tuple[0], result_tuple[1])
#
#
#def main():
#    continue_grading = get_input()
#    if not continue_grading:
#        print(f"\nHave a nice day!")
#
#if __name__ == "__main__":
#    main()