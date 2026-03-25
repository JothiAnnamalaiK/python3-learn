import re


def generate_slug(text):
    """
    Convert a string into a URL-friendly slug with dashes.
    """
    # Convert to lowercase
    text = text.lower()
    # Replace spaces and underscores with dash
    text = re.sub(r"[\s_]+", "-", text)
    # Remove all non-alphanumeric and non-dash characters
    text = re.sub(r"[^a-z0-9\-]", "", text)
    # Remove leading/trailing dashes
    text = text.strip("-")
    # Replace multiple dashes with a single dash
    text = re.sub(r"-+", "-", text)
    return text


# --------------------------
# Test cases
# --------------------------
tests = [
    "Hello World",  # hello-world
    "Python_Programming 101",  # python-programming-101
    "   Spaces   Everywhere   ",  # spaces-everywhere
    "Special!@#Characters*&^%",  # specialcharacters
    "Multiple---Dashes___Test",  # multiple-dashes-test
    "Trailing & Leading - Dashes ",  # trailing-leading-dashes
]

for t in tests:
    slug = generate_slug(t)
    print(f"'{t}' -> '{slug}'")
