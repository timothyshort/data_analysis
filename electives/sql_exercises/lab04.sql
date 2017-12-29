# This query is intended to find pairs of roommates.  It almost works!
# There's something not quite right about it, though.  Find and fix the bug.
select a.id, b.id, a.building, a.room
       from residences as a, residences as b
 where a.building = b.building
   and a.room = b.room
   and a.id != b.id
 group by a.room
 order by a.building, a.room;
 
# The query below is intended to count the number of bugs in each program. But it doesn't return a row for any program that has zero bugs.  Try running it as it is; then change it so that it includes rows for the programs with no bugs.
select programs.name, count(bugs.id) as num
   from programs left join bugs
        on programs.filename = bugs.filename
   group by programs.name
   order by num;
  
  
# Modify the Python code so that the student records are fetched in sorted order by student's name.
import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0], " | ", row[1]

db.close()


# This code attempts to insert a new row into the database, but doesn't commit the insertion.  Add a commit call in the right place to make it work properly.
import sqlite3
db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()


# The function below performs two database queries in order to find the right players.
# Refactor this code so that it performs only one query.
def lightweights(cursor):
    query = "select name, weight \
                from players, \
                    (select avg(weight) as avg_weight from players) as weights \
                where weight < avg_weight;"
    
    """Returns a list of the players in the db whose weight is less than the average."""
    #cursor.execute("select avg(weight) as av from players;")
    #av = cursor.fetchall()[0][0]  # first column of first (and only) row
    #cursor.execute("select name, weight from players where weight < " + str(av))
    cursor.execute(query)
    return cursor.fetchall()
