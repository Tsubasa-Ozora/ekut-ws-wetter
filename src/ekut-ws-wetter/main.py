def get_weather(city: str) -> str:
    if city == "Tübingen":
        return "Cloudy"
    elif city == "Stuttgart":
        return "Rainy"
    elif city == "Bordeaux":
        return "Sunny"
    return None


def get_temp(city: str) -> float:
    return 11.7
