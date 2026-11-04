import time
class FailoverKernel:
    def __init__(self, p): self.p = p
    def execute(self, q):
        for pr in self.p:
            try: return pr(q)
            except:
                continue
        raise Exception('All failed')
