import requests
import tkinter as tk

window = tk.Tk()
window.title("Weather")
window.geometry("400x350")
window.configure(pady=20, bg="#e0f7fa")

icon_dict = {
    "01d": tk.PhotoImage(file="weather_icon_set/01d.png").subsample(1, 1),
    "01n": tk.PhotoImage(file="weather_icon_set/01n.png").subsample(1, 1),
    "02d": tk.PhotoImage(file="weather_icon_set/02d.png").subsample(1, 1),
    "02n": tk.PhotoImage(file="weather_icon_set/02n.png").subsample(1, 1),
    "03d": tk.PhotoImage(file="weather_icon_set/03d.png").subsample(1, 1),
    "03n": tk.PhotoImage(file="weather_icon_set/03n.png").subsample(1, 1),
    "04d": tk.PhotoImage(file="weather_icon_set/04d.png").subsample(1, 1),
    "04n": tk.PhotoImage(file="weather_icon_set/04n.png").subsample(1, 1),
    "09d": tk.PhotoImage(file="weather_icon_set/09d.png").subsample(1, 1),
    "09n": tk.PhotoImage(file="weather_icon_set/09n.png").subsample(1, 1),
    "10d": tk.PhotoImage(file="weather_icon_set/10d.png").subsample(1, 1),
    "10n": tk.PhotoImage(file="weather_icon_set/10n.png").subsample(1, 1),
    "11d": tk.PhotoImage(file="weather_icon_set/11d.png").subsample(1, 1),
    "11n": tk.PhotoImage(file="weather_icon_set/11n.png").subsample(1, 1),
    "13d": tk.PhotoImage(file="weather_icon_set/13d.png").subsample(1, 1),
    "13n": tk.PhotoImage(file="weather_icon_set/13n.png").subsample(1, 1),
    "50d": tk.PhotoImage(file="weather_icon_set/50d.png").subsample(1, 1),
    "50n": tk.PhotoImage(file="weather_icon_set/50n.png").subsample(1, 1),
    "Default": tk.PhotoImage(file="default.png").subsample(1, 1)
}


#label
input_label = tk.Label(window, text="Şehir İsmi Giriniz",pady=5,bg="#e0f7fa")
input_label.pack()

#input
inputCityEntry = tk.Entry(window, width=30, font=("Arial", 12), bd=0, highlightthickness=0, bg="white")
inputCityEntry.pack(pady=10, ipady=5)

def activate_button():
    city = inputCityEntry.get()
    api_key = "5cf5b4791875ea629dce8f9825a54f24"
    api_url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"



    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data["weather"][0]["description"]
            city_name = data["name"]

            status = data["weather"][0]["icon"]
            choise_icon = icon_dict.get(status, icon_dict["Default"])
            iconLabel.config(image=choise_icon)

            result_label_weather.config(text=f"{city} şehrinde hava sıcaklığı:\n {temp} C°",pady=5)
            result_label_sky.config(text=f"ve {desc}",pady=5)


        else:
            result_label_weather.config(text=f"City Not Found",pady=5)


    except:
        result_label_weather.config(text="Connection Error",fg="red",pady=5)


#button
getCityButton = tk.Button(text="Hava Nasıl?",command=activate_button,font=("Arial",10,"bold"),bg="white",bd=0,highlightthickness=0,activebackground="#eeeeee")
getCityButton.pack(pady=5,ipady=2, ipadx=10 )
#result
city = inputCityEntry.get()

result_label_weather = tk.Label(window, text="",pady=5,bg="#e0f7fa", font=("Helvetica", 14, "bold"))
result_label_weather.pack()
result_label_sky = tk.Label(window, text="",pady=5,bg="#e0f7fa", font=("Helvetica", 14, "italic"))
result_label_sky.pack()
result_label_sky.pack()

iconApp = tk.PhotoImage(file="default.png")
iconApp = iconApp.subsample(5, 5)
iconLabel = tk.Label(window, image=iconApp,bg="#e0f7fa")
iconLabel.pack()
iconLabel.pack(pady=10)

window.mainloop()