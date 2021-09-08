import requests

API_END_POINT = ""


class TwitterRepository:

    @staticmethod
    def search(hashtag: str):
        _api_resource = 'tweets'
        requests.get(f"{API_END_POINT}/{_api_resource}")
