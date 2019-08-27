import bs4 as bs
import urllib.request

address = "http://concertcalendarusa.com/saint-louis-concert-schedule"

sauce = urllib.request.urlopen(address).read()

soup = bs.BeautifulSoup(sauce, 'html5')

print(soup)

print("Done printing " + address)

Output_File = open(r"Site_Output.txt","w")

Output_File.write(sauce.text)

Output_File.close()