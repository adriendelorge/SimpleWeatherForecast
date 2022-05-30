# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    #Look for a given city and disambiguate between several candidates. Return one city (or None)

    city_name=query

    response=requests.get('https://www.metaweather.com/api/location/search', params={'query': city_name}).json()

    if len(response)==0:
        return None

    return response [0]
    #print (response[city_name])

def weather_forecast(woeid):
    '''Return a 5-element list of weather forecast for a given woeid'''

    #response=requests.get('https://www.metaweather.com/api/location/', params={'woeid': woeid}).json()
    response=requests.get('https://www.metaweather.com/api/location/'+str(woeid)).json()
   # print('https://www.metaweather.com/api/location/' + str(woeid))
    weather=response.get('consolidated_weather')
    return (weather[1:])

def main():
    #Ask user for a city and display weather forecast
    query = input("City?\n> ")
    city = search_city(query)
    if city==None:
        print ("Error")
    else:
        weather= weather_forecast(city['woeid'])
    # TODO: Display weather forecast for a given city
        print ('Here is the weather in' + ' ' + str(city['title']))
        for index in weather:

            print (str(index['applicable_date']) + ':' + ' ' +str(index['weather_state_name'])+ ' '+str(round(index['the_temp'],1))+'°C')

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
