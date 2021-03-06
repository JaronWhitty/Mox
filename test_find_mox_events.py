#test_find_mox_events
from find_mox_events.find_mox_events import find_mox_events as fmox
import numpy as np
import pytest
import random

@pytest.fixture
def set_up_mox():
    mox = [1,2,3]*160
    times = np.arange(480)
    bmox = [1,2,3]*160
    bmox.append(5000)
    btimes = np.arange(481)
    varmox = []
    for i in range(660):
        varmox.append(random.randrange(1,300))
    varmox= varmox + ([300,600,900,1200,1500,1800,2100]*20)
    for i in range(500):
        varmox.append(random.randrange(1,300))
    vartimes = np.arange(1300)
    varmox2 = []
    for i in range(660):
        varmox2.append(random.randrange(1,300))
    varmox2= varmox2 + ([300,600,900,1200,1500,1800,2100]*20)
    varmox2 = varmox2 + ([0]*500)
    vartimes = np.arange(1300)
    varmox3 = [300,600,900,1200,1500,1800,2100, 2400, 2700, 3000, 3300, 3600, 3900]*100
    return mox, times, bmox, btimes, varmox, vartimes, varmox2, varmox3

def test_find_mox_events(set_up_mox):
    mox, times, bmox, btimes, varmox, vartimes, varmox2, varmox3 = set_up_mox
    events = fmox(mox, times)
    bevents = fmox(bmox, btimes)
    vevents = fmox(varmox, vartimes)
    vevents2 = fmox(varmox2, vartimes)
    vevents3 = fmox(varmox3, vartimes)
    assert len(vevents3['magnitude']) != 0
    assert len(vevents2['magnitude']) == 0
    assert len(vevents['magnitude']) == 0
    assert type(vevents) == dict
    assert len(bevents['magnitude']) == 0
    assert type(bevents) == dict
    assert len(events['magnitude']) == 0
    assert type(events) == dict

    
    