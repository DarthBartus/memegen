import os

from unittest import TestCase
from generator_domain.generator import Generator

image_b64 = "/9j/4AAQSkZJRgABAQEBLAEsAAD//gATQ3JlYXRlZCB3aXRoIEdJTVD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wgARCADIAMgDAREAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAj/xAAUAQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIQAxAAAAGqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//EABQQAQAAAAAAAAAAAAAAAAAAAJD/2gAIAQEAAQUCHH//xAAUEQEAAAAAAAAAAAAAAAAAAACQ/9oACAEDAQE/ARx//8QAFBEBAAAAAAAAAAAAAAAAAAAAkP/aAAgBAgEBPwEcf//EABQQAQAAAAAAAAAAAAAAAAAAAJD/2gAIAQEABj8CHH//xAAUEAEAAAAAAAAAAAAAAAAAAACQ/9oACAEBAAE/IRx//9oADAMBAAIAAwAAABCSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSf/8QAFBEBAAAAAAAAAAAAAAAAAAAAkP/aAAgBAwEBPxAcf//EABQRAQAAAAAAAAAAAAAAAAAAAJD/2gAIAQIBAT8QHH//xAAUEAEAAAAAAAAAAAAAAAAAAACQ/9oACAEBAAE/EBx//9k="
current_path = os.path.dirname(os.path.realpath('__name__'))
rel_path = "fonts/impact.ttf"
font_path = os.path.join(current_path, rel_path)


class GeneratorTest(TestCase):

    def setUp(self):
        self.generator = Generator()
        self.font = open(font_path, "rb")
        self.image_data = {
            "width": 200,
            "height": 200,
            "base64": image_b64,
            "top_text": '',
            "bottom_text": '',
            "font": self.font,
            "mimetype": "image/jpeg",
        }

    def test_should_return_same_image_when_no_text(self):
        processed_image = self.generator(self.image_data).get("base64")
        self.assertEqual(processed_image, image_b64)

    def test_generates_new_image_when_given_text(self):

        self.image_data["top_text"] = "TEST TEST TEST"
        self.image_data["bottom_text"] = "TEST TEST TEST"

        self.generator(self.image_data)

        self.assertNotEqual(self.image_data.get("base64"), image_b64)
