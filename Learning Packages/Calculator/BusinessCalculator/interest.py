class Interest:
    def simple_interest(self, principle, rate, time):
        SI = (self.principle * self.rate * self.time)/100
        return self.SI

    def compound_interest(self, principle, rate, time):
        amount = principle * (pow((1 + rate / 100), time))
        CI = amount - principle
        return CI
