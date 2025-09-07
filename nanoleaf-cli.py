from nanoleafapi import discovery, Nanoleaf
from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE, WHITE
import argparse, time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple CLI Interface for the nanleafapi")

    # Actions TODO: Impement help messages
    parser.add_argument("--discovery", action="store_true", help="")
    parser.add_argument("--get_token", action="store_true", help="")
    parser.add_argument("--toggle_power", action="store_true", help="")
    parser.add_argument("--set_color", type=str, help="")
    parser.add_argument("--get_current_effect", action="store_true", help="")

    parser.add_argument("--get_color_mode", action="store_true", help="")

    parser.add_argument("--list_effects", action="store_true", help="")
    parser.add_argument("--effect_exists", type=str, help="")
    parser.add_argument("--set_effect", type=str, help="")


    # Params
    parser.add_argument("--host", type=str, help="Hostname for the Nanoleaf lights.")

    args = parser.parse_args()

    host = ""
    nl = None


    if args.discovery:
        print("Running Discovery")
        nanoleaf_dict = discovery.discover_devices()
        print(f"Devices Found: {nanoleaf_dict}")
    else:
        if not args.host:
            print("Command requires a host parameter.")
            exit(-1)
        host = args.host

    if args.get_token:
        nl = Nanoleaf(f"{host}")

# User Management
# [ ] create_auth_token()   # Creates an authentication token and stores it in the user's home directory.
# [ ] delete_auth_token()   # Deletes an authentication token from the device and the token storage file.

# General
# [ ] get_info()         # Returns device information dictionary
# [ ] get_name()         # Returns the current device name
# [ ] check_connection() # Raises NanoleafConnectionError if connection fails

# Power
# [ ] get_power()               # Returns True if lights are on, otherwise False
# [ ] power_off()               # Powers off the lights
# [ ] power_on()                # Powers on the lights
# [X] toggle_power()            # Toggles light on/off
    if args.toggle_power:
        nl = Nanoleaf(f"{host}")
        nl.toggle_power()

# Colour
# Colours are generated using HSV (or HSB) in the API, and these individual values can be adjusted using methods which are as described, hue, saturation, brightness/value. The method in this section uses RGB (0-255) and converts this to HSV.
# There are already some pre-set colours which can be imported to be used with the set_color() method:
# from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE, WHITE
# The set_color() method can then be called, passing in either a pre-set colour or your own RGB colour in the form of a tuple: (r, g, b).
# [ ] set_color((r, g, b))      # Set all lights to RGB colour. Pass the colour as a tuple.
# [X] set_color(RED)            # Same result but using a pre-set colour.
#   - TODO: Implement TUPLE input
    elif args.set_color:
        color = args.set_color
        nl = Nanoleaf(f"{host}")
        if color in ("RED", "ORANGE", "YELLOW", "GREEN", "LIGHT_BLUE", "BLUE", "PINK", "PURPLE", "WHITE"):
            nl.set_color(locals()[color])


# Brightness
# [ ] set_brightness(brightness, duration)     # Sets the brightness of the lights (accepts values between 0-100)
# [ ] increment_brightness(value)              # Increments the brightness by set amount (can also be negative)
# [ ] get_brightness()                         # Returns current brightness

# Hue
# Use these if you want to change the HSV values manually, otherwise use set_color() for colour change using RGB.
# [ ] set_hue(value)            # Sets the hue of the lights (accepts values between 0-360)
# [ ] increment_hue(value)      # Increments the hue by set amount (can also be negative)
# [ ] get_hue()                 # Returns current hue

# Saturation
# Use these if you want to change the HSV values manually, otherwise use set_color() for colour change using RGB.
# [ ] set_saturation(value)            # Sets the saturation of the lights (accepts value between 0-100)
# [ ] increment_saturation(value)      # Increments the saturation by set amount (can also be negative)
# [ ] get_saturation()                 # Returns current saturation

# Identify
# This is usually used to identify the current lights by flashing them on and off.
# [ ] identify()

# Colour Temperature
# [ ] set_color_temp(value)            # Sets the colour temperature of the lights (accepts between 1200-6500)
# [ ] increment_color_temp(value)      # Increments the colour temperature by set amount (can also be negative)
# [ ] get_color_temp()                 # Returns current colour temperature

# Colour Mode
# [ ] get_color_mode()      # Returns current colour mode
    if args.get_color_mode:
        nl = Nanoleaf(f"{host}")
        print(f"Color Mode: {nl.get_color_mode()}")

# Effects
# [X] get_current_effect()    # Returns either name of current effect if available or *Solid*/*Static*/*Dynamic*.
    if args.get_current_effect:
        nl = Nanoleaf(f"{host}")
        print(f"Current Effect: {nl.get_current_effect()}")
# [x] list_effects()          # Returns a list of names of all available effects.
    if args.list_effects:
        nl = Nanoleaf(f"{host}")
        print(f"Effects: {nl.list_effects()}")

# [X] effect_exists(name)     # Helper method which determines whether the given string exists as an effect.
    if args.effect_exists:
        nl = Nanoleaf(f"{host}")
        print(f"{args.effect_exists} exitsts: {nl.effect_exists(args.effect_exists)}")
# [X] set_effect(name)        # Sets the current effect.
    if args.set_effect:
        nl = Nanoleaf(f"{host}")
        effect = args.set_effect
        print(f"Previous Effect: {nl.get_current_effect()}")
        nl.set_effect(effect)

        t_end = time.time() + 5
        while nl.get_current_effect() != effect and time.time() < t_end:
            pass

        print(f"Current Effect: {nl.get_current_effect()}")



# Custom Effects
# [ ] pulsate((r, g, b), speed)                  # Displays a pulsate effect with the specified colour and speed.
# [ ] flow([(r, g, b), (r, g, b), ...], speed)   # Displays a sequence of specified colours and speed.
# [ ] spectrum(speed)                            # Displays a spectrum cycling effect with the specified speed.

# Write Effect
# [ ] write_effect(effect_dict)    # Sets a user-created effect.
