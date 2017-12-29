# Modify it to make it find the names of all the animals that are not gorillas and not named 'Max'.
SELECT name 
FROM animals 
WHERE species != 'gorilla' AND name != 'Max'

# Find all the llamas born between January 1, 1995 and December 31, 1998.
SELECT name, species, birthdate
FROM animals
WHERE species = 'llama'
    AND (birthdate >= '1995-01-01' AND birthdate <= '1998-12-31')

# Write a query that returns all the species in the zoo, and how many animals of each species there are, sorted with the most populous species at the top. The result should have two columns:  species and number.
SELECT species, count(*) as number
FROM animals
GROUP BY species
ORDER BY number DESC

# Insert a newborn baby opossum into the animals table and verify that it's been added.
# SELECT_QUERY should find the names and birthdates of all opossums.
# INSERT_QUERY should add a new opossum to the table
#SELECT_QUERY
SELECT name, birthdate FROM animals WHERE species = 'opossum';
#INSERT_QUERY
INSERT INTO animals (name, species, birthdate) values('Jerry', 'opossum', '2017-05-15');

# Find the names of the individual animals that eat fish.
SELECT animals.name, diet.food
FROM animals, diet
WHERE animals.species = diet.species
AND diet.food = 'fish'

# Find the one food that is eaten by only one animal.
SELECT animals.name, animals.species, diet.food, count (*) as diff_foods
FROM animals, diet
WHERE animals.species = diet.species
GROUP BY diet.food
HAVING diff_foods=1

# List all the taxonomic orders, using their common names, sorted by the number of animals of that order that the zoo has.
# The animals table has (name, species, birthdate) for each individual.
# The taxonomy table has (name, species, genus, family, t_order) for each species.
# The ordernames table has (t_order, name) for each order.
SELECT ordernames.name, count(*) as quantity
FROM animals, taxonomy, ordernames
WHERE animals.species = taxonomy.name AND taxonomy.t_order = ordernames.t_order
GROUP BY ordernames.t_order
ORDER BY quantity DESC