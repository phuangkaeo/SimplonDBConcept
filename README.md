# SimplonDBConcept

# Introduction to Database Design

# A house and apartment rental agency wishes to manage its list of accommodation.
# She would indeed like to know the location of each dwelling (name of the town and district) as well as the people who occupy them (the signatories only). The rent depends on the accommodation, but depending on its type (house, studio, T1, T2 ...) the agency will always charge in addition to the rent the same lump sum to its customers. For example, the price of a studio will always be equal to the price of the rent + 30 DH of fixed charges per month. For each accommodation, we also want to have the address, the area as well as the rent. The agency would also like to know: The individuals who occupy the accommodation (the signatories of the contract only), we will be satisfied with their names, first names, date of birth and telephone number. For each municipality,

# Pedagogical modalities
# ++ Chapter 1: designing a database with UML and the PDM ++

# Part 1

# We will work from the openclassroom tutorial: https://openclassrooms.com/fr/courses/4055451-modelISE-et-implementez-une-base-de-donnees-relationnelle-avec-uml

# Read the very first chapter: “Understand objects and the relational model”

Part 2

Read Chapter 2: (Describe your functional area using the UML class diagram)

On draw.io represent the class diagram of the real estate agency including:

types
associations
Part 3

Read Chapters 3, 4 and 5 through (Modeling the Functional Area)

On draw.io represent the Physical Data Model (PDM) of the real estate agency including:

types
relationships
primary and foreign keys (if necessary)
Additional information to take into account: -The agency wishes to manage the history of occupancy of housing by individuals. It will also be considered that an individual can be a signatory to several rental contracts. -We also specify that a dwelling may be the subject of several separate rentals over time

Part 4

Read Chapter 6: Optimize your relational model with normal shapes

Check that your MDP respects the normal forms: For each normal form, find an example of a case that does not respect them (either what you did first, or invent it)

++ Chapter 2 Creating a database with MySQL ++

Part 1

In groups, from the openclassroom tutorial (https://openclassrooms.com/fr/courses/1959476-admintez-vos-bases-de-donnees-avec-mysql 1st part).

Your mission: -Understand what MySQL is (chapter 1)

Install MySQL (chapter 2)
Part 2:

Using chapter 3 (Distinguish between the different types of data) update the rental agency's PDM using the types specific to MySql

Part 3: Create the temp agency database on Mysql Use:

- chapters 4 and 5 of the first part - the primary key / foreign key chapter of the second.

Part 4:

Using the end of the first part of the tutorial: Insert 5 tuples for each table then display them (screenshot of a table) Modify one of the tuples for each table then display them (screenshot of a table) remove a tuple and display the result (screenshot)

If you have problems with foreign keys, this chapter should help you: https://openclassrooms.com/fr/courses/1959476-admintez-vos-bases-de-donnees-avec-mysql/1965264-options-des- foreign-keys

Part 5

Carry out the same thing but from python and using "MySQL Connector": -Create the database -Create the different Tables -Perform the CRUD queries -Insert 5 tuples for each table then display them (screenshot of a table) -Modify for each table one of the tuples then display them (screenshot of a table) -remove a tuple and display the result (screenshot)

tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp

Performance criteria
The class diagram and the PDM must respect the standards of use and correspond to the tables created The python code must work

Assessment methods
(exercise) Validate and return from the github repository.
