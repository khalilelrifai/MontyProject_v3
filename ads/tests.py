from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from decimal import Decimal
from .models import Ad

class AdModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_ad_creation(self):
        ad = Ad.objects.create(
            title='Test Ad',
            price=Decimal('10.00'),
            text='This is a test ad.',
            owner=self.user
        )

        # verify that the Ad object was created correctly
        self.assertEqual(ad.title, 'Test Ad')
        self.assertEqual(ad.price, Decimal('10.00'))
        self.assertEqual(ad.text, 'This is a test ad.')
        self.assertEqual(ad.owner, self.user)

        # verify that the created_at and updated_at fields were set automatically
        self.assertIsNotNone(ad.created_at)
        self.assertIsNotNone(ad.updated_at)

    def test_title_validation(self):

        # test that a title with 2 or more characters does not raise a ValidationError
        ad = Ad.objects.create(
            title='Test Ad',
            price=Decimal('10.00'),
            text='This is a test ad.',
            owner=self.user
        )
        self.assertEqual(ad.title, 'Test Ad')
