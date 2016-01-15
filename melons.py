"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Abstract class for our melon orders"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price."""
        base_price = 5

        if self.species == "christmas":
            base_price = 1.5*base_price

        if self.quantity < 10 and self.order_type == "international":
            total = (1 + self.tax) * self.qty * base_price + 3
        else:
            total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

        return "Your order has been shipped."


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    passed_inspection = False 
    def inspect_melons(self, passed):
        if passed == True:
            self.passed_inspection = True



