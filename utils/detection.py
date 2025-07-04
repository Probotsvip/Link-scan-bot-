import re

link_regex = r"(https?://\S+|t\.me/\S+|www\.\S+)"

def contains_link(text):
    return bool(re.search(link_regex, text.lower()))

def bio_contains_link(bio):
    return contains_link(bio)
