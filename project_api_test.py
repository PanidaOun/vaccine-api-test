import unittest
import requests
"""Test for reservation API."""

class reservationApiTest(unittest.TestCase):
    """Class to test feature about get reservation by ID."""

    def test_get_reservation_by_ID(self):
        """Test if user can get reservation by input specific ID. """
        response = requests.get("https://flamxby.herokuapp.com/reservation/4")
        self.assertEqual(response.status_code, 200)

    def test_get_reservation_by_ID_using_uncorrect_link(self):
        """Test if user can get reservation by input uncorrect link."""
        response = requests.get("https://flamxby.herokuapp.com/reservation/aaa")
        self.assertEqual(response.status_code, 422)

    def test_get_reservation_by_ID_check_content_type_equals_json(self):
        """Test when user get reservation by input specific ID and the outcome is json format."""
        response = requests.get("https://flamxby.herokuapp.com/reservation/4")
        self.assertEqual(response.headers["Content-Type"], "application/json")
        
    def test_get_reservation_by_ID_equals_specific_ID(self):
        """Test when user get reservation by input specific ID and the outcome is the correct reservation."""
        response = requests.get("https://flamxby.herokuapp.com/reservation/4")
        response_body = response.json()
        self.assertEqual(response_body["reservation_id"], 4)

    def test_get_unvalid_reservation_by_ID(self):
        """Test when user get reservation by input unvalid ID."""
        response = requests.get("https://flamxby.herokuapp.com/reservation/5000")
        self.assertEqual(response.status_code, 404)

    def test_get_unvalid_reservation_by_ID_given_message_error(self):
        """Test when user get reservation by input unvalid ID and the outcome is the message error"""
        response = requests.get("https://flamxby.herokuapp.com/reservation/5000")
        response_body = response.json()
        self.assertEqual(response_body,{'detail': 'No reservation with this id'})


if __name__ == '__main__':
    unittest.main()