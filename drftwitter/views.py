from django.http import HttpResponse


def tweets_by_hashtag(request, keyword: str):
    return HttpResponse('Hello, World!' + keyword)
