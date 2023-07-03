from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from ..models import Menu
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Pizza", price=100, inventory=50)
        self.menu2 = Menu.objects.create(title="Burger", price=80, inventory=30)

    def test_get_all(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
