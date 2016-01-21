# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
print 'hello world I am happy but tired'
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
#This is what I did on the 20th PM
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
myage = 39
mylist = ['hello', 'is it me', "you're looking for"]
mynumlist = [1, 4, 9, 16]
listlength = len(mylist)
numlistlength = len(mynumlist)
print myvar
print myage
print mylist
print mynumlist
print listlength
print numlistlength
# urltoscrape = urltoscrape+"p1"
# print urltoscrape
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
