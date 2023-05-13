from satellite import Satellite
from space_station import SpaceStation

# Create space station and satellites
space_station = SpaceStation("ISS")
satellite1 = Satellite("GOES-16", [0, 0, 0])
satellite2 = Satellite("GOES-17", [0, 0, 0])

# Add satellites to space station
space_station.add_satellite(satellite1)
space_station.add_satellite(satellite2)

# Retrieve weather data
data = space_station.get_weather_data()

# Print weather data
for i, satellite_data in enumerate(data):
    print(f"Satellite {i+1}: {satellite_data}")
