from django.urls import resolve
from django.test import TestCase
from cvsite.views import section_list  

class SectionListTest(TestCase):

    def test_root_url_resolves_to_section_list_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, section_list)