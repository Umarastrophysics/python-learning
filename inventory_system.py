"""
SYSTEM: Space Station Inventory Manager
AUTHOR: [Your Name]
DESCRIPTION: Simulates an emergency alarm system and allows the user 
             to safely look up items inside the ship's inventory lockers.
"""

# space station inventory setup
space_station_inventry = ["rockets","exo_guns","plasma_guns","fuel_tank","guiding_ai_gemini"]
space_station_inventry.append("repair_crew")
space_station_inventry.append("emergency_super_dense_fuel")

# The alarm loop
for i in range(3):
    print("we forgot stuff")

# User choice system
item_needed_to_utlize_from_space_station_inventry = int(input("what item do we need to utlize:"))
print(space_station_inventry[item_needed_to_utlize_from_space_station_inventry])
