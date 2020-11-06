# Assignment 3b:
    - Invitation Link : https://github.com/2020202014Geeta/2020202014_Assignment3a/invitations
	- Repository Link : https://github.com/2020202014Geeta/2020202014_Assignment3a.git
### Que 1:
    - First json package is imported in the program to work with JSON data.
    - First org.json file is accessed, and its content is loaded in a var called tree.
    - The input is assumed to be space separted.
    -  Ex : 
       If inputs were:              
       2 003 004

       Output will be:
       001
       001 is 1 levels above 003
	   001 is 2 levels above 004

    - Inputs are taken from the user, and parent of these inputs is checked.
    - searchParent: Stores the employee Ids entered by the user.
      levelList: Stores level of the employees
      levelLeader: Stores level of the leader
      fun1(leader): finds the level of the leader.
      parentList : Stores all the employees which occur on the path from root (level 0) to 
      that employee, for each employee.
    - Then makeParentList function is called for all the the employees
      - This function takes the input in a variable called toFind and searches its parent starting from the last level up to the first level, since parent will always be atleast one level up.
      - Whenever we find a parent we append in the parentList, and update toFind variable to that parent, since we need to search all the parents
      - Then we search for the common parent, i.e. the leader
      - And then using fun1(leader): we find the level of the leader, and print the output on the screen.
      - 
NOTE: Minor changes have been made to make the code generic:
    - changes from 3a:
        - How we are taking Input- Line 6 to 13
        - fun1(leader): function added to find level of the leader- Line 39 to 44.
        - How to find leader- Line 58 to 68:
-Example: parentList:  [['B', 'A', 'X'], ['A', 'X'], ['C', 'B', 'A', 'X']]
We will ignore the first element of each sublist
We will start from the second element of the first list till the end (here A and X), and search them in all the sublists, if the total count of there occurences matches with totalEmployee whose parent are asked -1, then its our leader.


### Que 2:
    - The Assignment-3a which assumed the date in input file to be in the following format:
       10th September, 2020 , DD/MM/YYYY , DD-MM-YYYY , DD.MM.YYYY , 10th Sep, 2020
       Ex : Date1: 25/08/2019
            Date2: 01/03/2020
    have been modified and made generic.
    
  - Major Assumptions: 
    - It is assumed that the user will enter it in the command line, whether the data in the date_calculator.txt is dd/mm/yyyy or mm/dd/yyyy 
    - The date inside date_calculator.txt could be anything,
                                   Eg: Date1: 10/09/2020
                                       Date2: 11th September, 2020
   But both of them will be either mm/dd/yyyy or dd/mm/yyyy

- To run Use: python3 q2.py dd/mm/yyyy 
     or      python3 q2.py mm/dd/yyyy
- Concept Used:
    - First the dates are converted to dd/mm/yyyy or mm/dd/yyyy format, then the 2 dates are stored in 2 strings: date1, date2
    - Then using split("/"), each date is broken, and given to dd1,dd2- for DD, mm1,mm2- for months, and yy1,yy2 for year
    
    - addLeapDays(yy1,yy2) - 
        A (user defined) function was made,and called to check if there exists a leap year
        between the 2 given year, if found 366 is added to the number of days in the function else 365 is added.
        This way the function returns total no.of days in between these 2 years, and the returned value is stored in leapDays
        
    - daysInY1(mm1,mm2,yy1,yy2) - 
        A (user defined) function was made,and called to find the number of days in yy1 year after mm1.
        Also, if mm1 was not a leap year, then 1 is subtracted from oddDays.
        The function returns oddDays + daysAftrM1, and the returned value is stored in daysInYear1
        
    - daysInY2(mm1,mm2,yy1,yy2) - 
        A (user defined) function was made,and called to find the number of days in yy2 year before mm2.
        The function returns oddDays + daysAftrM1,  and the returned value is stored in daysInYear2
    
    - There will be 3 cases:
      - Both the months are same
      - Both the year are same
      - Both the days are same
    
    Finally the total no.of days are stored in 
    days= daysInYear1 + daysInY12 + leapDays + daysInYear2
    and this is saved in a file called Output.txt
    Ex : Date Difference: 10 Days
    
NOTE: Minor changes have been made to make the code generic:
- changes from 3a:
    - Line no: 1
        - from sys import argv used for command line arguments
        - userDateForm = argv[1]            ( In line 71)
    - Line no: 3
        - The dictionary which was delared locally to find month ( Eg: Jan: 1, Feb: 2, etc.), has now been declared globally, so that we can compare it use it for both the formats:
        dd/mm/yyyy and mm/dd/yyyy 
    - Line no: 66 to 113:
        - Is same as line-64 to 87 of Assignment-3a, but with the change that now it will first check whether the user entered mm/dd/yyyy or dd/mm/yyyy

### Que 3:
- Assumptions:
    - Folder name is employee and files name are Example: Employee1.txt etc
    - It is assumed that we are checking the common free slot of employees for the same date,
      hence, it is assumed that both the files have data of the same date.
	- The input is assumed to be single digit for numbers like 9,1,2,3,4,5. Ex : 9:00AM
    - Example of Input file format:
      {'Employee1': {'5/10/2020':['10:00AM - 11:00AM', '12:30PM - 1:00PM', '4:00PM - 5:00PM']}}
    -Note: If no common free slot is available, then "no slot available" is stored in the file (without quotes)
    
Example :
Available slot
Employee1: ['9:00AM - 10:00AM', '11:00PM - 12:30PM', '1:00PM - 4:00PM']
Employee2: ['9:00AM - 10:30AM', '11:30PM - 12:00PM', '1:30PM - 3:30PM', '4:30PM - 5:00PM']

Slot Duration: 2.5 hour
no slot available
    
    - First the details of employee busy slot is separated from their repective name and date using split function.
    The name is stored in empName1, empName2, and date
    - Then fillFreeSlots function is called, which converts the time in minutes and finds 
      free slots in both the employee is filled in the following lists: 
      freeStE1- for starting time of free slot of employee of all the employees
      freeEndE1- for ending time of free slot of employee of all the employees
    
    - Then mergeInterval function is called which workes on the merge algorithm of merge sort, 
     and finds all the common free slots of both the employees, and is stored in the lists:
     interValS- for starting time of common free slots
     interValE- for ending time of common free slots
    
    - Input is taken from the user, and is checked against the common slots of the employees
    - Later the time is converted back to original time given in the input file
    - Available slots of both the employees and the common slot is saved in a file called Output.txt.

Example: 
Available slot
Employee1: ['9:00AM - 10:00AM', '11:00PM - 12:30PM', '1:00PM - 4:00PM']
Employee2: ['9:00AM - 10:30AM', '11:30PM - 12:00PM', '1:30PM - 3:30PM', '4:30PM - 5:00PM']

Slot Duration: 0.5 hour
{'5/10/2020' : ['9:00AM - 9:30AM']}

NOTE:
No new functions are added.
Minor changes have been made to make the code generic:
- changes from 3a:
    - Line no: 117 to 147: Minor changes like instead of 2 employees, information of all the employees are added- to make it generic.
    
      


