from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # To handle images
import requests

def data_get():
    city = city_name.get()
    # Fetch the data from the API
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2b7c042eff31fa4c5cf7278f80bfa5e1")
    
    # Convert the response to JSON
    data = response.json()
    
    # Update the labels with the data
    w1_label.config(text=data['weather'][0]['main'])
    wd2_label.config(text=data['weather'][0]['description'])
    temp1_label.config(text=str(data['main']['temp'] - 273.15))  # Convert from Kelvin to Celsius
    pressure1_label.config(text=data['main']['pressure'])

# Create the main windowfrom tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # To handle images
import requests

def data_get():
    city = city_name.get()
    # Fetch the data from the API
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2b7c042eff31fa4c5cf7278f80bfa5e1")
    
    # Convert the response to JSON
    data = response.json()
    
    # Update the labels with the data
    w1_label.config(text=data['weather'][0]['main'])
    wd2_label.config(text=data['weather'][0]['description'])
    temp1_label.config(text=str(data['main']['temp'] - 273.15))  # Convert from Kelvin to Celsius
    pressure1_label.config(text=data['main']['pressure'])

# Create the main window
win = Tk()
win.title("CLIMATECH")
win.geometry("600x650")

# Set the background image
bg_image = Image.open("clouds-sun-rays-sky.jpg")  # Ensure the image is in the same directory
bg_image = bg_image.resize((600, 650), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(win, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Set background image

# Add the logo
logo_image = Image.open("weather(1).png")  # Ensure the logo is in the same directory
logo_image = logo_image.resize((100, 100), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = Label(win, image=logo_photo, bg="light blue")
logo_label.place(x=250, y=10, width=100, height=100)

# Application title
name_label = Label(win, text="CLIMATECH", font=("Helvetica", 28, "bold"), fg="white", bg="#1e90ff")
name_label.place(x=100, y=120, height=50, width=400)

# Dropdown for city selection
city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
             "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
             "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli",
             "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("Helvetica", 16), textvariable=city_name)
com.place(x=100, y=200, height=40, width=400)

# Weather labels
w_label = Label(win, text="Weather Climate: ", font=("Helvetica", 15), fg="black", bg="#add8e6")
w_label.place(x=50, y=300, height=40, width=220)
w1_label = Label(win, text="", font=("Helvetica", 15), fg="black", bg="#add8e6")
w1_label.place(x=300, y=300, height=40, width=220)

wd_label = Label(win, text="Weather Description: ", font=("Helvetica", 15), fg="black", bg="#add8e6")
wd_label.place(x=50, y=360, height=40, width=220)
wd2_label = Label(win, text="", font=("Helvetica", 15), fg="black", bg="#add8e6")
wd2_label.place(x=300, y=360, height=40, width=220)

temp_label = Label(win, text="Temperature (°C): ", font=("Helvetica", 15), fg="black", bg="#add8e6")
temp_label.place(x=50, y=420, height=40, width=220)
temp1_label = Label(win, text="", font=("Helvetica", 15), fg="black", bg="#add8e6")
temp1_label.place(x=300, y=420, height=40, width=220)

pressure_label = Label(win, text="Pressure (hPa): ", font=("Helvetica", 15), fg="black", bg="#add8e6")
pressure_label.place(x=50, y=480, height=40, width=220)
pressure1_label = Label(win, text="", font=("Helvetica", 15), fg="black", bg="#add8e6")
pressure1_label.place(x=300, y=480, height=40, width=220)

# Button to fetch weather data
done_button = Button(win, text="Get Weather", font=("Helvetica", 16, "bold"), bg="#1e90ff", fg="white", command=data_get)
done_button.place(x=250, y=550, height=50, width=150)

win.mainloop()

win = Tk()
win.title("CLIMATECH")
win.geometry("600x650")

# Set the background image
bg_image = Image.open("clouds-sun-rays-sky.jpg")  # Ensure the image is in the same directory
bg_image = bg_image.resize((600, 650), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(win, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Set background image

# Add the logo
logo_image = Image.open("weather(1).png")  # Ensure the logo is in the same directory
logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = Label(win, image=logo_photo, bg="light blue")
logo_label.place(x=250, y=10, width=100, height=100)

# Application title
name_label = Label(win, text="CLIMATECH", font=("Helvetica", 28, "bold"), fg="white", bg="#1e90ff")
name_label.place(x=100, y=120, height=50, width=400)

# Dropdown for city selection
city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
             "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
             "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli",
             "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("Helvetica", 16), textvariable=city_name)
com.place(x=100, y=200, height=40, width=400)

# Weather labels
w_label = Label(win, text="Weather Climate: ", font=("Helvetica", 15), fg="black", bg="#add8e6")
w_label.place(x=50, y=300, height=40, width=220)
w1_label = Label(win, text="", font=("Helvetica", 15), fg="black", bg="#add8e6")
w1_label.place(x=300, y=300, height=40, width=220)

wd_label = Label(win, text="Weather Description: ", font=("Helvetica", 15), fg="black", bg="#add8e6")
wd_label.place(x=50, y=360, height=40, width=220)
wd2_label = Label(win, text="", font=("Helvetica", 15), fg="black", bg="#add8e6")
wd2_label.place(x=300, y=360, height=40, width=220)

temp_label = Label(win, text="Temperature (°C): ", font=("Helvetica", 15), fg="black", bg="#add8e6")
temp_label.place(x=50, y=420, height=40, width=220)
temp1_label = Label(win, text="", font=("Helvetica", 15), fg="black", bg="#add8e6")
temp1_label.place(x=300, y=420, height=40, width=220)

pressure_label = Label(win, text="Pressure (hPa): ", font=("Helvetica", 15), fg="black", bg="#add8e6")
pressure_label.place(x=50, y=480, height=40, width=220)
pressure1_label = Label(win, text="", font=("Helvetica", 15), fg="black", bg="#add8e6")
pressure1_label.place(x=300, y=480, height=40, width=220)

# Button to fetch weather data
done_button = Button(win, text="Get Weather", font=("Helvetica", 16, "bold"), bg="#1e90ff", fg="white", command=data_get)
done_button.place(x=250, y=550, height=50, width=150)

win.mainloop()
