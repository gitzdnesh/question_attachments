# UNDERSTAND:
# The task is to determine the fire hazard zone based on the fire factor formula using relative humidity, surface temperature, and wind velocity.

# MATCH:
# We need to match the fire factor values to the corresponding fire hazard zones: "Medium", "High", and "Very high."

# PLAN:
# 1. Define the function calculate_fire_zone with parameters surface_temperature, relative_humidity, and wind_velocity.
# 2. Calculate the fire factor using the formula f = (TV) / r.
# 3. Determine the fire hazard zone based on the calculated fire factor.
# 4. Return the corresponding fire hazard zone name.

# IMPLEMENT:

def calculate_fire_zone(surface_temperature, relative_humidity=1, wind_velocity=0):
    """
    Determines the fire hazard zone based on surface temperature, relative humidity, and wind velocity.

    :param surface_temperature: Surface temperature in Fahrenheit.
    :param relative_humidity: Relative humidity of the air (default is 1%).
    :param wind_velocity: Wind velocity (default is 0 mph).
    :return: The fire hazard zone name ("Medium", "High", or "Very high").
    """
    # Calculate the fire factor
    fire_factor = (surface_temperature * wind_velocity) / relative_humidity

    # Determine the fire hazard zone
    if fire_factor <= 2:
        return "Medium"
    elif 2 < fire_factor <= 6:
        return "High"
    else:
        return "Very high"

def main():
    # Testing test case 1
    surface_temperature_1 = 110
    print(calculate_fire_zone(surface_temperature_1))

    # Testing test case 2
    relative_humidity_2 = 20
    surface_temperature_2 = 105
    wind_velocity_2 = 70
    print(calculate_fire_zone(surface_temperature_2, relative_humidity_2, wind_velocity_2))

    # Testing test case 3
    relative_humidity_3 = 90
    surface_temperature_3 = 60
    wind_velocity_3 = 5
    print(calculate_fire_zone(surface_temperature_3, relative_humidity_3, wind_velocity_3))

if __name__ == "__main__":
    main()