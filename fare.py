class V():
    def __init__(self,cap):
        self.cap=cap
    def fare(self):
        return self.cap*100
class B(V):
    def fare(self):
        f1=self.cap*100
        t= f1 + (0.1 * f1)
        return t
final= B(10)
print(final.fare())