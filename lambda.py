from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


def handle(event, context):
    gimme_these = ['SUN', 'MOON', 'MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO',
                   'ASC', 'CHIRON', 'HOUSE1', 'HOUSE2', 'HOUSE3', 'HOUSE4', 'HOUSE5', 'HOUSE6', 'HOUSE7', 'HOUSE8', 'HOUSE9',
                   'HOUSE10', 'HOUSE11', 'HOUSE12']
    date = str(event['date'])
    time = str(event.get('time', ''))
    timezone = str(event.get('timezone', ''))
    lat = str(event.get('lat', '')).replace('.', ':')
    lng = str(event.get('lng', '')).replace('.', ':')

    # date = "1987/04/20"
    # time = "12:00"
    # timezone = "+01:00"
    # lat = "37:09024"
    # lng = "-95:712891"

    time_is_good = (time != '' and timezone != '')
    place_is_good = (lat != '' and lng != '')
    if time_is_good:
        datetime = [Datetime(date, time, timezone)]
    else:
        datetime = [Datetime(date, "23:59", "-12:00"), Datetime(date, "00:01", "+12:00")]
    if place_is_good:
        pos = [GeoPos(lat, lng)]
    else:
        pos = [GeoPos('-60:000', '-180:000'), GeoPos('78:000', '180:000')]
    ret = []
    if len(datetime) * len(pos) == 1:
        chart = Chart(datetime[0], pos[0], IDs=const.LIST_OBJECTS)
        for item in gimme_these:
            key = getattr(const, item)
            ret.append({'characteristic': key, 'sign': chart.get(key).sign, 'angle': str(chart.get(key).signlon)})
    else:
        chart1 = Chart(datetime[0], pos[0], IDs=const.LIST_OBJECTS)
        chart2 = Chart(datetime[-1], pos[-1], IDs=const.LIST_OBJECTS)
        for item in gimme_these:
            key = getattr(const, item)
            is_same = (chart1.get(key).sign == chart2.get(key).sign)
            ret.append({'characteristic': key,
                        'sign': str(chart1.get(key).sign if is_same else "vary"),
                        'angle': str(chart1.get(key).signlon if is_same else "vary")})
    return ret

print handle(1,2)
