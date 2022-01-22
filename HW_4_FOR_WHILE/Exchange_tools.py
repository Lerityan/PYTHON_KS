class Currency(object):

    def __init__(self, name, usd_rate):
        self.name = name
        self.rate = usd_rate

    def to_usd(self, amount):
        usd_amount = amount / self.rate
        return usd_amount

    def from_usd(self, amount):
        self_amount = amount * self.rate
        return self_amount

    def to_self_output(self, amount):
        print("Конвертированная сумма в", self.name, "=", "%.2f" % self.from_usd(amount))

    def to_usd_output(self, amount):
        print("Конвертированная сумма в USD =", "%.2f" % self.to_usd(amount))


class Exchange:

    def convert(Cur1, Cur2, amount):
        return Cur2.from_usd(Cur1.to_usd(amount))
