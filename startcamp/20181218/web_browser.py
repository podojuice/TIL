import webbrowser

keywords = [
    'i', '1', '2', 'dkdlwmdnjs'
]

for keyword in keywords:
    url = 'https://www.google.com/search?&q=' + keyword
    webbrowser.open_new(url)
