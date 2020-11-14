# Assignment 3c:
    - Invitation Link : https://github.com/2020202014Geeta/2020202014_Assignment3a/invitations
	- Repository Link : https://github.com/2020202014Geeta/2020202014_Assignment3a.git
### Que 1:
NOTE: Minor changes have been made to make the code generic:
    - changes from 3a:
        - How we are taking Input- Line 6 to 13
        - fun1(leader): function added to find level of the leader- Line 39 to 44.
        - How to find leader- Line 58 to 68:
-Example: parentList:  [['B', 'A', 'X'], ['A', 'X'], ['C', 'B', 'A', 'X']]
We will ignore the first element of each sublist
We will start from the second element of the first list till the end (here A and X), and search them in all the sublists, if the total count of there occurences matches with totalEmployee whose parent are asked -1, then its our leader.


### Que 2:  
- No changes were made to the code. 
NOTE: The overall complexity of q2.py of Assignment-3b
     ![Final Complexity Grade Q3 screenshot](https://github.com/2020202014Geeta/2020202014_Assignment3a/blob/PartC/q3_Cyclo.PNG)
    - Line no: 1
        - from sys import argv used for command line arguments
        - userDateForm = argv[1]            ( In line 71)
    - Line no: 3
        - The dictionary which was delared locally to find month ( Eg: Jan: 1, Feb: 2, etc.), has now been declared globally, so that we can compare it use it for both the formats:
        dd/mm/yyyy and mm/dd/yyyy 
    - Line no: 66 to 113:
        - Is same as line-64 to 87 of Assignment-3a, but with the change that now it will first check whether the user entered mm/dd/yyyy or dd/mm/yyyy

### Que 3:
- No changes were made to the code.
 ![Final Complexity Grade Q3 screenshot](https://github.com/2020202014Geeta/2020202014_Assignment3a/blob/PartC/q3_Cyclo.PNG)
    
      


