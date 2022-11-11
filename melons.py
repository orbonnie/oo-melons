# from calendar import weekday
from random import randint
from datetime import datetime

class TooManyMelonsError(ValueError):
    def __str__(self):
        return ("No more than 100 melons!")

"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    order_type = None
    tax = 0

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.time = None
        self.day = datetime.now().weekday()
        self.rush: False
        self.check_order_qty()
        self.set_date()
        self.check_rush_hour()

    def get_base_price(self):
        return randint(5, 9)

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        print(f'The base price for this order is {base_price}')
        if self.species.lower() == "christmas":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3

        if self.rush: total += 4

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def check_order_qty(self):
        if self.qty > 100:
            raise TooManyMelonsError

    def set_date(self):
        stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.time = tuple([int(x) for x in stamp.split(' ')[1].split(':')])

    def check_rush_hour(self):
        if self.day < 5:
            if (self.time[0] in range(8, 11) or
               (self.time[0] == 11 and self.time[1] == 0)):
                self.rush = True




class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)

        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """An US government melon order."""

    def __int__(self, species, qty):
        super().__init__(species, qty)

        self.passed_inspection = False
        self.shipped = False
        self.order_type = "government"
        self.tax = 0

    def mark_inspection(self, passed):
        self.passed_inspection = passed

