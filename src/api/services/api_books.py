# os
import os

# asynnc io
import asyncio
import httpx

loop = asyncio.get_event_loop()


async def get_books_google(query):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            os.environ.get("GOOGLE_API_BOOKS_URL")+"/?q="+query+"&key="+os.environ.get("GOOGLE_API_KEY"))
        return format_response_google(response.json())


async def get_books_others(params):
    print("external api")


def get_books_external_api(query):
    task = [
        get_books_google(query),
        get_books_others(query)
    ]
    loop.run_until_complete(asyncio.wait(task))
    print("termino todo")
    return []


def format_response_google(data):
    print(
        list(map(lambda item: {
            'title': item['volumeInfo']['title'],
            'sub_title': item['volumeInfo']['subtitle'] if 'subtitle' in item['volumeInfo'].keys() else None,
            'authors': item['volumeInfo']['authors'] if 'authors' in item['volumeInfo'].keys() else [],
            'categories': item['volumeInfo']['categories'] if 'categories' in item['volumeInfo'].keys() else [],
            'description': item['searchInfo']['textSnippet'] if 'textSnippet' in item['searchInfo'].keys() else None,
        }, data['items'])))
    # for dat in data['items']:
    #     print(dat)
    return []
