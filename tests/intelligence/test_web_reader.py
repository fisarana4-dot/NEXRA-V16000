def test_fetch():
 from app.intelligence.external.web_reader import fetch
 assert fetch("https://www.bea.gov/")[0]==200
