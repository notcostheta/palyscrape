# PlayScrape

# U gib link, I gib video

## Installation

### (Optional) Make a Venv :

Isolate the code by making a python3 virtual environment

```bash
python3 -m venv .venv
```

### Activate the virtual environment

```bash
source .venv/bin/activate
```

- Install the dependencies like you normally do.
    
    ```bash
    pip3 install -r requirements.txt
    ```
    


## Usage :

- Open `main.py` and edit the `path` to your desired path, by default it’s `"content".`
- Your videos would be saved there.
- Run the `[main.py](http://main.py)` normally in your Python interpreter
    
    ```bash
    python3 main.py
    ```
    
- Enter the desired URL when prompted

### (Optional) Change Default threads :

- Modify `video_downloader.py` by changing line no. `33`
- By default it’s set to `'concurrent_fragment_downloads': 5,`
- Change it to the desired number of threads, for example
    - `'concurrent_fragment_downloads': 10,`



## How it works :

- This program opens a lightweight browser window that fetches the `master.m3u8` URL
- This only works for websites that automatically send the request to the server to prematurely load the URL
- This code doesn't work for sites which require some kind of action to load the m3u8 url
- Then it parses the url with the `m3u8` parser library
- And finally downloads it using `yt-dlp`

---