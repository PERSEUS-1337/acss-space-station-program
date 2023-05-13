class Satellite:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def capture_weather_data(self):
        # Simulate capturing weather data
        data = {
            "temperature": 25.5,
            "humidity": 60.0,
            "pressure": 1013.2
        }
        return data
