from GetRequester import GetRequester

URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

# Use string, not bytes
JSON_STRING = """[
  {
    "name": "Daniel",
    "occupation": "LG Fridge Salesman"
  },
  {
    "name": "Joe",
    "occupation": "WiFi Fixer"
  },
  {
    "name": "Avi",
    "occupation": "DJ"
  },
  {
    "name": "Howard",
    "occupation": "Mountain Legend"
  }
]
"""

CONVERTED_DATA = [
    { 'name': 'Daniel', 'occupation' : 'LG Fridge Salesman' },
    { 'name': 'Joe', 'occupation': 'WiFi Fixer' },
    { 'name': 'Avi', 'occupation': 'DJ' },
    { 'name': 'Howard', 'occupation': 'Mountain Legend' }
]

def test_get_response():
    requester = GetRequester(URL)
    assert requester.get_response_body() == JSON_STRING  # call method with ()

def test_load_json():
    requester = GetRequester(URL)
    assert requester.load_json() == CONVERTED_DATA
