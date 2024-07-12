# crm_app/tests.py
import unittest
from django.test import TestCase

class TestLeadModel(TestCase):
    def test_lead_creation(self):
        lead = Lead(name='Test Lead', email='test@example.com')
        lead.save()
        self.assertEqual(Lead.objects.count(), 1)

if __name__ == '__main__':
    unittest.main()