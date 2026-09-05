class VolumeEngine:
    def analyze(self,d): return [float(x['volume']) for x in d]
volume_engine=VolumeEngine()
