import math
def haversine_distance(lat1, lon1, lat2, lon2):
    earth_radius = 6371
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c

    return distance

# Example usage
lat1 = 52.5200  # Latitude of Place 1
lon1 = 13.4050  # Longitude of Place 1
lat2 = 48.8566  # Latitude of Place 2
lon2 = 2.3522   # Longitude of Place 2

distance = haversine_distance(lat1, lon1, lat2, lon2)
print(f"The distance between the two places is {distance:.2f} km.")