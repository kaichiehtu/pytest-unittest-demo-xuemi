import json
import logging

import pytest
from src.crawlers.moptt_crawler import MoPtt


def _require_fields(resp):
    fields = ["posts", "nextPage"]
    for f in fields:
        logging.debug("exp=[%s], actual=[%s]", f, resp)
        assert f in resp


def _posts_required_field(post: list):
    """
    "_id": "66fec752dd082d1974be8592",
            "title": "[問卦] 基隆現在還在下暴雨~確定正常上班上課?",
            "author": "enlong777",
            "board": "Gossiping",
            "timestamp": "2024-10-03T15:17:39.000Z",
            "url": "https://www.ptt.cc/bbs/Gossiping/M.1727968661.A.202.html",
            "hits": 1367,
            "description": "https://imgur.com/a/3pWMblu 剛收到通知 又是強降雨警報 基隆下午四點已經破歷史降雨紀錄 現在飆升到快400毫米 隔壁的瑞芳就不用說 直接飆到636毫米 直接打破歷史紀錄 瑞…",
            "cover": "Gossiping.M.1727968661.A.202.jpg",
            "acceptedDate": "2024-10-03T16:33:22.171Z",
            "image": "https://moptt.blob.core.windows.net/post-covers/200/Gossiping.M.1727968661.A.202.jpg"
    """
    fields = ["_id", "title", "author", "board", "timestamp", "url", "hits", "description", "cover", "acceptedDate", "image"]
    for f in fields:
        logging.debug("posts exp=[%s], actual=[%s]", f, post)
        assert f in post


@pytest.mark.int_test
def test_real_connect_to_moptt():
    resp = MoPtt().get_hot_posts("Gossiping")
    logging.info(json.dumps(resp, indent=2))
    #verify
    _require_fields(resp)
    _posts_required_field(resp["posts"][0])
    assert len(resp["posts"]) > 0

@pytest.mark.int_test
def test_real_connect_to_moptt_with_fail():

    with pytest.raises(AssertionError):
        resp = MoPtt().get_hot_posts("ccccccc")
        logging.debug(resp)
        #verify
        _require_fields(resp)
        assert len(resp["posts"]) > 0
        _posts_required_field(resp["posts"][0])