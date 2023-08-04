from phue import Bridge

BRIDGE_IP = '192.168.1.155'
bridge = Bridge(BRIDGE_IP)
bridge.connect()

for light in bridge.lights:
    print(f"ID: {light.light_id}, Name: {light.name}")
