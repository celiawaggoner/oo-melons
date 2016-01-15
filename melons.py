"""This file should have our order classes in it."""

from random import randint 
from datetime import datetime

class AbstractMelonOrder(object):
    """Abstract class for our melon orders"""

    def __init__(self, species, qty, country_code = None):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        if self.qty > 100:
            raise TooManyMelonsError
        self.shipped = False

    def get_base_price(self):
        base_price = randint(5, 9) 

        now = datetime.now()
        if now.hour in range(8, 12) and now.weekday() < 5:
            base_price += 4
        
        return base_price


    def get_total(self):
        """Calculate price."""
        base_price = self.get_base_price()

        if self.species == "christmas":
            base_price = 1.5 * base_price

        if self.qty < 10 and self.order_type == "international":
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

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, country_code)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    passed_inspection = False 
    def inspect_melons(self, passed):
        if passed == True:
            self.passed_inspection = True

class TooManyMelonsError(ValueError):
    """Returns an error if order exceeds 100 melons."""

    def __init__(self):
        super(TooManyMelonsError, self).__init__("No more than 100 melons!")



