from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos


def handle(event, context):
    date = str(event['date'])
    time = str(event['time'])
    timezone = str(event['timezone'])
    lat = str(event['lat'])
    lng = str(event['lng'])
    pos = GeoPos(lat, lng)
    datetime = Datetime(date, time, timezone)
    chart = Chart(datetime, pos)
    return [
        {'characteristic': 'Sun', 'sign': chart.get(const.SUN).sign, 'angle': str(chart.get(const.SUN).signlon)},
        {'characteristic': 'Moon', 'sign': chart.get(const.MOON).sign, 'angle': chart.get(const.MOON).signlon},
        {'characteristic': 'Mercury', 'sign': chart.get(const.MERCURY).sign, 'angle': chart.get(const.MERCURY).signlon},
        {'characteristic': 'Mars', 'sign': chart.get(const.MARS).sign, 'angle': chart.get(const.MARS).signlon},
        {'characteristic': 'Venus', 'sign': chart.get(const.VENUS).sign, 'angle': chart.get(const.VENUS).signlon},
        {'characteristic': 'Jupiter', 'sign': chart.get(const.JUPITER).sign, 'angle': chart.get(const.JUPITER).signlon},
        {'characteristic': 'Saturn', 'sign': chart.get(const.SATURN).sign, 'angle': chart.get(const.SATURN).signlon},
        # {'characteristic': 'Uranus', 'sign': chart.get(const.URANUS).sign, 'angle': chart.get(const.URANUS).signlon},
        # {'characteristic': 'Neptune', 'sign': chart.get(const.NEPTUNE).sign, 'angle': chart.get(const.NEPTUNE).signlon},
        {'characteristic': 'Ascendant', 'sign': chart.get(const.ASC).sign, 'angle': chart.get(const.ASC).signlon},
    ]

