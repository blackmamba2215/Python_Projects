import tkinter as tk
from tkinter import ttk, messagebox
from weather_api import Weather_API

class Weater_GUI():
    def __init__(self):
        # Create the main window
       
        self.root = tk.Tk()
        self.root.title("Weather forecast application")
        
        self.weather_api = Weather_API()

        # Create a frame for the left side
        selection_frame = tk.Frame(self.root)
        selection_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nw')

        # Labels and widgets in the left frame
        city_label = tk.Label(selection_frame, text="City:")
        city_label.grid(row=0, column=0, sticky='w', pady = 5)

        self.city_entry = tk.Entry(selection_frame)
        self.city_entry.grid(row=0, column=1, sticky='e', pady = 5)

        confirm_button = tk.Button(selection_frame, text='OK', command=self.function)
        confirm_button.grid(row = 2, column = 0, columnspan = 2, pady=5)
        
        combo_label = tk.Label(selection_frame, text="Combo Box:")
        combo_label.grid(row=1, column=0, sticky='w')
        self.deg_type = ttk.Combobox(selection_frame, values=["Celsius", "Fahrenheit"], width=15)
        self.deg_type.grid(row=1, column=1, sticky = 'w')

    def function(self):
        city = self.city_entry.get()
        self.weather_api.get_Weather_Data(city)
        print(city)
        val = self.weather_api.weather_data
        print(val)
        if type(val) == str:
            messagebox.showerror(title='Error', message=val)
        else:
            self.current_conditions_Frame().grid(row = 0, column = 1)
            self.show_current_weather(val)


    def show_current_weather(self, weather_data):
        if self.deg_type.get() == 'Celsius':
            self.temp_value.config(text = str(weather_data['current']['temp_c']))
            self.feels_value.config(text = str(weather_data['current']['feelslike_c']))
        else:
            self.temp_value.config(text = str(weather_data['current']['temp_f']))
            self.feels_value.config(text = str(weather_data['current']['feelslike_f']))
        
        self.hum_value.config(text=str(weather_data['current']['humidity']))
        
    def current_conditions_Frame(self):
        current_frame = tk.Frame(self.root)
        current_frame.grid(row=0, column=1, padx=30, pady=10, sticky='ne', columnspan=4)
        
        current_title = tk.Label(current_frame, text="Current conditions", font=("Helvetica", 16))
        current_title.grid(row=0, column=0, columnspan=2, sticky='w')
        
        if self.deg_type.get() == 'Celsius':
            temp_label = tk.Label(current_frame, text = 'Temperature [C]:')
            feels_label = tk.Label(current_frame, text = 'Feels like [C]:')
        else:
            temp_label = tk.Label(current_frame, text = 'Temperature [F]:')
            feels_label = tk.Label(current_frame, text = 'Feels like [F]:')
        
        humidity_label = tk.Label(current_frame, text = 'Humidity [%]')
        
        temp_label.grid(row = 1, column=0, sticky='w')    
        feels_label.grid(row = 2, column=0, sticky='w') 
        humidity_label.grid(row = 3, column=0, sticky='w')
        
        self.temp_value = tk.Label(current_frame, text = '')
        self.temp_value.grid(row=1, column=1)
        self.feels_value = tk.Label(current_frame, text = '')
        self.feels_value.grid(row=2, column=1)
        self.hum_value = tk.Label(current_frame, text = '')
        self.hum_value.grid(row=3, column=1)
        
        return current_frame
        
        
                
        
'''       

# Center the main window on the screen
window_width = 600
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x}+{y}')
'''
# Start the Tkinter main loop
if __name__ == '__main__':
    app = Weater_GUI()
    app.root.mainloop()
