def get_season_advice(season: str) -> str:
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type: str) -> str:
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def generate_advice(season: str, plant_type: str) -> str:
    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)
    return advice


def main() -> None:
    # Hardcoded values for the season and plant type
    season = "summer"  # TODO: Replace with input() to allow user interaction.
    plant_type = "flower"  # TODO: Replace with input() to allow user interaction.

    # Generate and print the advice
    print(generate_advice(season, plant_type))


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
