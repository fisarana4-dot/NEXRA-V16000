from observability.logger import EMFLogger
def test_logger():
    assert "aws" in EMFLogger.log("lat", 45)
