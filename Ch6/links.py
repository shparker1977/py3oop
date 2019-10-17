from urllib.request import urlopen
from urllib.parse import urlparse
from queue import Queue
import re
import sys

LINK_REGEX = re.compile(
    "<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>"
)

class LinkCollector:
    def __init__(self, url):
        self.url = "" + urlparse(url).netloc
        self.collected_links = {}
        self.visited_links = set()

    def collect_links(self, path="/"):
        queue = Queue()
        queue.put(self.url)
        while not queue.empty():
            url = queue.get().rstrip('/')
            full_url = "http://" + self.url + path
            self.visited_links.add(full_url)
            page = str(urlopen(full_url).read())
            links = LINK_REGEX.findall(page)
            links = {self.normalize_url(path, link) for link in links}
            self.collected_links[full_url] = links
            for link in links:
                self.collected_links.setdefault(link, set())
            unvisited_links = links.difference(self.visited_links)
            for link in unvisited_links:
                if link.startswith(self.url):
                    queue.put(link)

    def normalize_url(self, path, link):
        if link.startswith("http://"):
            return link
        elif link.startswith("/"):
            return "http://" + self.url + link
        else:
            return "http://" + self.url + path.rpartition('/')[0] + '/' + link


if __name__ == "__main__":
    collector = LinkCollector(sys.argv[1])
    collector.collect_links()
    for link, item in collector.collected_links.items():
        print("{}: {}".format(link, item))