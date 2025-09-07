#!/usr/bin/env python3
"""
Ubuntu Image Fetcher
A mindful tool for collecting images from the web.
"""

import os
from urllib.parse import urlparse
import requests

# Directory where images will be saved
SAVE_DIR = "Fetched_Images"


def fetch_image(url):
    """Fetch a single image and save it to Fetched_Images."""
    try:
        # Make sure folder exists
        os.makedirs(SAVE_DIR, exist_ok=True)

        # Fetch image
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Confirm content type is an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        # Extract filename or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            ext = content_type.split("/")[-1]
            filename = f"downloaded_image.{ext}"

        filepath = os.path.join(SAVE_DIR, filename)

        # Skip duplicates
        if os.path.exists(filepath):
            print(f"✗ Skipped (already exists): {filename}")
            return

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls_input = input("Please enter image URLs separated by commas:\n")
    urls = [u.strip() for u in urls_input.split(",") if u.strip()]

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
