from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemView


class MenuItemViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=200, inventory=10)
        Menu.objects.create(title="Cake", price=150, inventory=10)
        Menu.objects.create(title="Pasta", price=200, inventory=10)
    
    def test_getall(self):
        view = MenuItemView()
        queryset = view.get_queryset()
        serializer_class = view.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        expected_data = [
            {
                'title': 'Pizza',
                'price': '200.00',
                'inventory': 10
            },
            {
                'title': 'Cake',
                'price': '150.00',
                'inventory': 10
            },
            {
                'title': 'Pasta',
                'price': '200.00',
                'inventory': 10
            }
        ]
        self.assertEqual(serializer.data, expected_data)
