WORKSPACE = {
             "rack1"     : [(100, 0, 100), (100, 10, 100), (100, 30, 100)],
             "rack2"     : [(200, 0, 100), (200, 10, 100), (200, 30, 100)],
             "rack3"     : [(300, 0, 100), (300, 10, 100), (300, 30, 100)],
             "centrifuge": [(400, 0, 150)]
            }

def get_names():
    names = []
    for name, positions in WORKSPACE.items():
        slot = 1
        for point in positions:
            names.append(name + "slot" + str(slot))
            slot += 1
    return names

def get_position(ai_name):
    for name, positions in WORKSPACE.items():
        slot = 1
        for point in positions:
            if ai_name == name + "slot" + str(slot):
                return point
            slot += 1
    return None