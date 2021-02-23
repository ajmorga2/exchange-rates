from tkinter import *
import requests

#API Workings

#Get data from website
r = requests.get("https://api.currencyfreaks.com/latest?apikey=522701cf666047b89a423f98229f2f10")

#convert data into json format
currencies = r.json()

#Create list for 3 letter currency identifiers e.g 'USD'
currencyList = []

#add identifiers from api databse to list called 'currencies'
#print it out for testing purposes
for currency in currencies['rates']:
    currencyList.append(currency)



#Creation of GUI using tkinter module

#Main window
root = Tk()

#Change background color of GUI widow using hex codes
root['bg'] = "#C6DDF0"

#Title
mainTitle = Label(root, text="Welcome to Real Time Currency Coverter", bg="#996888", fg="#C6DDF0")


#String Variable for left and right dropdowns
variable1 = StringVar(root)
variable2 = StringVar(root)

#setting default currency to USD
variable1.set(currencyList[67])
variable2.set(currencyList[67])


#Drop Down List for left and Right
leftDropDown = OptionMenu(root, variable1, *currencyList)
rightDropDown = OptionMenu(root, variable2, *currencyList)

convertButton = Button(root, text='Covert', command=converter)
convertButton.grid(row=2, column =3)


#Placing the elements on the screen
mainTitle.grid(row=0, column=2, columnspan=4)
leftDropDown.grid(row=1, column=0)
rightDropDown.grid(row=1,column=3)


root.mainloop()

#example to add countries to dropdown on left
#same logic can be applied to dropdown menue on the right

#for country in countries:
    #leftDropDown.insert(f'{country}')

def converter():
    
    #api key in variable
    apiKey = '522701cf666047b89a423f98229f2f10'
    #get the value in the leftDrop
    base = variable1.get()
    currency2 = variable2.get()
    
    r = requests.get(f"https://api.currencyfreaks.com/latest?apikey={apiKey}&symbols={currency2}&base={base}")
    results = r.json()
    date = results['date']
    conversion = results['rates'][f'{currency2}']
    
    #string variables for 'dateLabel' and 'coversionLabel' 
    v1 = StringVar()
    v2 = StringVar()
      
    dateLabel = Label(root, text= f'Date:{date}')
    conversionLabel = Label(root, text=f'1{base} = {conversion} {currency2}')
    
    dateLabel.grid(row=3,column=0)
    conversionLabel.grid(row=4, column=0)