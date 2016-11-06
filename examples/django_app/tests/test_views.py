from django.test import TestCase
from django.core.exceptions import ValidationError
from chatterbot.ext.django_chatterbot.views import ChatterBotView, ChatterBotTrainingView


class ChatterBotViewTestCase(TestCase):

    def setUp(self):
        super(ChatterBotViewTestCase, self).setUp()
        self.view = ChatterBotView()

    def test_validate_text(self):
        try:
            self.view.validate({
                'text': 'How are you?'
            })
        except ValidationError:
            self.fail('Test raised ValidationError unexpectedly!')

    def test_validate_invalid_text(self):
        with self.assertRaises(ValidationError):
            self.view.validate({
                'type': 'classmethod'
            })


class TrainingViewTestCase(TestCase):

    def setUp(self):
        super(TrainingViewTestCase, self).setUp()
        self.view = ChatterBotTrainingView()

    def test_invalid_training_data(self):
        pass

    def test_valid_training_data(self):
        pass