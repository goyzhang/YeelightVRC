from json import load
from yeelightvrc.models.avatar_model import *
import os

localpath = os.path.dirname(os.path.abspath(__file__))


def test_hello():
    with open(localpath +"/avtr_sample.json") as f:
        cfg = f.read()
    avtr_parm = load_from_config(cfg)
    assert "hue top" in avtr_parm
    assert "/avatar/parameters" in avtr_parm["hue top"].address
    return
    