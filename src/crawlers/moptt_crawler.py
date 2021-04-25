from http import HTTPStatus
import requests


class MoPtt:

    def __init__(self):
        self.headers = {
            "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"),
            "Authorization": "cMIS1Icr95gnR2U19hxO2K7r6mYQ96vp"
        }
        self.base_url = "https://moptt.azurewebsites.net/api/v2/hotpost"
        self.session = requests.Session()

    def get_hot_posts(self, topic_name: str) -> requests.Response.json:
        """
        Returns:
            resp (json):
                {
                    "posts":[
                        {
                            "_id":"607ed8a09d132e2b9c7b566d",
                            "title":"[新聞] 拋街道正名議題！柯文哲：立法院被大陸包",
                            "author":"proprome",
                            "board":"Gossiping",
                            "timestamp":"2021-04-20T12:31:25.000Z",
                            "url":"https://www.ptt.cc/bbs/Gossiping/M.1618921888.A.7A1.html",
                            "hits":1853,
                            "description": "拋街道正名議題！\u3000柯文哲：立法院被大陸包圍 "
                                "https://news.tvbs.com.tw/politics/1496256 記者 柳采葳 / 攝影 崔重群 報導 "
                                "https://cc.tvbs.com.tw/img/upload/2021/04/20/20210420181522-5551347f.jpg…",
                            "cover":"Gossiping.M.1618921888.A.7A1.jpg",
                            "acceptedDate":"2021-04-20T13:35:26.985Z",
                            "image":"https://moptt.blob.core.windows.net/post-covers"
                            "/200/Gossiping.M.1618921888.A.7A1.jpg"
                        },
                        ...
                    ],
                    "nextPage":{
                        "skip":20
                    }
                }
        """
        url = f"{self.base_url}?b={topic_name}"
        resp = self.session.get(url, headers=self.headers)
        if resp.status_code == HTTPStatus.OK:
            return resp.json()
        raise requests.RequestException(f"request status = [{resp.status_code}]")
