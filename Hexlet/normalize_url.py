def normalize_url(link):
    if len(link) >= 7:
        if link[0:8] == 'https://':
            return link
        elif link[0:7] == 'http://':
            return 'https://' + link[7:]
        else:
            return 'https://' + link
    return 'https://' + link

print(normalize_url('http://yandex.ru'))