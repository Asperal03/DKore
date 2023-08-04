from phue import Bridge

# IP address of your bridge
BRIDGE_IP = '192.168.1.155'

# Connection to the bridge
bridge = Bridge(BRIDGE_IP)

# Connect to bridge
bridge.connect()

# List light IDs or names you want to control
LIGHTS = [20, 36, 37, 17, 15]

def set_hue_light(light_id, on=None, brightness=None, hue=None, saturation=None):
    """
    Control a specified Hue light.
    
    :param light_id: ID or name of the light to control
    :param on: True to turn on, False to turn off
    :param brightness: 0 to 254
    :param hue: 0 to 65535
    :param saturation: 0 to 254
    """
    command = {}
    if on is not None:
        command['on'] = on
    if brightness is not None:
        command['bri'] = brightness
    if hue is not None:
        command['hue'] = hue
    if saturation is not None:
        command['sat'] = saturation

    bridge.set_light(light_id, command)


def set_all_lights(on=None, brightness=None, hue=None, saturation=None):
    """
    Control all specified Hue lights.
    """
    for light_id in LIGHTS:
        set_hue_light(light_id, on, brightness, hue, saturation)

if __name__ == '__main__':
    # Turn on all lights with medium brightness
    light = bridge.lights[20] # Replace with one of your light IDs
    print(light.__dict__) # Print the state before
    set_hue_light(20, on=True, brightness=127, hue=10000, saturation=100)
    light = bridge.lights[20] # Access the light again to refresh its state
    print(light.__dict__) # Print the state after

    api_data = bridge.get_api()
    lights_data = api_data['lights']
    for light_id, details in lights_data.items():
        name = details['name']
        state = details['state']['on']
        reach = details['state']['reachable']
        print(f"Light ID: {light_id}, Name: {name}, On: {state}, Reachable: {reach}")
