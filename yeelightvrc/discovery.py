from yeelight import discover_bulbs

r = discover_bulbs()
print(f"device(s) find: {len(r)}")