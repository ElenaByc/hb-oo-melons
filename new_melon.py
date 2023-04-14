from random import randint
from datetime import (date, datetime)

"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly
    def __init__(self, species, qty, country_code=None, tax=0.00):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.tax = tax
        
    @staticmethod
    def get_base_price():
        """Return a random base price, from $5-$9."""
        # Pull date and time from datetime
        day = datetime.now().weekday()
        time = datetime.now().hour
        # add an extra $4 charge to each melon ordered 
        # during morning rush hour (from 8-11am, Monday-Friday)
        base_price = randint(5, 9) 
        print("rand_price = ", base_price)
        if day in range(0,5) and time in range(8,12):
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        fee = 0
        if self.qty < 10 and self.order_type == "domestic":
            fee = 3

        # base_price = 5
        base_price = self.get_base_price()

        if self.species == "christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price + fee
        print("get_total = ", total)
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    # Class level attributes are defined here:
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    #tax = 0.17
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, country_code, 0.17)
        #self.tax = InternationalMelonOrder.tax 



class GovernmentMelonOrder(AbstractMelonOrder):
    # passed_inspection = False
    # Class level attributes are defined here:
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "government")
        # self.species = species
        # self.qty = qty
        # self.order_type = "government"
        # self.tax = 0.00
        self.passed_inspection = False

    
    def mark_inspection(self):
        """Record the fact than an order has been shipped."""

        self.passed_inspection = True


#watermelon = InternationalMelonOrder("watermelon", 10, "USA")

#honeymelon = DomesticMelonOrder("honeymelon", 10)

govermentmelon = GovernmentMelonOrder("govermentmelon", 10)

# print(govermentmelon.get_base_price())
print("tax = ", govermentmelon.tax)

print("total", govermentmelon.get_total())
