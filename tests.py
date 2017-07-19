from unittest import TestCase, main
from server import app, show_homepage, show_register_form, show_study_notes
from model import db, sample_data, connect_to_db


class FlaskTests(TestCase):
    """Tests the webpages"""

    def setUp(self):
        """Performs this before all tests"""

        self.client = app.test_client()
        app.config["TESTING"] = True

    def tearDown(self):
        """Performs this after all tests"""

        # might not need

    def test_show_homepage(self):
        """Tests whether homepage displays"""

        result = self.client.get("/")
        self.assertIn("test your knowledge.", result.data)

    def test_show_register_form(self):
        """Tests whether registration form shows."""

        result = self.client.get("/register")
        self.assertIn("Register", result.data)


class DatabaseTests(TestCase):
    """Tests the database"""

    def setUp(self):
        """Performs this before each test."""

        self.client = app.test_client()
        app.config["TESTING"] = True
        app.config["SECRET_KEY"] = "code"

        with self.client as c:
            with c.session_transaction() as sess:
                sess['current_user'] = "user"

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        db.create_all()

        # Put in sample data
        sample_data()

    def tearDown(self):
        """Performs after each test"""

        db.session.close()
        db.drop_all()
    
    def test_add_username(self):
        """Tests add user"""

        result = self.client.get("/user/info")
        self.assertIn("testf testl", result.data)

    def test_add_module(self):
        """Tests add module"""

        result = self.client.get("/user/studynotes")
        self.assertIn("testmod", result.data)






if __name__ == "__main__":
    main()

