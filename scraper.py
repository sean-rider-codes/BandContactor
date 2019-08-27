import bs4 as bs
import urllib.request

address = "http://concertcalendarusa.com/saint-louis-concert-schedule"

sauce = urllib.request.urlopen(address).read()

soup = bs.BeautifulSoup(sauce, 'html5')

table = soup.find('table')

table_rows = table.find_all('tr')

Output_File = open(r"Site_Output.txt","w")

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td] 
    Output_File.write(str(row))

Output_File.close()