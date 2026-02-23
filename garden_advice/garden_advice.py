# garden_advice.py

def get_advice():
    # TODO: Replace hardcoded values with a config file or user input
    plant = "Tomato"
    soil_moisture = "Dry"
    
    # TODO: Create a separate function to handle advice logic
    if plant == "Tomato" and soil_moisture == "Dry":
        print("Water your tomatoes immediately.")
    else:
        print("Check soil again tomorrow.")

# TODO: Add proper documentation/docstrings
get_advice()
