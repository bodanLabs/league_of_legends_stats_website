import requests


def convert_game_time(game_duration):
    url_for_minutes_conversion = f"https://www.inchcalculator.com/api/calculators/unit-conversion/?from_value={game_duration}&from_unit=second&to_unit=minute"
    response = requests.get(url_for_minutes_conversion)
    data_for_minutes_conversion = response.json()
    game_time_before_formatting = data_for_minutes_conversion['results']["display_value"]
    game_time = game_time_before_formatting.split("=", 2)
    return(game_time[2])