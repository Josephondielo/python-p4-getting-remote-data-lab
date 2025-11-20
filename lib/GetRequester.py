import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send GET request and return response as a string."""
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text  # string, not bytes

    def load_json(self):
        """Return the JSON response as Python object (list/dict)."""
        response_body = self.get_response_body()
        return json.loads(response_body)
