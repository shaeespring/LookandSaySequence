"""
This function should take user inputs for as long as the user continues to input correct lines.

Author: Shaela Spring
"""

def correct():
    #this should check if the user input is correct
 ...
""" CORRECT ANSWERS:
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
continue
"""

def user_input():
#receives/returns user input
    user_input = int(input("Enter Number:"))
    return user_input


def main():
#runs the functions
    user_input()
    correct(user_input())


if __name__ == "__main__":
    main()
    