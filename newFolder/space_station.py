class SpaceStation:
    def __init__(self, name):
        self.name = name
        self.satellites = []
    
    def add_satellite(self, satellite):
        self.satellites.append(satellite)
    
    def get_weather_data(self):
        # Retrieve weather data from satellites
        data = []
        for satellite in self.satellites:
            satellite_data = satellite.capture_weather_data()
            data.append(satellite_data)
        return data
