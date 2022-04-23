
import json


class AvatarParameter:
    name: str
    address: str

    def __init__(self, name, address):
        self.name = name
        self.address = address

def load_from_config(avatarConfig) -> dict[str, AvatarParameter]:
    parms = json.loads(avatarConfig)["parameters"]
    avps = {}
    for avp in parms:
        if "input" in avp:
            avps[avp["name"]] = AvatarParameter(avp["name"], avp["input"]["address"])
        elif "address" in avp:
            avps[avp["name"]] = AvatarParameter(avp["name"], avp["input"]["address"])
    return avps


SampleParameters = {
    "color": AvatarParameter("color", "/avatar/parameters/hue_top"),
    "brightness": AvatarParameter("brightness", "/avatar/parameters/Dark"),
}