import m3u8
import requests
import yt_dlp

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    # add more default headers as per your requirements
}


def send_request(url: str, headers: dict = None) -> str:
    if not headers:
        headers = DEFAULT_HEADERS
    payload = ""
    response = requests.request("GET", url, data=payload, headers=headers)
    return response


def m3u8_parser(response: str) -> str:
    play = m3u8.loads(response.text)
    highest_quality_index = len(play.data['playlists']) - 1
    highest_quality_url = play.data['playlists'][highest_quality_index]['uri']
    return highest_quality_url


def download(url: str, path: str, title: str, headers: dict = None) -> str:
    if not headers:
        headers = DEFAULT_HEADERS
    ydl_opts = {
        'outtmpl': f'{path}/{title}.%(ext)s',
        'concurrent_fragment_downloads': 1,
        'http_headers': headers
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        output_file_path = ydl.prepare_filename(info_dict)
        
    return output_file_path

