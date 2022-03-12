from tkinter import *
from tkinter import messagebox
import json
import os

LABEL_FONT = ("Verdana", 15, "normal")
INPUT_FONT = ("Verdana", 10, "normal")
BUTTON_FONT = ("Verdana", 12, "bold")
FONT_NAMES = ("Verdana", 15, "normal")
PASSWORD = '123456D'

win = Tk()
win.title("Zaph Market Secret Auction")
win.config(padx=30, pady=30, bg="#fff")
win.minsize(width=600, height=400)



label_name = Label(text="Your full name")
label_name.config(padx=5, pady=5, font=LABEL_FONT)
label_name.grid(column=0, row=1)
input_name = Entry()
input_name.grid(column=1, row=1, padx=10)
input_name.config(font=INPUT_FONT)

label_price = Label(text="Enter your price")
label_price.config(padx=5, pady=5, font=LABEL_FONT)
label_price.grid(column=2, row=1)
input_price = Spinbox(from_=1, to_=10000000000000000000000000)
input_price.grid(column=3, row=1, padx=10)
input_price.config(font=INPUT_FONT)

button_bid = Button(text="Bid")
button_bid.grid(column=4, row=1)
button_bid.config(width=5, height=1, font=BUTTON_FONT, bg="crimson", fg="white", border=0)

button_show_winner = Button(text="Show winner")
button_show_winner.grid(column=2, row=2)
button_show_winner.config(width=15, height=1, font=BUTTON_FONT, bg="crimson", fg="white", border=0, pady=10, bd=1)


bidders_names = []
def show_active_bidders():
    row = 3
    for name_index in range(len(bidders_names)):
        if name_index % 2 != 0:
            name_label = Label(text=f"{name_index+1}.{bidders_names[name_index]}", bg="crimson", fg="white", anchor="w", width=80)
        else:
            name_label = Label(text=f"{name_index+1}.{bidders_names[name_index]}",anchor="w", width=80)
        name_label.config(padx=10, pady=10, font=FONT_NAMES, border=0)
        name_label.grid(column=1, row=row, columnspan=3)
        row += 1
    
def capture_data():
    bidder_name = input_name.get()
    bidder_price = float(input_price.get())

    if bidder_name == "" or bidder_price == "" or type(bidder_price) != float:
        print(bidder_name, bidder_price)
        pass
    else:
        confirmation = messagebox.askyesno(title="Confirm bid", 
        message=f"Are you ok with the submission:{bidder_name} {bidder_price}\n")
        if confirmation == True:
            bid = {
                "name": bidder_name,
                "price": input_price.get()
            }
            bidder_name = bid["name"]
            bidder_price = bid["price"]
            bidders_names.append(bidder_name)

            try:
                with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(bid, data_file, indent=4)
            else:
                #Updating old data with new data
                data.update(bid)

                with open("data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)
        else:
            pass


def process_winner():
    print("we are in the process of processing winners")
    d = json.load(open("data.json"))
    print(d)
    print(d + {"name": "dennis", "price": 345})
        
    

button_bid.config(command=capture_data)
button_show_winner.config(command=process_winner)
win.mainloop()