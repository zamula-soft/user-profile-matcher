class ExternalServiceListCampaigns:
    """Mocked external service to get list of current campaigns"""
    @staticmethod
    def get_list_campaigns():
        return [
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
            }
        ]
