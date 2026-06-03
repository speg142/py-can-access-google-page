import unittest
from unittest.mock import patch
from app.main import can_access_google_page


class TestCanAccessGooglePage(unittest.TestCase):
    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_valid_url_and_connection_exists(self,
                                             mock_url: bool,
                                             mock_internet: bool
                                             ) -> None:
        mock_url.return_value = True
        mock_internet.return_value = True
        self.assertTrue(can_access_google_page("https://www.google.com"),
                        "Accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_valid_url_exists(self,
                              mock_url: bool,
                              mock_internet: bool
                              ) -> None:
        mock_url.return_value = True
        mock_internet.return_value = False
        self.assertTrue(can_access_google_page("https://www.google.com"),
                        "Not accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_connection_exists(self,
                               mock_url: bool,
                               mock_internet: bool
                               ) -> None:
        mock_url.return_value = False
        mock_internet.return_value = True
        self.assertTrue(can_access_google_page("https://www.google.com"),
                        "Not accessible")

    @patch("app.main.has_internet_connection")
    @patch("app.main.valid_google_url")
    def test_can_access_google_page_both_false(self,
                                               mock_url: bool,
                                               mock_internet: bool
                                               ) -> None:
        mock_url.return_value = False
        mock_internet.return_value = False
        self.assertTrue(can_access_google_page("https://www.google.com"),
                        "Not accessible")
