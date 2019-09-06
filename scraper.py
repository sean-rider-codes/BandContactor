import tkinter
import os
import pandas as pd
import requests
from lxml import html
import smtplib

#GUI
window = tkinter.Tk()
window.title("Set Up")
tkinter.Label(window, text = "                                  Email Bands                                 ").pack()
window.mainloop()

#building directory and filename for file we will write to
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'ScriptOutput.txt')

#url for concert website, change to reflect your city/state
address = "http://concertcalendarusa.com/saint-louis-concert-schedule"
print("\nQuerying " + address +"...")

#Create DataFrame from HTML table using Pandas, trim city and link columns
print("Importing table...")
df = pd.read_html(address)[0]

print("Formatting table...")
trimDF = df.drop([df.columns[3], df.columns[4]], axis='columns')

#set max number of rows so all entries are shown
pd.set_option('display.max_rows', 300)

#set max width so long names are not truncated
pd.set_option('display.max_colwidth', -1)

#write table rows to text file
print("Writing to " + filename)

Output_File = open(filename,"w")
trimDF.to_string(Output_File)
Output_File.close()

print("File has been updated")

#Booking Agent Info Section
payload = {
    "username": "seanriderphoto",
    "password": "BAIPassword1234"
}