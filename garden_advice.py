"""Garden advice helpers.

This module provides small, focused functions that return
gardening advice based on a season and plant type. The functions
are intentionally simple so they are easy to test and extend.
"""


def get_season_advice(season: str) -> str:
    """Return a short piece of advice for the given season.

    Parameters
    - season: a string indicating the current season (e.g. 'summer').

    Behaviour
    - For 'summer' and 'winter' we return specific, actionable tips.
    - For any other value we return a generic fallback message so the
      caller always receives a string.

    Returns
    - A string containing season-specific advice ending with a newline
      so it reads nicely when concatenated with other advice.
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type: str) -> str:
    """Return a short piece of advice for the given plant type.

    Parameters
    - plant_type: a string such as 'flower' or 'vegetable'.

    Behaviour
    - Returns targeted tips for known plant categories.
    - Falls back to a generic message for unknown types.
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def generate_advice(season: str, plant_type: str) -> str:
    """Compose and return the full advice message.

    This function coordinates the smaller helper functions and ensures
    that the combined advice is returned as a single string. Keeping
    composition here makes it easy to change formatting in one place
    (for example, adding blank lines or headers) without touching the
    individual advice generators.
    """
    advice = ""
    # Append season-specific advice (includes trailing newline)
    advice += get_season_advice(season)
    # Append plant-specific advice (no trailing newline)
    advice += get_plant_advice(plant_type)
    return advice


def main() -> None:
    # Hardcoded defaults kept intentionally simple for this exercise.
    # TODO: Replace with `input()` or command-line args for real usage.
    season = "summer"  # TODO: Replace with input() to allow user interaction.
    plant_type = "flower"  # TODO: Replace with input() to allow user interaction.

    # Generate the combined advice and print it. Keeping the print here
    # makes this module usable as both an importable library and a
    # standalone script (guarded by the __main__ check below).
    print(generate_advice(season, plant_type))


if __name__ == "__main__":
    main()

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
