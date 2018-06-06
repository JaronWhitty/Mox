#test_find_mox_events
from find_mox_events import find_mox_events as fme
import numpy as np
import pytest


@pytest.fixture
def set_up_mox():
    mox = [1,2,3]*160
    times = np.arange(480)
    return mox, times

def test_find_mox_events(set_up_mox):
    mox, times = set_up_mox
    events = fme.find_mox_events(mox, times)
    assert len(events) == 0
    assert type(events) == dict
    assert np.shape(events) == ()
    
    