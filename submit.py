import json
from logging import info


def submit():
    # Submits the user data for validation

    with open('./data.json', 'r') as d:
        j = json.load(d)

        j['submit_confirmation'] = False
        res = requests.post(url, json=j + token)

        info(res.json())

