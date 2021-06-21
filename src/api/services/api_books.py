# os
import os

# request lib
import requests

# format string url params
from urllib.parse import quote


def get_books_google(query):
    """ get google  api books list """

    response = requests.get(
        os.environ.get("GOOGLE_API_BOOKS_URL")+"/?q="+quote(query)+"&key="+os.environ.get("GOOGLE_API_KEY"))
    return format_response_google(response.json())


def get_books_open_lib(query):
    """ get open api books list """

    response = requests.get(
        os.environ.get("OPEN_LIBRARY_API")+quote(query))
    return format_response_open_library(response.json())


def get_books_external_api(query):
    """ consulting books in apis externals """

    google_api_response = get_books_google(query)
    if len(google_api_response) > 0:
        return google_api_response
    else:
        other_api_response = get_books_open_lib(query)
        return other_api_response


def format_response_google(data):
    """ formatter data from google api books """

    if len(data) > 0:
        return list(map(lambda item: {
            'title': item['volumeInfo']['title'],
            'sub_title': item['volumeInfo']['subtitle'] if 'subtitle' in item['volumeInfo'].keys() else None,
            'authors': item['volumeInfo']['authors'] if 'authors' in item['volumeInfo'].keys() else [],
            'categories': item['volumeInfo']['categories'] if 'categories' in item['volumeInfo'].keys() else [],
            'description': item['searchInfo']['textSnippet'] if 'searchInfo' in item.keys() and 'textSnippet' in item['searchInfo'].keys() else None,
            'publish_date':  item['volumeInfo']['publishedDate'] if 'publishedDate' in item['volumeInfo'].keys() else None,
            'editor':  item['volumeInfo']['publisher'] if 'publisher' in item['volumeInfo'].keys() else None,
            'image':  item['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in item['volumeInfo'].keys() and 'thumbnail' in item['volumeInfo']['imageLinks'].keys() else None,
            'source_book': 'google-api'
        }, data['items']))
    return []


def format_response_open_library(data):
    """ formatter data from open library """

    if len(data) > 0:
        return list(map(lambda item: {
            'title': item['title'],
            'sub_title': item['title_suggest'],
            'authors': item['author_name'] if 'author_name' in item.keys() else [],
            'categories': item['subject'] if 'subject' in item.keys() else [],
            'description': ' '.join(map(str, item['text'])) if 'text' in item.keys() else None,
            'publish_date':  item['publish_date'].pop() if 'publish_date' in item.keys() else None,
            'editor':  item['publisher'].pop() if 'publisher' in item.keys() else None,
            'image':  None,
            'source_book': 'open-library-api'
        }, data['docs']))
    return []
