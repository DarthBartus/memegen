from unittest import TestCase
from generator_domain.validator import Validator
from generator_domain.exceptions import ValidationError


class ValidatorTest(TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_validate_ratio(self):
        image_dimensions = {'width': 1920, 'height': 1080}
        validated_data = self.validator.validate_ratio(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 800, 'height': 600}
        validated_data = self.validator.validate_ratio(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 600, 'height': 600}
        validated_data = self.validator.validate_ratio(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 1, 'height': 15000}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_ratio(image_dimensions)

        image_dimensions = {'width': 15000, 'height': 1}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_ratio(image_dimensions)

    def test_validate_size(self):

        image_dimensions = {'width': 500, 'height': 500}
        validated_data = self.validator.validate_size(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 1500, 'height': 500}
        validated_data = self.validator.validate_size(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 500, 'height': 1500}
        validated_data = self.validator.validate_size(image_dimensions)
        self.assertEqual(validated_data, image_dimensions)

        image_dimensions = {'width': 1, 'height': 15000}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_size(image_dimensions)

        image_dimensions = {'width': 15000, 'height': 1}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_size(image_dimensions)

        image_dimensions = {'width': 15000, 'height': 15000}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_size(image_dimensions)

    def test_validate_mimetype(self):

        image_mime = {'mimetype': 'image/jpeg'}
        validated_data = self.validator.validate_mimetype(image_mime)
        self.assertEqual(validated_data, image_mime)

        image_mime = {'mimetype': 'image/png'}
        validated_data = self.validator.validate_mimetype(image_mime)
        self.assertEqual(validated_data, image_mime)

        image_mime = {'mimetype': 'image/gif'}
        validated_data = self.validator.validate_mimetype(image_mime)
        self.assertEqual(validated_data, image_mime)

        image_mime = {'mimetype': 'image/tiff'}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_mimetype(image_mime)

        image_mime = {'mimetype': 'application/json'}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_mimetype(image_mime)

        image_mime = {'mimetype': 'text/html'}
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_mimetype(image_mime)

    def test_should_raise_validation_error_on_text_too_long(self):

        image_data = {"top_text": "Short text", "bottom_text": "Short text"}
        validated_data = self.validator.validate_length(image_data)
        self.assertEqual(validated_data, image_data)

        image_data = {"top_text": "Text of reasonable length", "bottom_text": "Tex of reasonable length"}
        validated_data = self.validator.validate_length(image_data)
        self.assertEqual(validated_data, image_data)

        image_data = {"top_text": "", "bottom_text": ""}
        validated_data = self.validator.validate_length(image_data)
        self.assertEqual(validated_data, image_data)

        image_data = {
            "top_text": "Text that is needleslly, overly long. It needs to be at the very least 51 characters long. I hope I already hit that limit.",
            "bottom_text": "Text that is needleslly, overly long. It needs to be at the very least 51 characters long. I hope I already hit that limit.",
        }
        with self.assertRaises(ValidationError):
            validated_data = self.validator.validate_length(image_data)

    def test_validator(self):

        image_data = {
            'mimetype': 'image/jpeg',
            'width': 800,
            'height': 600,
        }
        try:
            self.validator(image_data)
        except ValidationError:
            self.fail("Validator failed to validate image data!")
