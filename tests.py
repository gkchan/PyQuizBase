from unittest import TestCase, main
from server import app, show_homepage, show_register_form, show_study_notes
from model import db, sample_data, connect_to_db


def set_user_login(self):
    """Simulates login to test page views that require a login"""

    with self.client as c:
            with c.session_transaction() as sess:
                sess['current_user'] = "user"


class FlaskTests(TestCase):
    """Tests the webpages"""

    def setUp(self):
        """Performs this before all tests"""

        self.client = app.test_client()
        app.config["TESTING"] = True

        set_user_login(self)

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

    def test_show_login(self):
        """Tests whether login page shows."""

        result = self.client.get("/login")
        self.assertIn("Login", result.data)

    def test_show_dashboard(self):
        """Tests whether dashboard shows."""

        result = self.client.get("/user/dashboard")
        self.assertIn("user's Dashboard", result.data)

    def test_show_add_module(self):
        """Tests whether add module page shows"""

        result = self.client.get("/user/addmodules")
        self.assertIn("Add New Function Info", result.data)

    def test_show_delete_functions(self):
        """Tests whether delete functions page shows"""

        result = self.client.get("/user/delete")
        self.assertIn("Delete functions", result.data)

    def test_show_delete_modules(self):
        """Tests whether delete modules shows"""

        result = self.client.get("/user/delete")
        self.assertIn("Delete modules", result.data)


class DatabaseTests(TestCase):
    """Tests the database and pages that require a database"""

    def setUp(self):
        """Performs this before each test."""

        self.client = app.test_client()
        app.config["TESTING"] = True
        app.config["SECRET_KEY"] = "code"

        set_user_login(self)

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        db.create_all()

        # Put in sample data
        sample_data()

    def tearDown(self):
        """Performs after each test"""

        db.session.close()
        db.drop_all()

    def test_registration(self):
        """Tests registration form function"""

        result = self.client.post("/register", data={"username":"u", "password":"pw", "firstname":"first", "lastname":"la", "email":"e"})
        self.assertIn("You have registered", result.data)
    
    def test_user_info_page(self):
        """Tests whether user info page shows."""

        result = self.client.get("/user/info")
        self.assertIn("user's Information", result.data)

    def test_show_user_info(self):
        """Tests whether user info shows."""

        result = self.client.get("/user/info")
        self.assertIn("testf testl", result.data)

    def test_show_user_info_email(self):
        """Test whether e-mail shows on user info page"""

        result = self.client.get("/user/info")
        self.assertIn("test@gmail.com", result.data)

    def test_show_user_info_level(self):
        """Test whether level shows on user info page"""

        result = self.client.get("/user/info")
        self.assertIn("5", result.data)

    def test_study_notes(self):
        """Test whether study table page shows."""

        result = self.client.get("/user/studynotes")
        self.assertIn("Modules/Functions Info", result.data)

    def test_show_module(self):
        """Tests whether module info shows."""

        result = self.client.get("/user/studynotes")
        self.assertIn("testmod", result.data)

    def test_show_function(self):
        """Tests whether function shows"""

        result = self.client.get("/user/studynotes")
        self.assertIn("func", result.data)

    def test_show_description(self):
        """Tests whether module description shows"""

        result = self.client.get("/user/studynotes")
        self.assertIn("moddesc", result.data)

    # Note: Goes to a redirect, not actual page
    
    def test_add_module_function(self):
        """Tests whether adding a function loads redirect"""

        result = self.client.post("/user/addmodules", data={"mname":"mod", "mdesc":"desc", "fname":"func", "fdesc":"desc"})
        self.assertIn("Redirect", result.data)
        self.assertEqual(result.status_code, 302)

    # Note: add more sample data in test database to test quiz

    def test_show_question(self):
        """Tests whether quiz question shows."""

        result = self.client.get("/user/quiz")
        self.assertIn("Question", result.data)







if __name__ == "__main__":
    main()

