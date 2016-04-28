import csv
from lxml import html
import requests
import re
import smtplib
import time


#Gathering the text from the webpage
page = requests.get('http://www.nco.ncep.noaa.gov/pmb/nwprod/thanks/index.thankusa.php')
tree = html.fromstring(page.content)
test = tree.xpath('/html/body/table[5]/tbody/tr[1]/td[2]/font/pre')
contents = test[0].text_content()



#Removing the stuff we don't want
rawlist = "".join(contents.splitlines(True)[6:][:16])
#print(rawlist)


#f = open("Resources/Rawlist.txt", "r")
#rawlist = f.read()
#print(rawlist)

rawlist = rawlist.replace('     ',' Nodata')

#splitting the strings into a list by every space
results = re.split('\s', rawlist)
#print(results)


#handling the space in the instance of "A C" for a site
z=1
x=0
for i in range(len(results)):
    if results[i]==('C' or 'c'):
        z=z+1

for i in range(len(results) - z):
    
    if results[i+1] == ('C' or 'c'):
        #print(results[i+1])
        #print(results[i:i+2])
        results[i:i+2] = [''.join(results[i:i+2])]
        #print(results)

#print(results)
#removing empty objects in our results list
results = list(filter(None, results))
      
#Defining some functions to gather every odd and every even object in the lists
def getsites(b):
    return b[::2]
def getthnks(c):
    del  c[0]
    return c[::2]

# Using our newly created functions
sitelist = getsites(results)
thnkslist = getthnks(results)

#print(thnkslist)

goodsites = sitelist
badsites = []

#for i in range(len(sitelist)):
    #if thnkslist[i] != 'THKS':
        #print(sitelist[i] + " reported " + thnkslist[i])


sitelistnames = sitelist

sitenames=['Barrow, AK','Kotzebue, AK','Nome, AK','Bethel, AK','McGrath, AK','Fairbanks, AK',
           'Anchorage, AK','St Paul Island, AK','Cold Bay, AK','King Salmon, AK','Kodiak, AK',
           'Yakutat, AK','Anneette, AK','Key West, FL','Miami, Fl','Jacksonville, FL','Charleston, SC',
           'Tampa Bay, Fl','Tallahassee, Fl','Peachtree City, GA','Birmingham, Al','Slidell, La',
           'Jackson, MI','lake Charles, La','Shreveport, La','Fort Worth, TX','Brownsville, TX',
           'Corpus Christi, TX','Del Rio, TX','Midland, TX','Tucson, AZ','San Diego, CA','Newport, NC',
           'Greensboro, NC','Blackburg, VA','Nashville, TN','Little Rock, AR','Norman, OK','Amarillo,TX',
           'Santa Teresa, NM','Albuquerque, NM','Flagstaff, AZ','????','Wallops Island, VA','Sterling, VA',
           'Wilmington, OH','Springfield, MO','Dodge City, KS','Topeka, KS','Denver, CO','Grand Junction, CO',
           'Reno, NV','Oakland, CA','Upton, NY','Albany, NY','Pittsburgh,PA','Buffalo, NY',
           'Valley, NE','North Platte, NE','Salt Lake City, UT','Elko, NV','Medford, OR',
           'White Lake, MI','Gaylord, MI','Green Bay, WI','Chanhassen, MN','Aberdeen, SD',
           'Rapid City, SD','Riverton, WY','Boise ID','Salem, OR','Caribou, ME','Intl, Falls, MN',
           'Bismark, ND','Glasgow, MT','Great Falls, MT','Spokane, WA','Quillayute, WA',
           'Gray, ME','Quad City, IA','Chatham, MA','Lincon, IL','San Juan',
           'Lihue, HI','Guam','Hilo, HI','Chuuk','PohnPei','Majuro','Koror, Palau','Yap, Coraline Islands',
           'Pago Pago Pago Pago']

Emailstring = []

for i in range(len(sitenames)):
    if thnkslist[i] != 'THKS':
        Emailstring.append(sitenames[i] + "(" + sitelist[i] + ")" + " reported " + thnkslist[i])

Emailstring = '\n'.join(Emailstring)


def getsitenames():
    return sitenames
def getthnkslist():
    return thnkslist
def getemailstring():
    return Emailstring
    
    
