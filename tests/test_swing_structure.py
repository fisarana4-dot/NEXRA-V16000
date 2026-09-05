from app.trading.gold.structure.swing_engine import *

def test_empty():
 assert detect_swings([])==[]

def test_peak():
 assert detect_swings([1,3,1],1)==["HIGH"]

def test_low():
 assert detect_swings([3,1,3],1)==["LOW"]

def test_labels():
 assert detect_swings([1,3,1,4,2],1)==["HIGH","LOW","HIGH"]

def test_hh():
 assert classify_swings([("HIGH",3),("HIGH",4)])==["HH"]

def test_hl():
 assert classify_swings([("LOW",2),("LOW",3)])==["HL"]
def test_multiple_structure(): assert classify_swings([("HIGH",3),("LOW",2),("HIGH",4),("LOW",1)])==["HH","LL"]

def test_swing_points():
 assert detect_swing_points([1,3,1])==[(1,"HIGH",3)]
def test_bull_bos():
 assert structure_shift([(1,"HIGH",3)],4)=="BOS_UP"
def test_bear_bos():
 assert structure_shift([(1,"LOW",3)],2)=="BOS_DOWN"
