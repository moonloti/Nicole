# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_names(targets):
    for name in targets:
        print(name)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_star_and_spectral_type(targets):
    for name, info in targets.items():
        print(name, "-", info["Spectral Type"])

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def stars_brighter_than_point_one(targets):
    for name, info in targets.items():
        if info["Magnitude"] > 0.1:
            print(name, "has magnitude", info["Magnitude"])

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Aldebaran"] = {
    "RA": "04h 35m 55.2s",
    "Dec": "+16° 30′ 33″",
    "Magnitude": 0.85,
    "Spectral Type": "K5III"
}
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def dec_to_degrees(dec_string):
    # Example: "+07° 24′ 25″"
    sign = 1 if dec_string[0] == "+" else -1
    parts = dec_string[1:].replace("°", "").replace("′", "").replace("″", "").split()
    degrees = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return sign * (degrees + minutes/60 + seconds/3600)

def brightest_near_20_deg(targets):
    best_star = None
    best_score = float("inf")  # smaller = closer to 20°
    best_mag = float("inf")    # smaller = brighter

    for name, info in targets.items():
        dec_deg = dec_to_degrees(info["Dec"])
        closeness = abs(dec_deg - 20)

        if closeness < best_score or (closeness == best_score and info["Magnitude"] < best_mag):
            best_star = name
            best_score = closeness
            best_mag = info["Magnitude"]

    return best_star

# 6) What is your favorite constellation?
# Orion mainly because it is the easiest to spot in the night sky.