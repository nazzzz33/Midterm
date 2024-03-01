import re


def is_valid_url(url):
    # Regular expression pattern to match a URL
    pattern = re.compile(r"^https?://(?:www\.)?[\w.-]+\.[a-zA-Z]{2,}$")

    # Use the pattern to search for a match in the URL
    match = pattern.match(url)

    # If a match is found, return True (valid URL), otherwise return False
    return bool(match)


# Example usage:
url1 = "https://www.example.com"
url2 = "http://invalid.url"
url3 = "ftp://another.invalid.url"

print(is_valid_url(url1))  # Output: True
print(is_valid_url(url2))  # Output: False
print(is_valid_url(url3))  # Output: False
