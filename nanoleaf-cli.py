from nanoleafapi import discovery, Nanoleaf
import argparse, time, ast

DEBUG = True

ERROR_MISSING_ARGS = 3

COLORS={
    "RED": (255, 0, 0),
    "ORANGE": (255, 165, 0),
    "YELLOW": (255, 255, 0),
    "GREEN": (0, 255, 0),
    "LIGHT_BLUE": (173, 216, 230),
    "BLUE": (0, 0, 255),
    "PINK": (255, 192, 203),
    "PURPLE": (128, 0, 128),
    "WHITE": (255, 255, 255),
}
def print_debug(log):
    if DEBUG:
        print(f"\033[34m[DEBUG] {log}")

def print_error(log):
    print(f"\033[31m[ERROR] {log}")

def setup_args():
    parser = argparse.ArgumentParser(description="Simple CLI Interface for the nanleafapi")

    function_map = setup_function_map()
    # Actions TODO: Impement help messages
    parser.add_argument("--discovery", action="store_true", help="")
    parser.add_argument("--get_token", action="store_true", help="")

    parser.add_argument("command", choices=function_map.keys())

    parser.add_argument("--color", type=str, help="")

    parser.add_argument("-b", "--brightness", type=int, help="")
    parser.add_argument("-d", "--duration", type=int, help="Optional (Default=0), The duration over which to change the brightness ")

    parser.add_argument("-i", "--increment", type=int, help="")

    # Params
    parser.add_argument("--host", type=str, help="Hostname for the Nanoleaf lights.")
    parser.add_argument("--debug", action="store_true", help="Print debug logs.")

    return parser.parse_args()

def setup_function_map():

    return {
            'discovery': do_discovery,
            'get_token': get_token,
            'get_info': get_info,
            'get_name': get_name,
            'check_connection': check_connection,
            'get_power': get_power,
            'power_on': power_on,
            'power_off': power_off,
            'toggle_power': toggle_power,
            'set_color': set_color,
            'set_brightness': set_brightness,
            'increment_brightness': increment_brightness,
            'get_brightness': get_brightness,
        }

def get_host(args):
    if not args.host:
        print("Command requires the --host parameter.")
        exit(ERROR_MISSING_ARGS)
    return args.host

def get_nanoleaf(host):
    return Nanoleaf(host)

def is_three_tuple(s):
    try:
        value = ast.literal_eval(s)
        return isinstance(value, tuple) and len(value) == 3
    except (ValueError, SyntaxError):
        return False

def do_discovery(args, nl):
    print("Running Discovery")
    nanoleaf_dict = discovery.discover_devices()
    print(f"Devices Found: {nanoleaf_dict}")
    exit(0)

def get_token(args, nl):
    pass

def get_info(args, nl):
    print_debug(host)
    print(nl.get_info())

def get_name(args, nl):
    print(nl.get_name())

def check_connection(args, nl):
    pass

def get_power(args, nl):
    print(nl.get_power())

def power_on(args, nl):
    nl.power_on()
    print(nl.get_power())

def power_off(args, nl):
    nl.power_off()
    print(nl.get_power())

def toggle_power(args, nl):
    nl.toggle_power()
    print(nl.get_power())

def set_color(args, nl):
    if not args.color:
        print_error("--color argument required")
        exit(ERROR_MISSING_ARGS)
    color = args.color

    print_debug(f"Set color to: {color}")

    if is_three_tuple(color):
        print_debug("String matches tuple")
        nl.set_color(ast.literal_eval(color))
    elif color in COLORS:
        print_debug("Color is a defined color")
        nl.set_color(COLORS[color])
    else:
        print_debug("Not Tuple")

def set_brightness(args, nl):
    if not args.brightness:
        print_error("--brightness argument required")
        exit(ERROR_MISSING_ARGS)
    brightness = args.brightness

    duration = 0
    if args.duratrion:
        duration = args.duration

    nl.set_brightness(brightness, duration)

def increment_brightness(args, nl):
    if not args.increment:
        print_error("--increment argument required")
        exit(ERROR_MISSING_ARGS)
    increment = args.increment

    nl.increment_brightness(increment)

def get_brightness(args, nl):
    print(nl.get_brightness())

if __name__ == "__main__":
    args = setup_args()
    function_map = setup_function_map()

    host = ""
    nl = None

    selected_function = function_map.get(args.command)
    if selected_function:
        host = get_host(args)
        nl = get_nanoleaf(host)
        selected_function(args, nl)
    else:
        print("Invalid command specified.")

#     if args.get_name:
#         print(f"{nl.get_name()}")

# # [ ] check_connection() # Raises NanoleafConnectionError if connection fails

# # Power
#     if args.get_power:
#         print(f"Power: {nl.get_power()}")
#     if args.power_off:
#         nl.power_off()
#         print(f"Power: {nl.get_power()}")
#     if args.power_on:
#         nl.power_on()
#         print(f"Power: {nl.get_power()}")
# # [X] toggle_power()            # Toggles light on/off
#     if args.toggle_power:
#         nl.toggle_power()
#         print(f"Power: {nl.get_power()}")

# # Colour
# # Colours are generated using HSV (or HSB) in the API, and these individual values can be adjusted using methods which are as described, hue, saturation, brightness/value. The method in this section uses RGB (0-255) and converts this to HSV.
# # There are already some pre-set colours which can be imported to be used with the set_color() method:
# # from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE, WHITE
# # The set_color() method can then be called, passing in either a pre-set colour or your own RGB colour in the form of a tuple: (r, g, b).
# # [ ] set_color((r, g, b))      # Set all lights to RGB colour. Pass the colour as a tuple.
# # [X] set_color(RED)            # Same result but using a pre-set colour.
# #   - TODO: Implement TUPLE input
#     elif args.set_color:
#         color = args.set_color
#         if color in ("RED", "ORANGE", "YELLOW", "GREEN", "LIGHT_BLUE", "BLUE", "PINK", "PURPLE", "WHITE"):
#             nl.set_color(locals()[color])



# # Hue
# # Use these if you want to change the HSV values manually, otherwise use set_color() for colour change using RGB.
# # [ ] set_hue(value)            # Sets the hue of the lights (accepts values between 0-360)
# # [ ] increment_hue(value)      # Increments the hue by set amount (can also be negative)
# # [ ] get_hue()                 # Returns current hue

# # Saturation
# # Use these if you want to change the HSV values manually, otherwise use set_color() for colour change using RGB.
# # [ ] set_saturation(value)            # Sets the saturation of the lights (accepts value between 0-100)
# # [ ] increment_saturation(value)      # Increments the saturation by set amount (can also be negative)
# # [ ] get_saturation()                 # Returns current saturation

# # Identify
# # This is usually used to identify the current lights by flashing them on and off.
# # [ ] identify()

# # Colour Temperature
# # [ ] set_color_temp(value)            # Sets the colour temperature of the lights (accepts between 1200-6500)
# # [ ] increment_color_temp(value)      # Increments the colour temperature by set amount (can also be negative)
# # [ ] get_color_temp()                 # Returns current colour temperature

# # Colour Mode
# # [X] get_color_mode()      # Returns current colour mode
#     if args.get_color_mode:
#         print(f"Color Mode: {nl.get_color_mode()}")

# # Effects
# # [X] get_current_effect()    # Returns either name of current effect if available or *Solid*/*Static*/*Dynamic*.
#     if args.get_current_effect:
#         print(f"Current Effect: {nl.get_current_effect()}")
# # [x] list_effects()          # Returns a list of names of all available effects.
#     if args.list_effects:
#         print(f"Effects: {nl.list_effects()}")

# # [X] effect_exists(name)     # Helper method which determines whether the given string exists as an effect.
#     if args.effect_exists:
#         print(f"{args.effect_exists} exitsts: {nl.effect_exists(args.effect_exists)}")
# # [X] set_effect(name)        # Sets the current effect.
#     if args.set_effect:
#         effect = args.set_effect
#         print(f"Previous Effect: {nl.get_current_effect()}")
#         nl.set_effect(effect)

#         t_end = time.time() + 5
#         while nl.get_current_effect() != effect and time.time() < t_end:
#             pass

#         print(f"Current Effect: {nl.get_current_effect()}")



# # Custom Effects
# # [ ] pulsate((r, g, b), speed)                  # Displays a pulsate effect with the specified colour and speed.
# # [ ] flow([(r, g, b), (r, g, b), ...], speed)   # Displays a sequence of specified colours and speed.
# # [ ] spectrum(speed)                            # Displays a spectrum cycling effect with the specified speed.

# # Write Effect
# # [ ] write_effect(effect_dict)    # Sets a user-created effect.
