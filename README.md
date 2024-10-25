#Student Grades Tracker
This Python program allows users to input student grades, classify them based on a grading scale, and calculate the average of all entered grades. The program keeps track of grades in a list and provides the average at the end.

#Features
Input Student Grades: Enter grades one by one.
Grade Classification: Automatically classifies grades into letter grades:
A for grades 90 and above.
B for grades between 75 and 89.
C for grades between 60 and 74.
F for grades below 60.
Calculate Average Grade: Computes the average of all entered grades.
Continue or Exit: After entering each grade, you can choose to continue or stop.
#How It Works
The program will prompt the user to input a student's grade.
It will classify the grade and store it in a list.
After each entry, the program will ask if you wish to continue entering grades.
If you choose to stop, the program will display all the entered grades and calculate the average.

#Example
bash
Copy code
Enter Grade: 85
B = 85
Do you wish to continue? (y/n: ) y
Enter Grade: 92
A = 92
Do you wish to continue? (y/n: ) n
[85, 92]
The avg is: 88.5
#Requirements
Python 3.x
