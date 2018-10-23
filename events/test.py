import json
import requests


def read_events():
    with open('sample_data.json', 'r') as f:
        body = f.read()
        return json.loads(body)


if __name__ == '__main__':
    events = read_events()
    r = requests.post('http://webhook:5000/events', json=events);
    r.raise_for_status()
    print('Events succesfully sent')

