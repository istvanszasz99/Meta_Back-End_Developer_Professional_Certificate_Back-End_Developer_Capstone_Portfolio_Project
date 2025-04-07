from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_instance(self):
        menuitem = Menu.objects.create(title="Pepperonata", price=8.99, inventory=20)
        self.assertEqual(str(menuitem), "Pepperonata : 8.99")