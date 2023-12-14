import requests
from django.shortcuts import render
from django.conf import settings

FLASK_PROXY_URL = settings.FLASK_PROXY_URL

common_headers = {'Content-Type': 'application/json'}

def user_list(request):
    parsed_url = request.GET.urlencode()
    url = f'{FLASK_PROXY_URL}?{parsed_url}'

    response = requests.get(url, headers=common_headers)
    user_list_data = response.json().get('data', {})
    page_numbers = list(range(1, user_list_data['totalPages'] + 1))

    return render(request, 'myapp/user_list.html', {
        'api_url': FLASK_PROXY_URL,
        'user_list_data': user_list_data,
        'page_numbers': page_numbers,
        'page_row_count': len(user_list_data['users']['rows']),
        'current_page': user_list_data['page'],
    })

def edit_user(request, id):
    url = f'{FLASK_PROXY_URL}/{id}'
    response = requests.get(url, headers=common_headers)
    user = response.json().get('data', None)
    return render(request, 'myapp/edit_user.html', {
        'api_url': FLASK_PROXY_URL,
        'user': user
    })

def add_user(request):
    return render(request, 'myapp/add_user.html', { 'api_url': FLASK_PROXY_URL })

def detail_user(request, id):
    url = f'{FLASK_PROXY_URL}/{id}'
    response = requests.get(url, headers=common_headers)
    user = response.json().get('data', None)

    return render(request, 'myapp/detail_user.html', {
        'user': user,
        'api_url': FLASK_PROXY_URL
    })
