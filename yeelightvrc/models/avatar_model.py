
import json


class AvatarParameter:
    name: str
    address: str

    def __init__(self, name, address):
        self.name = name
        self.address = address

def load_from_config(avatarConfig) -> list[AvatarParameter]:
    parms = json.load(avatarConfig)["parameters"]
    avps = {}
    for avp in parms:
        avps[avp["name"]] = AvatarParameter(avp["name"], avp["address"])
    return avps


SampleParameters = {
    "color": AvatarParameter("color", "/avatar/parameters/hue_top"),
    "brightness": AvatarParameter("brightness", "/avatar/parameters/Dark"),
}