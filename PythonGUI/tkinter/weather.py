from tkinter import *
from PIL import ImageTk, Image
import requests 
import json

root = Tk()
root.title("Weather")

def ziplookup():
    zip.get()

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() +"&distance=25&API_KEY=0FD57A46-DBB2-4252-80B9-793EEA9E50F7")
        api =json.loads(api_request.content)
        city = text=api[0]["ReportingArea"]
        quality = text=api[0]["AQI"]
        category = text=api[0]["Category"]['Name']
        
        weather_color = "gray"
        
        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)
        
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
        myLabel.grid(row=1, column=0)
    except:
        api = "Error..."
    
zip = Entry(root)
zip.grid(row=0 , column=0, sticky=W+E+N+S)

zipButton =Button(root, text="Lookup zipcode", command=ziplookup)
zipButton.grid(row=0 , column=1)
    
    
root.mainloop()


