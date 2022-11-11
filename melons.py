"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because
    # AbstractMelonOrder should never be instantiated directly

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == "Christmas":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        #checks for international order_type
        if self.order_type == 'international' and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    order_type = None
    tax = 0


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