# Assignment 3a:

### Que 1:
    - First json package is imported in the program to work with JSON data.
    - First org.json file is accessed, and its content is loaded in a var called tree.
    - 2 inputs are taken from the user, and parent of these 2 inputs is checked.
    - parentList1, parentList2 : Stores all the employees which occur on the path from root 
      (level 0) to that employee
    - Then makeParentList function is called for both the employees
      - This function takes the input in a variable called toFind and searches its parent starting from the last level up to the first level, since parent will always be atleast one level up.
      - Whenever we find a parent we append in the parentList, and update toFind variable to that parent, since we need to search all the parents

      - Then we search for the common parent and print the output on the screen. 
	  
       Ex : 
       If inputs were:              
       003
       004
       Output will be:
       001
       001 is 1 levels above 003
	   001 is 2 levels above 004

### Que 2:
    - The date in input file is assumed to be in the following format:
       10th September, 2020 , DD/MM/YYYY , DD-MM-YYYY , DD.MM.YYYY , 10th Sep, 2020
       Ex : Date1: 25/08/2019
            Date2: 01/03/2020
    - First the dates are converted to DD/MM/YYYY format, then the 2 dates are stored in 2 
      strings: date1, date2
    - Then using split("/"), each date is broken, and given to dd1,dd2- for DD, mm1,mm2- for months, and yy1,yy2 for year
    
    - addLeapDays(yy1,yy2) - 
        A (user defined) function was made,and called to check if there exists a leap year
        between the 2 given year, if found 366 is added to the number of days in the function
        else 365 is added.
        This way the function returns total no.of days in between these 2 years, and the returned value is stored in leapDays
        
    - daysInY1(mm1,mm2,yy1,yy2) - 
        A (user defined) function was made,and called to find the number of days in yy1
        year after mm1.
        Also, if mm1 was not a leap year, then 1 is subtracted from oddDays.
        The function returns oddDays + daysAftrM1, and the returned value is stored in 
        daysInYear1
        
    - daysInY2(mm1,mm2,yy1,yy2) - 
        A (user defined) function was made,and called to find the number of days in yy2 
        year before mm2.
        The function returns oddDays + daysAftrM1,  and the returned value is stored in
        daysInYear2
    
    - There will be 3 cases:
      - Both the months are same
      - Both the year are same
      - Both the days are same
    
    Finally the total no.of days are stored in 
    days= daysInYear1 + daysInY12 + leapDays + daysInYear2
    and this is saved in a file called Output.txt
    Ex : Date Difference: 10 Days
      
### Que 3:
    - It is assumed that we are checking the common free slot of employees for the same date,
      hence, it is assumed that both the files have data of the same date.
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
      freeStE1- for starting time of free slot of employee1
      freeEndE1- for ending time of free slot of employee1
      freeStE2- for starting time of free slot of employee2
      freeEndE2- for ending time of free slot of employee2
    
    - Then mergeInterval function is called which workes on the merge algorithm of merge sort, 
     and finds all the common free slots of both the employees, and is stored in the lists:
     interValS- for starting time of common free slot
     interValE- for ending time of common free slot
    
    - Input is taken from the user, and is checked against the common slots of the employees
    - Later the time is converted back to original time given in the input file
    - Available slots of both the employees and the common slot is saved in a file called Output.txt.

Example: 
Available slot
Employee1: ['9:00AM - 10:00AM', '11:00PM - 12:30PM', '1:00PM - 4:00PM']
Employee2: ['9:00AM - 10:30AM', '11:30PM - 12:00PM', '1:30PM - 3:30PM', '4:30PM - 5:00PM']

Slot Duration: 0.5 hour
{'5/10/2020' : ['9:00AM - 9:30AM']}




