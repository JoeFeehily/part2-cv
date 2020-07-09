from django.urls import resolve
from django.test import TestCase
from cvsite.views import mainsite  

class SectionListTest(TestCase):

    def test_root_url_resolves_to_mainsite_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, mainsite)