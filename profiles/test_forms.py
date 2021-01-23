from django.test import TestCase
from profiles.forms import UserProfileForm


class TestUserProfileForm(TestCase):

    def test_user_profile_form_not_required_data(self):
        valid_data = {
                'default_phone_number': '',
                'default_postcode': '',
                'default_town_or_city': '',
                'default_address_line1': '',
                'default_address_line2': '',
                'default_county': '',
        }
        form = UserProfileForm(data=valid_data)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_user_profile_form_metaclass(self):

        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))
