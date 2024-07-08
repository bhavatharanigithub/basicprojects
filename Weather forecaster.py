
import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather Forecast App")

        self.label = tk.Label(master, text="Enter city name:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.button.pack()

        self.unit_var = tk.StringVar()
        self.unit_var.set("metric")
        self.unit_label = tk.Label(master, text="Select unit:")
        self.unit_label.pack()
        self.unit_combobox = ttk.Combobox(master, textvariable=self.unit_var, values=["metric", "imperial"])
        self.unit_combobox.pack()

    def get_weather(self):
        location = self.entry.get()
        unit = self.unit_var.get()
        api_key = 'a96ace5abaaa93f8acf3591fcaeb83aa'  # Replace 'YOUR_API_KEY' with your actual API key
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units={unit}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            forecast_data = response.json()

            forecast_str = ""
            for item in forecast_data['list']:
                date_time = item['dt_txt']
                temperature = item['main']['temp']
                weather_description = item['weather'][0]['description']
                forecast_str += f"Date/Time: {date_time}, Temperature: {temperature}°C, Weather: {weather_description.capitalize()}\n"

            messagebox.showinfo("Weather Forecast", f"5-Day Weather Forecast for {location}:\n{forecast_str}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to retrieve weather forecast: {e}")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
