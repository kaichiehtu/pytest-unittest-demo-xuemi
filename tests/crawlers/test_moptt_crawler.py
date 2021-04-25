import json
import logging
from http import HTTPStatus
from unittest.mock import patch

import pytest
from requests import Session
import requests

from src.crawlers.moptt_crawler import MoPtt


class MockResponse:

    def __init__(self, resp, status_code):
        self.status_code = status_code
        self.resp_json = resp

    def json(self):
        return self.resp_json


@pytest.mark.int_test
def test_real_connect_to_moptt():
    g = MoPtt()
    resp = g.get_hot_posts("Gossiping")
    logging.info(json.dumps(resp, indent=2))
    assert "posts" in resp
    assert isinstance(resp["posts"], list)
    assert len(resp["posts"]) > 0


@patch.object(Session, 'get', return_value=MockResponse({"posts": []}, HTTPStatus.OK))
def test_get_hot_posts(response):
    g = MoPtt()
    resp = g.get_hot_posts("Gossiping")
    logging.debug(resp)
    logging.debug(response)
    assert "posts" in resp
    assert isinstance(resp["posts"], list)


@patch.object(Session, 'get', return_value=MockResponse({}, HTTPStatus.FORBIDDEN))
def test_get_hot_posts_failed(response):
    g = MoPtt()
    with pytest.raises(requests.RequestException):
        resp = g.get_hot_posts("Gossiping")
        assert resp == {}
