import pandas as pd
from datetime import*

x = datetime.now().hour + 10
y= datetime.date(datetime.now()).weekday()
z = datetime.now().minute
if x > 23:
  x -= 24
  y += 1
if y == 7:
  y = 0



#df = pd.read_csv("https://raw.githubusercontent.com/BrentV23/Brent-V-Data-Science/master/Restaurant_Data_New_New.csv")
df = pd.read_csv("https://raw.githubusercontent.com/BrentV23/Brent-V-Data-Science/master/Restaurant_Data_New_New.csv", parse_dates=[5,6,7,8,9,10,11,12,13,14,15,16,17,18])

cuisineValid = False
while cuisineValid == False:
  cuisine = input("Enter cuisine: ").lower()
  if cuisine == "western":
    cuisineValid = True
    cuisine = "Western"
  elif cuisine == "asian":
    cuisineValid = True
    cuisine = "Asian"
  else:
    cuisine = "Any"
    cuisineValid = True
  
    
deliveryValid = False
while deliveryValid == False:
  delivery = input("Delivery?: ").lower()
  if delivery == "yes" or delivery == "y":
    deliveryValid = True
    delivery = "Yes"
  elif delivery == "no" or delivery == "n":
    deliveryValid = True
    delivery = "No"
  

locationValid = False
while locationValid == False:
  location = input("Enter location: ").lower()
  if location == "belconnen":
    locationValid = True
    location = "Belconnen"
  elif location == "cbd":
    locationValid = True
    location = "CBD"
  elif location == "woden":
    locationValid = True
    location = "Woden"
  elif location == "gungahlin":
    locationValid = True
    location = "Gungahlin"
  else:
    location = "Any"
    locationValid = True

ratingValid = False
while ratingValid == False:
  rating = input("Any rating?: ").lower()
  if rating == "no" or rating == "n":
    ratingValid = True
    rating = "Yes"
  elif rating == "yes" or rating == "y":
    ratingValid = True
    rating = "No"

if y == 0:
  day = "Monday"
elif y== 1:
  day = "Tuesday"
elif y == 2:
  day = "Wednesday"
elif y == 3:
  day = "Thursday"
elif y == 4:
  day = "Friday"
elif y == 5:
  day = "Saturday"
elif y == 6:
  day = "Sunday"

Open = "Opening_" + day  
Close = "Closing_" + day

#test = "df." + Open
if delivery == "Yes":
  df = df[df.Delivery == delivery]

if cuisine == "Any":
  trash = 1
else:
  df = df[df.Cuisine == cuisine]
if rating == "Yes":
  df = df[df.Average_rating >= 4]

if location == "Any":
  ifthisisntherethenthisdoesntwork = 1
else:
  df[df.Location == location]

df[df[Open] <= str(datetime.now())]  
df[df[Close] >= str(datetime.now())]





