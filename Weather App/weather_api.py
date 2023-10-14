import requests

class Weather_API():
    def __init__(self) -> None:
        self.url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
        self.headers = {
            "X-RapidAPI-Key": "616da7c131mshf336e524cc759e2p119c85jsn5b120f1b5e7d",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }
        self.response = {}

    def get_Weather_Data(self, city_name):
        querystring = {"q":city_name}
        self.response = requests.get(self.url, headers=self.headers, params=querystring)
    
    def error_handling(self, error_message):
        print(error_message)
        return error_message

    def parse_Weather_Data(self):
        if 'error' in self.response.keys:
            self.error_handling(self.response['error']['message'])
        final_Data = {'city':self.response['location']['name'],
                      'forecast':{}}

        for day in self.response['forecast']['forecastday'].keys():
            dict_needed_Data_hourly = {
            'temp_c':'',
            'temp_f':'',
            'localtime':'',
            'is_day':'',
            'feelslike_c':'',
            'feelslike_f':'',
            'humidity': '',
            'precip_mm': '',
            'chance_of_rain':'',
            'chance_of_snow':''
        }
            day_Data = {'date':day['date'], 'average':{}, 'hourly':{}, 'astro':{}}



if __name__ == '__main__':
    api = Weather_API()
    api.get_Weather_Data('Bucharesta')