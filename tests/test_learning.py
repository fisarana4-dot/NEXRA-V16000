from app.trading.gold.learning.prediction import Prediction
def test_prediction():
 assert Prediction("BUY",.8).signal=="BUY"
from app.trading.gold.learning.outcome import Outcome
def test_outcome():
 assert Outcome("WIN",100).result=="WIN"
from app.trading.gold.learning.calibration import Calibration
def test_calibration():
 assert Calibration(.7,.8).confidence==.7
