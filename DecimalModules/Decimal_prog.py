import decimal
class Dec:
    def deci(self):
       d = decimal.Decimal("1.1")
       f = float(d)
       print(f)

d=Dec()
d.deci()
