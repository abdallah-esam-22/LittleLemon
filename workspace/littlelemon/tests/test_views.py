from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="small burger", price=2, inventory=30)
        self.item2 = Menu.objects.create(title="medium burger", price=2.50, inventory=25)
        self.item3 = Menu.objects.create(title="large burger", price=3, inventory=20)
        
    def test_getall(self):
        response = self.client.get(reverse("menu-list"))
        items = Menu.objects.all()
        final_items = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data , final_items.data)