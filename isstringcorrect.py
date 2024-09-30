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

def correct(start):
#finds correct next value using integers
    start = str(start)
    count = 0
    new_int = ""
   #while statement hasn't been fully checked
    while count < len(start):
      #if the number being checked != the second number
        if start[count] != start[count+1]:
            #the new integer gets a 1 + # added to the sequence
            new_int = "1" + start[count]
        #if the number being checked == the second number
            count = count +1
        else:
            #count how many times that number pops up (count)
            repet = 1
            if start[count] == start[count+2]:
                repet = 2
            if start [count == start[count+3]]:
                repet = 3
            else:
                repet = "CHECK ME"
            #the new integer gets a (count) + whatever number we were counting added to the sequence
            new_int = str(repet) + start [count+repet]
            count = count +1
        
    #return checked statement  
    return new_int


def main():
#runs the functions
    start = 1
    user_input()
    print(correct(start))


if __name__ == "__main__":
    main()
    