from io import StringIO
import contextlib
from unittest import mock

from weather import get_weather


dummy_response = '''
{
    "location": null,
    "forecasts": [
        {
            "date": "2018-02-22",
            "dateLabel": "今日",
            "telop": "曇り",
        },
        {
            "date": "2018-02-23",
            "dateLabel": "明日",
            "telop": "晴れ",
        },
    ],
    "status": 200
}
'''


@contextlib.contextmanager
def dummy_open(url):
    sio = StringIO()
    print('test=', dummy_response.encode('utf-8'))
    sio.write(dummy_response)
    sio.seek(0)
    yield sio


@mock.patch('urllib.request.urlopen', side_effect=dummy_open)
def test_get_address(m):
    actual = get_weather('130010')
    expected = '曇り'
    assert actual == expected
