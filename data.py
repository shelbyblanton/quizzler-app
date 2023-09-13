import requests

params = {
    "amount": 10,
    "type": "boolean"
}


def get_trivia_bank():
    """Using the `requests` library, retrieve question Quizzler question bank
    from `opentdb.com` via an API call, convert the API response into JSON, and
    return the simplified data to the app.
    :return:
    """
    response = requests.get(url="https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    data = response.json()
    return data['results']


question_data = get_trivia_bank()