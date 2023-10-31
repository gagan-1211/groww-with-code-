import pyshorteners

def shorten_url(original_url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(original_url)
    print("The URL is shortened to:", shortened_url)
    return shortened_url

if __name__ == "__main__":
    original_internet_url = "https://www.example.com/path/to/something"
    shortened_url = shorten_url(original_internet_url)
