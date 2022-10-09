from what_is_year_now import what_is_year_now
from unittest.mock import patch, MagicMock
from io import StringIO
import pytest


def patch_date(mocked: MagicMock, date: str):
    """Adds the given value as a return value"""
    mocked.return_value = StringIO('{"currentDateTime": "' + date + '"}')


def test_YMD():
    """Testing date in format YYYY-MM-DD"""
    with patch('what_is_year_now.urllib.request.urlopen') as mocked_get_cases:
        patch_date(mocked_get_cases, '2021-10-10')
        assert what_is_year_now() == 2021
        mocked_get_cases.assert_called_once()


def test_DMY():
    """Testing date in format DD.MM.YYYY"""
    with patch('what_is_year_now.urllib.request.urlopen') as mocked_get_cases:
        patch_date(mocked_get_cases, '10.10.2015')
        assert what_is_year_now() == 2015
        mocked_get_cases.assert_called_once()


def test_other():
    """Testing date in other format"""
    with patch('what_is_year_now.urllib.request.urlopen') as mocked_get_cases:
        patch_date(mocked_get_cases, '10-10-2015')
        with pytest.raises(ValueError):
            what_is_year_now()
        mocked_get_cases.assert_called_once()
