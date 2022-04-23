'''

ref : Yeelight_Inter-Operation_Spec

Property Name Possible value
power on: smart LED is turned on / off: smart LED is turned off
bright Brightness percentage. Range 1 ~ 100
ct Color temperature. Range 1700 ~ 6500(k)
rgb Color. Range 1 ~ 16777215
hue Hue. Range 0 ~ 359
sat Saturation. Range 0 ~ 100
color_mode 1: rgb mode / 2: color temperature mode / 3: hsv mode
flowing 0: no flow is running / 1:color flow is running
delayoff The remaining time of a sleep timer. Range 1 ~ 60 (minutes)
flow_params
Current flow parameters (only meaningful when 'flowing' is
1)
music_on 1: Music mode is on / 0: Music mode is off
name The name of the device set by “set_name” command
bg_power Background light power status
bg_flowing Background light is flowing
bg_flow_params Current flow parameters of background light
bg_ct Color temperature of background light
bg_lmode 1: rgb mode / 2: color temperature mode / 3: hsv mode
bg_bright Brightness percentage of background light
bg_rgb Color of background light
bg_hue Hue of background light
bg_sat Saturation of background light
nl_br Brightness of night mode light
active_mode 0: daylight mode / 1: moonlight mode (ceiling light only)
'''
class LightProperties:
    power: str
    bright: str
    ct: str
    rgb: str
    hue: str
    sat: str
    color_mode: str
    flowing: str
    delayoff: str
    music_on: str
    name: str
    bg_power: str
    bg_flowing: str
    bg_ct: str
    bg_bright: str
    bg_hue: str
    bg_sat: str
    bg_rgb: str
    nl_br: str
    active_mode: str
    current_brightness: str