import requests
import tkinter as tk

window = tk.Tk()
window.title("Weather")
window.geometry("500x500")
window.configure(pady=20)

#label
input_label = tk.Label(window, text="Enter City Name",pady=5)
input_label.pack()

#input
inputCityEntry = tk.Entry(window, width=30)
inputCityEntry.pack(pady=10)

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

            result_label_weather.config(text=f"Temperature in {city}: {temp} C°",pady=5)
            result_label_sky.config(text=f"The sky in {city}: {desc}",pady=5)


        else:
            result_label_weather.config(text=f"City Not Found",pady=5)

    except:
        result_label_weather.config(text="Connection Error",fg="red",pady=5)


#button
getCityButton = tk.Button(text="Get City",command=activate_button)
getCityButton.pack(pady=5)
#result
city = inputCityEntry.get()

result_label_weather = tk.Label(window, text="",pady=5)
result_label_weather.pack()
result_label_sky = tk.Label(window, text="",pady=5)
result_label_sky.pack()

window.mainloop()