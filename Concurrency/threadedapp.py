from multiprocessing.pool import ThreadPool

def fetch_url(url):
    """Fetch content of a given url from the web"""
    import urllib.request
    response = urllib.request.urlopen(url)
    return response.read()

def fetch_all_urls_threaded(urls):
    pool = ThreadPool(4)
    return pool.map(fetch_url, urls)

def fetch_all_urls(urls):
    contents = []
    for url in urls:
        contents.append(fetch_url(url))
    return contents

def wait_until(predicate):
    """Waits until the given predicate returns True"""
    import time
    seconds = 0
    while not predicate():
        print('Waiting...')
        time.sleep(1.0)
        seconds += 1
    print('Done!')
    return seconds