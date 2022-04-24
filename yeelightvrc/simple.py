import asyncio
import logging
from yeelight import Bulb
from pythonosc import udp_client

from yeelightvrc.models.avatar_model import SampleParameters

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class YeelightVrcService:
    
    def __init__(self, yeelightip, vrcip, vrcport):
        self.osc_client = udp_client.SimpleUDPClient(vrcip, vrcport)
        self.light = Bulb(yeelightip)

#TODO: abstract avatar parameters
#TODO: error handling
    def __set_vrc_state(self, state):
        if 'bg_bright' in state:
            bg_bright = float(state['bg_bright'])
            logging.info(f"Set brightness {bg_bright}")
            self.osc_client.send_message(SampleParameters["brightness"].address, 1-bg_bright/100.0)
        if 'bg_rgb' in state:
            r = int(state['bg_rgb']) >> 16
            g = int(state['bg_rgb']) >> 8 & 0xff
            b = int(state['bg_rgb']) & 0xff
            logging.info(f"Set rgb {r, g, b}")           
        if 'bg_hue' in state:
            logging.info(f"Set bg_hue {state['hue']}")
            hue = float(state['bg_hue'])
            self.osc_client.send_message(SampleParameters["color"].address, hue/360.0)
        if 'bg_sat' in state:
            logging.info(f"Set bg_sat {state['sat']}")
        return

    def __light_update(self, notification: dict):
        self.__set_vrc_state(notification)
        return

    async def run(self):  
        logging.debug(f"Initial status: {self.light.get_properties()}")
        loop = asyncio.get_running_loop()    
        # sync initial status
        self.__set_vrc_state(self.light.get_properties())  
        await loop.run_in_executor(None, self.light.listen, self.__light_update)
  
    def stop(self):
        self.light.stop_listening()
