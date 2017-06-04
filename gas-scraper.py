# coding: utf-8

# In[4]:

from bs4 import BeautifulSoup
import urllib.request
import time
import random


# In[39]:

def double_quote(word):
    double_q = '"' # double quote
    return double_q + word + double_q


# In[44]:

tld = "https://www.gasbuddy.com/Station/"
matches_path = "gas_station_data.txt"


# In[45]:

for i in range(1, 100000):
    try:
        time.sleep(random.random()) # rate limiting prevention
        with urllib.request.urlopen(tld + str(i)) as url:
            r = url.read()
        soup = BeautifulSoup(r, "html.parser")
        name = soup.find_all("h2", class_="station-name")
        amenities = soup.find_all("div", class_="station-feature")
        address = soup.find("div", class_="station-address")
        city = soup.find("span", itemprop="addressLocality")
        state = soup.find("span", itemprop="addressRegion")
        zipcode = soup.find("span", itemprop="postalCode")
        if len(name) == 0:
            print("Site did not have a Station %d", i)
        else:
            name = name[0].text.strip()
            address, city, state, zipcode = address.text, city.text, state.text, zipcode.text
            amenities = list(map(lambda x: x.get('title'), amenities))
            result = ",".join(map(double_quote, [str(i), name, address, city, state, zipcode]))
            result += "," + str(amenities)
            with open(matches_path, "a") as myfile:
                myfile.write(result + '\n')
            print(result)
    except:
        print("Error processing Station %d", i)

