import bs4 as bs
import pandas as pd
import urllib.request
import os

nl = "\n"

#building directory and filename for file we will write to
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'ScriptOutput.txt')

#url for concert website, change to reflect your city/state
address = "http://concertcalendarusa.com/saint-louis-concert-schedule"
print(nl + "Querying " + address)

#use beautiful soup to open website and pull table rows from the html
sauce = urllib.request.urlopen(address).read()

soup = bs.BeautifulSoup(sauce, 'html5lib')

table = soup.find('tbody')

table_rows = table.find_all('tr')

#write table rows to text file
print("Writing to " + filename)

Output_File = open(filename,"w")



for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td] 
    Output_File.write(str(row) + nl)
#Output_File.write("\n")

Output_File.close()

print("Closing " + filename + nl)