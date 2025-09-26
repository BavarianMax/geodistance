import math

def utm_distance(e1, n1, e2, n2):
    """Berechnet den Abstand zwischen zwei UTM-Koordinaten in Metern."""
    delta_e = e2 - e1
    delta_n = n2 - n1
    return math.sqrt(delta_e**2 + delta_n**2)

if __name__ == "__main__":
    while True:
        # Eingabe für Punkt 1
        print("Gib die UTM-Koordinaten für Punkt 1 ein:")
        E1 = float(input("Easting (m): "))
        N1 = float(input("Northing (m): "))

        # Eingabe für Punkt 2
        print("\nGib die UTM-Koordinaten für Punkt 2 ein:")
        E2 = float(input("Easting (m): "))
        N2 = float(input("Northing (m): "))

        # Abstand berechnen
        distanz = utm_distance(E1, N1, E2, N2)
        print(f"\nDer Abstand beträgt: {distanz:.2f} Meter")

        input("\nDrücke Enter zum Neustarten oder STRG+C zum Beenden...\n")
