import googlemaps


def get_geolocation(id, name):
    key = "your key...."
    gmaps = googlemaps.Client(key=key)
    geocode_result = gmaps.geocode('別府市 ' + name)
    print(str(len(geocode_result)), name)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    return (str(id), str(name), str(lat), str(lng))


output = open('onsen-location.csv', 'w', encoding='utf-8')


with open('onsen-base.txt', 'r', encoding="utf-8") as f:
    for line in f:
        cols = line.split(',')
        id = cols[0]
        name = cols[3]
        print(name)
        result = get_geolocation(id, name)
        output.write(",".join(result))
        output.write("\n")

output.close()
