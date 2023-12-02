import requests
import json

class Weather_API():
    def __init__(self) -> None:
        self.url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
        self.headers = {
            "X-RapidAPI-Key": "your_key",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }
        self.response = {}

    def get_Weather_Data(self, city_name):
        querystring = {"q":city_name, "days":"3"}
        self.response = json.loads(requests.get(self.url, headers=self.headers, params=querystring).content)
        if 'error' in self.response.keys():
            self.weather_data = self.error_handling(self.response['error']['message'])
            return self.weather_data
        final_Data = {'city':self.response['location']['name'], 'current':{},
                      'forecast':[]}

        
        
        for day in self.response['forecast']['forecastday']:
            list_needed_Data_hour = [
                'temp_c',
                'temp_f',
                'feelslike_c',
                'feelslike_f',
                'humidity',
                'chance_of_rain',
                'chance_of_snow'
                ]     
            list_needed_Data_day = [
                'maxtemp_c',
                'maxtemp_f',
                'mintemp_c',
                'mintemp_f',
                'avgtemp_c',
                'avgtemp_f',
                'daily_will_it_rain',
                'daily_will_it_snow'
                ]
            
            day_Data = {'date':day['date'], 'average':{}, 'hourly':{}}
            for key in day['day']:
                if key in list_needed_Data_day:
                    day_Data['average'][key] = day['day'][key]
            
            for hour in day['hour']:
                day_Data['hourly'][hour['time'].split(' ')[-1]] = {}
                for key in hour:
                    if key in list_needed_Data_hour:
                        day_Data['hourly'][hour['time'].split(' ')[-1]][key] = hour[key]   
        
            final_Data['forecast'].append(day_Data)
        
        list_needed_Data_day = [
            'temp_c',
            'temp_f',
            'humidity',
            'feelslike_c',
            'feelslike_f',
            'cloud'
            ]
        
        current_data = self.response['current']
        for key in current_data.keys():
            if key in list_needed_Data_day:
                final_Data['current'][key] = current_data[key]
                
        self.weather_data = final_Data
        return final_Data                 
    
    def error_handling(self, error_message):
        #print(error_message)
        return error_message


if __name__ == '__main__':
    api = Weather_API()
    weather_data = api.get_Weather_Data('Bucharest')
    print(weather_data)