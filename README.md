# Ubuntu_Requests
# Ubuntu Image Fetcher

A simple, respectful, and practical Python tool for fetching images from the web and saving them in an organized folder.
This README explains the assignment, what the program does, how to run and test it, and what code and files you should include in your GitHub repo `Ubuntu_Requests`.

---

# What the assignment asks you to build

The core requirements

* Use the `requests` library to fetch images from the web.
* Check for HTTP errors and handle them gracefully.
* Create the save directory with `os.makedirs(..., exist_ok=True)`.
* Extract a filename from the URL or generate a sensible fallback name.
* Save the image in binary mode.
* Follow Ubuntu principles: Community, Respect, Sharing, Practicality.

Extra or challenge items

* Accept multiple URLs at once.
* Describe precautions to take when downloading from unknown sources.
* Prevent duplicate images from being saved.
* Explain what HTTP headers to check before saving a response.

---

# What I implemented in the code

Files you should include in your repo

* `ubuntu_fetcher.py`  - the main script you will run.
* `requirements.txt`  - lists `requests`.
* `.gitignore`  - ignore `venv/`, `__pycache__/`, and `Fetched_Images/`.
* `README.md`  - this file.

Key features and behavior implemented by the script

* Accepts multiple URLs from the command line, from a text file, or interactively.
* Creates `Fetched_Images` automatically if it does not exist.
* Uses `requests` with a timeout and `raise_for_status()` to detect HTTP errors.
* Checks `Content-Type` header to confirm the response is an image.
* Checks `Content-Length` when available and enforces a maximum size limit.
* Streams downloads in chunks to avoid loading large responses into memory at once.
* Saves images in binary mode.
* Avoids duplicate images by computing a SHA-256 hash and recording it in `index.json` inside `Fetched_Images`.
* Provides friendly terminal messages that explain success or errors, aligning with Ubuntu principles.

---

# How to set up and run the project step by step

1. Create project folder and files

   * Create a folder, for example `Ubuntu_Requests`.
   * Inside that folder add `ubuntu_fetcher.py`, `requirements.txt`, `.gitignore`, and this `README.md`.

2. `requirements.txt`

```
requests
```

3. Optional `.gitignore`

```
venv/
__pycache__/
Fetched_Images/
*.pyc
```

4. Create and activate a virtual environment

* Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

* Windows

```bash
python -m venv venv
venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Run the script

* Interactive input

```bash
python ubuntu_fetcher.py
# then paste URLs when prompted
```

* Provide URLs on the command line

```bash
python ubuntu_fetcher.py --urls https://www.python.org/static/community_logos/python-logo.png https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png
```

* Provide a file with one URL per line

```bash
python ubuntu_fetcher.py --file urls.txt
```

7. Check results

* The saved images appear in `Fetched_Images/`.
* An `index.json` file records saved filenames, sha256 hashes, source URLs, timestamp, size and content type.

---

# Example terminal session and expected output

Example input

```
python ubuntu_fetcher.py --urls https://www.python.org/static/community_logos/python-logo.png
```

Example output

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

✓ Successfully fetched: python-logo.png
✓ Image saved to Fetched_Images/python-logo.png

Connection strengthened. Community enriched.
```

If a URL is not an image

```
✗ Skipped - not an image: https://example.com/page.html (Content-Type: text/html)
```

If a duplicate is detected by hash

```
✗ Skipped - duplicate of python-logo.png (sha256 match)
```

---

# How the code meets the assignment requirements

Requirement mapping

* `requests` usage: the script uses `requests.Session()` with timeouts and `raise_for_status()`.
* HTTP errors: handled by `try/except requests.exceptions.RequestException` and friendly messages.
* Directory creation: `os.makedirs("Fetched_Images", exist_ok=True)`.
* Filename extraction: obtained via `urllib.parse.urlparse` and `Content-Disposition` fallback or generated from content type.
* Binary saving: files are written using open in `wb` mode and streamed to disk.
* Ubuntu principles: friendly messaging and robust error handling reflect Community and Respect, `Fetched_Images` supports Sharing, and the tool is practical.

---

# Precautions included and recommended

Precautions implemented in code

* Check `Content-Type` to ensure the response is an image.
* Check `Content-Length` if present to avoid very large downloads.
* Use streaming to write the file in chunks and enforce a maximum allowed size while downloading.
* Use a timeout on network requests to avoid hanging.

Additional recommendations

* Prefer HTTPS links.
* Do not open or run downloaded files without scanning them with antivirus tools.
* If you plan to share images publicly, check licensing or copyright.
* Keep user agent friendly and explicit so remote servers can identify the tool.

---

# HTTP headers the script looks at and why

* `Content-Type`  - verify the server is returning an image.
* `Content-Length`  - estimate size before download when possible.
* `Content-Disposition`  - sometimes suggests a filename.
* `ETag` or `Last-Modified`  - could be used to detect unchanged resources in a future enhancement.
* `Accept` and `User-Agent`  - set by the script for polite requests.

---

# How duplicate prevention works

* While downloading, the script computes a SHA-256 hash of the file contents.
* `index.json` inside `Fetched_Images` stores each saved file along with its SHA-256 hash.
* Before finalizing a file save, the script compares the new hash with existing hashes. If a match is found, the new file is deleted and the download is skipped.

This ensures you do not store the same image twice even if the filename differs.

---

# How to prepare your GitHub repo and push

1. Create a repository on GitHub named `Ubuntu_Requests`.

2. Locally in your project folder run

```bash
git init
git add ubuntu_fetcher.py requirements.txt README.md .gitignore
git commit -m "Add Ubuntu Image Fetcher assignment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Ubuntu_Requests.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.


* You probably want `Fetched_Images/` in `.gitignore` so you do not push images to GitHub.

