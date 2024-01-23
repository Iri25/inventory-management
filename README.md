# inventory-management

Python application with a 3-layered architecture: data access layer ([Domain](https://github.com/Iri25/inventory-management/blob/main/InventoryManagement/Domain.py)), business logic layer ([Logic](https://github.com/Iri25/inventory-management/blob/main/InventoryManagement/Logic.py)) and presentation layer ([User Interface](https://github.com/Iri25/inventory-management/blob/main/InventoryManagement/User%20Interface.py)). The data is saved in memory ([Objects](https://github.com/Iri25/inventory-management/blob/main/InventoryManagement/Objects.txt)). The planning of functions, scenarios, activities ([Iterations](https://github.com/Iri25/inventory-management/blob/main/InventoryManagement/Iterations.py)) and  tests for functionality ([Tests](https://github.com/Iri25/inventory-management/blob/main/InventoryManagement/Tests.py)) was carried out.

An application for managing an inventory in an institution. The following operations are supported:
1. Add/delete/modify object: it is done based on the number of inventory/ID. An object contains: ID, name, description (non-null), purchase price, location (4 characters).
2. Moving all objects from one hall to another.
3. Concatenation of a string read to all the descriptions of the objects with the higher price than a read value.
4. Determination of the highest price for each location.
5. Ordering objects in ascending order by purchase price.
6. Display of price amounts for each location.
7. Undo
