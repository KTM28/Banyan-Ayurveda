from django.test import TestCase
from newsletters.forms import MarketingEmailSubForm
from newsletters.models import MarketingSubs


class TestMarketingEmailSubForm(TestCase):

    def test_marketing_sub_form(self):

        form = MarketingEmailSubForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('email', form.errors.keys())

    def test_marketing_sub_form_meta(self):

        form = MarketingEmailSubForm()
        self.assertEqual(
            form.Meta.fields, ('email',)
            )
