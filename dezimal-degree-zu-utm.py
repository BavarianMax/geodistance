import math

def deg_to_utm(lat, lon):
    """
    Wandelt Dezimalgrad (latitude, longitude) in UTM-Koordinaten um.
    Gibt Easting, Northing und Zone zurück.
    """
    a = 6378137.0  # Erdhalbachse
    f = 1 / 298.257223563  # Abplattung
    k0 = 0.9996  # Maßstabsfaktor

    zone_number = int((lon + 180) / 6) + 1
    lon0 = (zone_number - 1) * 6 - 180 + 3
    lon0_rad = math.radians(lon0)

    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    e = math.sqrt(f * (2 - f))

    N = a / math.sqrt(1 - e**2 * math.sin(lat_rad)**2)
    T = math.tan(lat_rad)**2
    C = (e**2 / (1 - e**2)) * math.cos(lat_rad)**2
    A = math.cos(lat_rad) * (lon_rad - lon0_rad)

    M = a * ((1 - e**2 / 4 - 3 * e**4 / 64 - 5 * e**6 / 256) * lat_rad
             - (3 * e**2 / 8 + 3 * e**4 / 32 + 45 * e**6 / 1024) * math.sin(2 * lat_rad)
             + (15 * e**4 / 256 + 45 * e**6 / 1024) * math.sin(4 * lat_rad)
             - (35 * e**6 / 3072) * math.sin(6 * lat_rad))

    easting = k0 * N * (A + (1 - T + C) * A**3 / 6
                       + (5 - 18 * T + T**2 + 72 * C - 58 * (e**2 / (1 - e**2))) * A**5 / 120) + 500000

    northing = k0 * (M + N * math.tan(lat_rad) * (A**2 / 2
                      + (5 - T + 9 * C + 4 * C**2) * A**4 / 24
                      + (61 - 58 * T + T**2 + 600 * C - 330 * (e**2 / (1 - e**2))) * A**6 / 720))

    if lat < 0:
        northing += 10000000  # Südliche Hemisphäre Korrektur

    return easting, northing, zone_number

if __name__ == "__main__":
    while True:
        print("Gib die Koordinaten in Dezimalgrad ein:")
        lat = float(input("Breitengrad (lat): "))
        lon = float(input("Längengrad (lon): "))

        E, N, zone = deg_to_utm(lat, lon)
        print(f"UTM Easting: {E:.2f}, Northing: {N:.2f}, Zone: {zone}")

        input("\nDrücke Enter zum Neustarten oder STRG+C zum Beenden...\n")
