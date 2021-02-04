#  CYjAX Limited

import datetime
from datetime import timedelta
from unittest.mock import patch, Mock

import pytest
import pytz

import cyjax
from cyjax import LeakedEmail, InvalidDateFormatException


class TestLeakedEmail:

    fake_date = Mock(wraps=datetime.datetime)
    fake_date.now.return_value.astimezone.return_value = datetime.datetime(2020, 5, 2, 12, 0, 0, tzinfo=pytz.UTC)

    def test_get_leaked_emails_without_parameters(self, mocker):
        leaked_email = LeakedEmail()
        spy_method_paginate = mocker.spy(leaked_email, 'paginate')

        leaked_email.list()
        spy_method_paginate.assert_called_once_with(endpoint='data-leak/credentials', params={})

    def test_get_leaked_emails_with_parameters(self, mocker):
        leaked_email = LeakedEmail()
        spy_method_paginate = mocker.spy(leaked_email, 'paginate')

        leaked_email.list(query='search-query', since='2020-05-02T07:31:11+00:00', until='2020-07-02T00:00:00+00:00')

        expected_params = {
            'query': 'search-query',
            'since': '2020-05-02T07:31:11+00:00',
            'until': '2020-07-02T00:00:00+00:00'
        }
        spy_method_paginate.assert_called_once_with(endpoint='data-leak/credentials', params=expected_params)

    @patch('cyjax.helpers.datetime', fake_date)
    def test_get_leaked_emails_with_date_as_timedelta(self, mocker):
        leaked_email = LeakedEmail()
        spy_method_paginate = mocker.spy(leaked_email, 'paginate')

        leaked_email.list(since=timedelta(hours=2), until=timedelta(hours=1))

        since = '2020-05-02T10:00:00+00:00'
        until = '2020-05-02T11:00:00+00:00'
        expected_params = {'since': since, 'until': until}

        spy_method_paginate.assert_called_once_with(endpoint='data-leak/credentials', params=expected_params)

    def test_get_leaked_emails_with_date_as_datetime_without_timezone(self, mocker):
        leaked_email = LeakedEmail()
        spy_method_paginate = mocker.spy(leaked_email, 'paginate')

        leaked_email.list(since=datetime.datetime(2020, 5, 2, 10, 0, 0), until=datetime.datetime(2020, 5, 2, 11, 0, 0))

        since = datetime.datetime(2020, 5, 2, 10, 0, 0).astimezone().isoformat()
        until = datetime.datetime(2020, 5, 2, 11, 0, 0).astimezone().isoformat()
        expected_params = {'since': since, 'until': until}

        spy_method_paginate.assert_called_once_with(endpoint='data-leak/credentials', params=expected_params)

    def test_get_leaked_emails_with_date_as_datetime_with_timezone(self, mocker):
        leaked_email = LeakedEmail()
        spy_method_paginate = mocker.spy(leaked_email, 'paginate')

        leaked_email.list(since=datetime.datetime(2020, 5, 2, 10, 0, 0, tzinfo=pytz.UTC),
                             until=datetime.datetime(2020, 5, 2, 11, 0, 0, tzinfo=pytz.UTC))

        expected_params = {'since': '2020-05-02T10:00:00+00:00', 'until': '2020-05-02T11:00:00+00:00'}

        spy_method_paginate.assert_called_once_with(endpoint='data-leak/credentials', params=expected_params)

    def test_get_leaked_emails_with_date_as_string(self, mocker):
        leaked_email = LeakedEmail()
        spy_method_paginate = mocker.spy(leaked_email, 'paginate')

        leaked_email.list(since='2020-05-02T10:00:00+00:00', until='2020-05-02T11:00:00+00:00')

        expected_params = {'since': '2020-05-02T10:00:00+00:00', 'until': '2020-05-02T11:00:00+00:00'}

        spy_method_paginate.assert_called_once_with(endpoint='data-leak/credentials', params=expected_params)

    def test_get_leaked_emails_with_wrong_date(self):
        leaked_email = LeakedEmail()
        with pytest.raises(InvalidDateFormatException):
            leaked_email.list(since='2020-05', until='2020-05-02T11:00:00+00:00')

        with pytest.raises(InvalidDateFormatException):
            leaked_email.list(since='2020-05-02T11:00:00+00:00', until='2020-05')

    def test_setting_client(self):
        cyjax.api_key = None  # reset to defaults

        resource = LeakedEmail()
        assert 'https://api.cyberportal.co' == resource._api_client.get_api_url()
        assert resource._api_client.get_api_key() is None

        resource = LeakedEmail('123456', 'https://api.new-address.com')
        assert 'https://api.new-address.com' == resource._api_client.get_api_url()
        assert '123456' == resource._api_client.get_api_key()

        cyjax.api_url = None  # Reset to default

    def test_get_one_by_id(self, mocker):
        resource = LeakedEmail()
        resource._api_client = Mock()

        spy_method_get_one_by_id = mocker.spy(resource, 'get_one_by_id')

        assert hasattr(resource, 'one')
        resource.one(400)

        spy_method_get_one_by_id.assert_called_once_with(endpoint='data-leak/credentials', record_id=400)
