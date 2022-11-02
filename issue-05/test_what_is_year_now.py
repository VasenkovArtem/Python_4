import urllib

from what_is_year_now import what_is_year_now, API_URL
from unittest.mock import patch
from io import StringIO
import pytest


def test_YMD():
    """Testing date in format YYYY-MM-DD"""
    str_date = StringIO('{"currentDateTime": "2021-10-10"}')
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=str_date) as mocked_get_cases:
        assert what_is_year_now() == 2021
        mocked_get_cases.assert_called_once()


def test_DMY():
    """Testing date in format DD.MM.YYYY"""
    str_date = StringIO('{"currentDateTime": "10.10.2015"}')
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=str_date) as mocked_get_cases:
        assert what_is_year_now() == 2015
        mocked_get_cases.assert_called_once()


def test_other_format():
    """Testing date in other format"""
    str_date = StringIO('{"currentDateTime": "10-10-2015"}')
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=str_date) as mocked_get_cases:
        with pytest.raises(ValueError):
            what_is_year_now()
        mocked_get_cases.assert_called_once()


def test_API_error():
    """Testing case when API returns error"""
    http_error = urllib.error.HTTPError(API_URL, None, None, None, None)
    with patch('what_is_year_now.urllib.request.urlopen',
               side_effect=http_error) as mocked_get_cases:
        with pytest.raises(urllib.error.HTTPError):
            what_is_year_now()
        mocked_get_cases.assert_called_once()


def test_json_invalid():
    """Testing case when json hasn't key 'currentDateTime'"""
    str_date = StringIO('{"currentDate": "10-10-2015"}')
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=str_date) as mocked_get_cases:
        with pytest.raises(KeyError):
            what_is_year_now()
        mocked_get_cases.assert_called_once()
