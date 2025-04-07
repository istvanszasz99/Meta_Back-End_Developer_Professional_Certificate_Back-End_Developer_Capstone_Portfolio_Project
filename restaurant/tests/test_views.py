from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def test_setup(self):
        Menu.objects.create(title="Pasta", price=12.99, inventory=10)
        Menu.objects.create(title="Pizza", price=9.99, inventory=15)
        Menu.objects.create(title="Salad", price=7.99, inventory=20)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menus = Menu.objects.all()
        serialized_menus = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized_menus.data)