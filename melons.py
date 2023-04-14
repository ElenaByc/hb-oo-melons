"""Classes for melon orders."""


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because
    # AbstractMelonOrder should never be instantiated directly

    # order_type = None
    # tax = 0

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder:
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #     self.shipped = False
    #     self.order_type = "domestic"
    #     self.tax = 0.08

        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder:
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        # self.country_code = country_code
        # self.shipped = False
        # self.order_type = "international"
        # self.tax = 0.17

        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
