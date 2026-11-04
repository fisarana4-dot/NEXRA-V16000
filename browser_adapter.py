import urllib.request
class BrowserAdapter:
    def fetch(self, url):
        return urllib.request.urlopen(url).read().decode('utf-8')
