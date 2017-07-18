from unittest import TestCase, main
from server import app, show_homepage, show_register_form


class FlaskTests(TestCase):

    def setUp(self):
        """Performs this before all tests"""

        self.client = app.test_client()
        app.config["TESTING"] = True

    def tearDown(self):
        """Performs this after all tests"""

    def test_show_homepage(self):
        """Tests whether homepage displays"""

        result = self.client.get("/")
        self.assertIn("test your knowledge.", result.data)

    def test_show_register_form(self):
        """Tests whether registration form shows."""

        result = self.client.get("/register")
        self.assertIn("Register", result.data)



if __name__ == "__main__":
    main()

