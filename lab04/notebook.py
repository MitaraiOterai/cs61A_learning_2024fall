from math import sqrt
def distance(city_a, city_b):
    """
    >>> city_a = make_city('city_a', 0, 1)
    >>> city_b = make_city('city_b', 0, 2)
    >>> distance(city_a, city_b)
    1.0
    >>> city_c = make_city('city_c', 6.5, 12)
    >>> city_d = make_city('city_d', 2.5, 15)
    >>> distance(city_c, city_d)
    5.0
    """
    def diff (x, y):
        assert type(x) == type(y) == int
        return abs(x - y)
    def l_diff(whitch_l, a, b):
        a = get_lat(city_a) if whitch_l == 'lat' else get_lon(city_a)
        b = get_lat(city_b) if whitch_l == 'lon' else get_lon(city_b)
        print(a, b)
        return diff(a,b)
    def square(x):
        return pow(x, 2)
    return sqrt(square(l_diff('lat', city_a, city_b)) + square(l_diff('lon', city_a, city_b)))

def get_name(city):
    return city[0]

def get_lat(city):


        return city[1]

def get_lon(city):

        return city[2]

city_a = make_city('city_a', 0, 1)
city_b = make_city('city_b', 0, 2)
distance(city_a, city_b)