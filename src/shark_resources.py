from geopy.geocoders import Nominatim
import numpy as np
import re
def find_age(x):
    """
    Esta función recibe un string y devuelve los dos primeros numeros de este. Se utilizó para limpiar la columna de edad
    Input: String
    Output: String
    """
    if re.match('\d{1,2}',x) != None and x != np.nan:
        a = re.match('\d{1,2}',x).group(0)
        return a
    else:
        x = np.nan
        
def find_month(x):
    """
    Esta función recibe un string y devuelve un string de 3 letras que se encuentren entre dos guiones ("-"). 
    Se utilizó para limpiar la columna de mes.
    Input: String
    Output: String
    """
    if len(re.findall('-(\w{3})-',x)) != 0 and x != np.nan:
        a = re.findall('-(\w{3})-',x)
        return a[0]
    else:
        x = np.nan
        

def geolocate(country):
    """
    Esta función recibe un país y devuelve el hemisferio en el que se encuentra ("N","S").
    Input: String
    Output: String
    """
    geolocator = Nominatim(user_agent="idk")
    try:
        # Geolocate the center of the country
        loc = geolocator.geocode(country)
        # And return latitude and longitude
        if loc.latitude <= 0:
            return 'S'
        else:
            return 'N'
    except:
        # Return missing value
        return np.nan