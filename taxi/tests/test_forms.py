from django.test import TestCase

from taxi.forms import DriverCreationForm


class FormsTest(TestCase):
    def test_driver_creation_form_with_licence__names_is_valid(self) -> None:
        form_data = {
            "username": "usertest",
            "password1": "lalo12pasl",
            "password2": "lalo12pasl",
            "license_number": "LWE45642",
            "first_name": "name test",
            "last_name": "last test",

        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
