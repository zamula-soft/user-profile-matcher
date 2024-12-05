import requests
import json

class ExternalServiceListCampaigns:
    """Mocked external service to get list of current campaigns"""

    @staticmethod
    def get_list_campaigns():
        """Get list campaigns data from external API service"""
        api_url = '/get_list_campaigns/'
        response = requests.get(api_url)
        data = json.loads(response.text)
        return data

    @staticmethod
    def get_list_campaigns_data():
        mock_data = [
            {
                "game": "mygame",
                "name":"mycampaign",
                "priority": 10.5,
                "matchers": {
                    "level": {
                        "min": 1,
                        "max": 3
                    },
                    "has": {
                        "country": ["US","RO","CA"],
                        "items": ["item_1"]
                    },
                    "does_not_have": {
                        "items": ["item_4"]
                    },
                },
                "start_date": "2022-01-25 00:00:00Z",
                "end_date": "2022-02-25 00:00:00Z",
                "enabled": True,
                "last_updated": "2021-07-13 11:46:58Z"
            },
            {
                "game": "mygame",
                "name": "mycampaign1",
                "priority": 10.5,
                "matchers": {
                    "level": {
                        "min": 1,
                        "max": 3
                    },
                    "has": {
                        "country": ["US", "RO", "CA"],
                        "items": ["item_1"]
                    },
                    "does_not_have": {
                        "items": ["item_34"]
                    },
                },
                "start_date": "2022-01-25 00:00:00Z",
                "end_date": "2022-02-25 00:00:00Z",
                "enabled": True,
                "last_updated": "2021-07-13 11:46:58Z"
            }
        ]

        return mock_data


# class TestGetData(unittest.TestCase):
#     @patch('get_list_campaigns')
#     def mocking_data_for_external_api(self, mock_get_data):
#         """
#         Test that get_data() returns the correct data demonstrating the
#         use of the mock library
#         """
#
#         mock_data = get_list_campaigns_data()#
#         mock_get_data.return_value = Mock()#
#         mock_get_data.return_value.json.return_value = mock_data
#         mock_get_data.return_value.status_code = 200
