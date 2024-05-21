# tests/test_models.py

from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_instance(self):
        item = Menu.objects.create(title="IceCream", price=2, inventory=100)
        self.assertEqual(str(item), "IceCream:2")
