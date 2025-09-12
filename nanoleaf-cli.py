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

    # Params
    parser.add_argument("--color", type=str, help="")
    parser.add_argument("-b", "--brightness", type=int, help="")
    parser.add_argument("-d", "--duration", type=int, help="Optional (Default=0), The duration over which to change the brightness ")
    parser.add_argument("-u", "--hue", type=int, help="")
    parser.add_argument("-i", "--increment", type=int, help="")
    parser.add_argument("-n", "--name", type=int, help="")

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
            'set_hue': set_hue,
            'increment_hue': increment_hue,
            'get_hue': get_hue,
            'set_saturation': set_saturation,
            'increment_saturation': increment_saturation,
            'get_saturation': get_saturation,
            'set_color_temp': set_color_temp,
            'increment_color_temp': increment_color_temp,
            'get_color_temp': get_color_temp,
            'identify': identify,
            'get_color_mode': get_color_mode,
            'get_current_effect': get_current_effect,
            'list_effects': list_effects,
            'effect_exists': effect_exists,
            'set_effect': set_effect,
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

    print_debug(f"Set color to: {args.color}")

    if is_three_tuple(args.color):
        print_debug("String matches tuple")
        nl.set_color(ast.literal_eval(args.color))
    elif args.color in COLORS:
        print_debug("Color is a defined color")
        nl.set_color(COLORS[args.color])
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
    nl.increment_brightness(args.increment)

def get_brightness(args, nl):
    print(nl.get_brightness())

def set_hue(args, nl):
    if not args.hue:
        print_error("--hue argument required")
        exit(ERROR_MISSING_ARGS)
    nl.set_hue(args.hue)

def increment_hue(args, nl):
    if not args.increment:
        print_error("--increment argument required")
        exit(ERROR_MISSING_ARGS)
    nl.increment_hue(args.increment)

def get_hue(args, nl):
    print(nl.get_hue())

def set_saturation(args, nl):
    if not args.saturation:
        print_error("--hue argument required")
        exit(ERROR_MISSING_ARGS)
    nl.set_saturation(args.saturation)

def increment_saturation(args, nl):
    if not args.increment:
        print_error("--increment argument required")
        exit(ERROR_MISSING_ARGS)
    nl.increment_saturation(args.increment)

def get_saturation(args, nl):
    print(nl.get_saturation())

def identify(args, nl):
    nl.identify()

def set_color_temp(args, nl):
    if not args.color_temp:
        print_error("--hue argument required")
        exit(ERROR_MISSING_ARGS)
    nl.set_color_temp(args.color_temp)

def increment_color_temp(args, nl):
    if not args.increment:
        print_error("--increment argument required")
        exit(ERROR_MISSING_ARGS)
    nl.increment_color_temp(args.increment)

def get_color_temp(args, nl):
    print(nl.get_color_temp())

def get_color_mode(args, nl):
    print(nl.get_color_mode())

def get_current_effect(args, nl):
    print(nl.get_current_effect())

def list_effects(args, nl):
    print(nl.list_effects())

def effect_exists(args, nl): #name
    if not args.name:
        print_error("--name argument required")
        exit(ERROR_MISSING_ARGS)
    nl.effect_exists(args.name)

def set_effect(args, nl): #name
    pass

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
