"""
Functionalities for managing an institution's inventory:
F1. Adding an object
F2. Deleting an object
F3. Modifying an object based on inventory number/ID
F4. Moving all objects from one room to another
F5. Concatenation of a read call to all item descriptions with a higher price than a read value
F6. Determining the highest price for each location
F7. Ordering objects in ascending order according to the purchase price
F8. Display of price amounts for each location
F9. Undo

Running scenario for F1:
# | User             | Program             | Comment
----------------------------------------------------------------------------------------
1  |                 | <main menu>         |
2  | 1               |                     | The user chooses add
3  |                 | Name data:          | The program asks for the name of the object
4  | Manual          |                     | The user gives the name: Manual
5  |                 | Description data:   | The program asks for the description of the object
6  | Informatics     |                     | The user gives the description of the object: Informatica
7  |                 | Price data:         | The program asks for the price of the object
8  | 25              |                     | The user gives the price of the object: 25
9  |                 | Location data:      | The program asks for the location of the object
10 | Hall A          |                     | The user gives the location: Hall A
  |                  | Book added!         |
-------------------------------------------------------------------------------------------

Running scenario for F2:
# | User             | Program                | Comment
----------------------------------------------------------------------------------------
1  |                 | <main menu>         |
2  | 2               |                     | The user chooses delete
3  |                 | Name data:          | The program asks for the name of the object to be deleted
4  | Collection      |                     | The user gives the name: Collection
5  |                 |                     | The program searches for the object to be deleted
  |                  | Collection deleted! |
-----------------------------------------------

Running scenario for F3:
# | User             | Program            | Comment
----------------------------------------------------------------------------------------
1  |                 | <main menu> |
2  | 3               |                    | The user chooses update
3  |                 | ID data:           | The program asks for the ID of the object to be modified
4  | 14              |                    | The user gives the ID: 14
5  |                 | Name data:         | The program asks for the name of the new object
6  | Dictionary      |                    | The user gives the name: Dictionary
7  |                 | Description data:  | The program asks for the description of the new object
8  | Romanian-English|                    | The user gives the description of the object: Romanian-English
9  |                 | Price data:        | The program asks for the price of the new object
10 | 20              |                    | The user gives the price of the object: 20
9  |                 | Location data      | The program asks for the location of the new object
10 | Hall H          |                    | The user gives the location: Sala H
11 |                 |                    |
5  |                 |                    | The program searches for the given ID
  |                  | Modified object    |
-------------------------------------------------------------------------------------------

Running scenario for F4:
# | User             | Program            | Comment
--------------------------------------------------------------------------------------------
1  |                 | <main menu>        |
2  | 4               |                    | The user chooses to move all objects from one room to another
3  |                 | Location data:     | The program asks for the initial location of the objects
4  | Hall C1         |                    | The user gives the location: C1
5  |                 | Location data:     | The program asks for the final location of the objects
6  | Hall C19        |                    | The user gives the location: C19
7  |                 |                    | The program searches for the given location
8  |                 | Objects moved      |
--------------------------------------------------------------------------------------------

Running scenario for F5:
# | User             | Program            | Comment
--------------------------------------------------------------------------------------------
1  |                 | <main menu>        |
2  | 5               |                    | The user chooses to concatenate a read cry to all object descriptions with
                                          | a price higher than a read value
3  |                 | Limit price data:  | The program asks for the limit price
4  | 65              |                    | The user gives the price: 65
5  |                 | string data:       | The program asks for the string
6  | Maximum         |                    | The user gives the string: Maxim
7  |                 |                    | The program searches
  |                  | String added!      |
--------------------------------------------------------------------------------------------

Running scenario for F6:
# | User             | Program            | Comment
------------------------------------------------
1  |                 | <main menu>        |
2  | 6               |                    | Determining the highest price for each location
3  |                 |Price,location data:| The program determines the price and location for each object; if the
                                          | price does not exist in the location, then it is added
   |                  |                   | The program searches
   |                  | Successful!       |
--------------------------------------------------------------------------------------------

Running scenario for F7:
# | User             | Program            | Comment
--------------------------------------------------------------------------------------------
1  |                 | <main menu>        |
2  | 7               |                    | Ordering objects in ascending order according to the purchase price
3  |                 |                    | The program sorts all the prices
   |                 | Successful!        |
--------------------------------------------------------------------------------------------

Running scenario for F8:
# | User             | Program            | Comment
--------------------------------------------------------------------------------------------
1  |                 | <main menu>        |
2  | 8               |                    | Display of price amounts for each location
3  |                 |Price,location data:| The program determines the price and location for each object;
                                          | if there is no amount in the location, then the amount will be zero
                                          | otherwise, the sum of all prices is calculated
4 |                  |                    | The program is looking
  |                  | Successful display |
--------------------------------------------------------------------------------------------

Running scenario for F9:
# | User             | Program             | Comment
--------------------------------------------------------------------------------------------
1  |                 | <main menu>         |
2  | 9               |                     | Undo

   |                 | Undo object!         |
--------------------------------------------------------------------------------------------

Activities for F1:
1. Representation of the inventory as a dictionary
2. Reading data for an inventory
3. Adding an inventory to the collection of inventories
4. Completing the user interface

Activities for F2:
1. Choosing the object to be deleted
2. Search for the object to be deleted in the name collection
3. Deleting an object from the inventory collection
4. Completing the user interface

Activities for F3:
1. Choosing the ID of the object to be modified
2. Adding a new dictionary
3. Modification of the object
4. Completing the user interface

Activities for F4:
1. Choosing the object to be moved
2. Adding the new location of the object e
3. Moving the object
4. Completing the user interface

Activities for F5:
1. Adding a value and a given string
2. Determination of the highest price
3. Adding the string to the description of the object with the highest price
4. Completing the user interface

Activities for F6:
1. Grouping of prices by location
2. Determination of the highest price for
3. Returning the highest price for each location
4. Completing the user interface

Activities for F7:
1. Ordering objects in ascending order according to the purchase price
2. Completing the user interface

Activities for F8:
1. Grouping of prices by locations
2. Calculation of each sum of prices
3. Returning price sums for each location
4. Completing the user interface

Activities for F9:

4. Completing the user interface

"""

