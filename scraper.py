#This is what I did on the 20th PM
#
print 'hello world I am happy but tired'
urltoscrape = "www.bbc.co.uk/cricket/"
print urltoscrape
My_age = 39
print My_age
listylist = ["p1","p2","p3"]
for blah in listylist:
  print blah
  fullurl = urltoscrape+blah
  print fullurl

#This is what I did on the 21st AM
myvar = "He is a potato head"
print myvar
myage = 39
print myage
mylist = ['hello', 'is it me', "you're looking for"]
print mylist
listlength = len(mylist)
print listlength
# The next two lines are the same as the two above this.  It does not matter what the 'blah' bit reads as.  This only prints out once in the list.
blah = len(mylist)
print blah
mynumlist = [1, 4, 9, 16]
print mynumlist
numlistlength = len(mynumlist)
print numlistlength
stringlength = len(myvar)
print stringlength
# the line below says find the 1 character i.e. second character as the first would be zero
# secondchar = mylist(1) - there is an error here so check Paul's slides
# numlistlength = len(myage) - this does not work because it is an integer.  It creates an error.
# print numlistlength
#
#
#
# Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
