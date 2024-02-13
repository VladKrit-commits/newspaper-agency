from django.test import TestCase

from agency.forms import RedactorsCreationForm


class FormsTest(TestCase):
    def test_redactor_creation_form_with_years_of_experience_first_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 12
        }
        form = RedactorsCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
