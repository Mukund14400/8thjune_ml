
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

import pandas as pd
m = pd.read_pickle('house_price_predictor.pkl')

import warnings
warnings.filterwarnings('ignore')
In [5]:
app = tk.Tk()
app.geometry('800x500')
app.title('House Price Predictor')


v_age = tk.StringVar(app)
v_income = tk.StringVar(app)
v_pop = tk.StringVar(app)
v_room = tk.StringVar(app)
res = tk.Variable(app)



image = Image.open("3.jpg")

resize_image = image.resize((800, 500))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img)
label1.image = img
label1.pack()

def houseprice():
    inc=eval(entry_inc.get())
    Age=eval(entry_age.get())
    Room=eval(entry_room.get())
    pop=eval(entry_pop.get())
    query=pd.DataFrame({'Income':[inc],'House_age':[Age],'Rooms':[Room],'Population':[pop]})
    result.set(round(m.predict(query)[0],2))
    


label=tk.Variable(app)
tk.Label(app,textvariable=label,font=('Courier',15),fg='blue').pack()



income=tk.Variable(app)
income.set('Enter your income: ')
tk.Label(app,textvariable=income,font=0).place(x=100,y=60)

age=tk.Variable(app)
age.set('Enter the age of House: ')
tk.Label(app,textvariable=age,font=0).place(x=100,y=100)

room=tk.Variable(app)
room.set('Enter the number of rooms: ')
tk.Label(app,textvariable=room,font=0).place(x=100,y=140)

population=tk.Variable(app)
population.set('Enter the population in the area: ')
tk.Label(app,textvariable=population,font=0).place(x=100,y=180)

entry_inc=tk.Variable(app)
entry_inc.set('0')
tk.Entry(app,textvariable=entry_inc).place(x=500,y=60,height=20)

entry_age=tk.Variable(app)
entry_age.set('0')
tk.Entry(app,textvariable=entry_age).place(x=500,y=100,height=20)

entry_room=tk.Variable(app)
entry_room.set('0')
tk.Entry(app,textvariable=entry_room).place(x=500,y=140,height=20)

entry_pop=tk.Variable(app)
entry_pop.set('0')
tk.Entry(app,textvariable=entry_pop).place(x=500,y=180,height=20)

tk.Button(app,text='Show price of houses available',command=houseprice,bg='red',fg='white',font=0).place(x=250,y=280,height=40)

pricepred=tk.Variable(app)
pricepred.set('The predicted price of your house in $: ')
tk.Label(app,textvariable=pricepred,font=0).place(x=100,y=400)

result=tk.Variable(app)
result.set('')
tk.Label(app,textvariable=result,font=0).place(x=520,y=400)

app.mainloop()

