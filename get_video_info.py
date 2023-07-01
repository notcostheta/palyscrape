from playwright.sync_api import sync_playwright

url = str(input("Enter the url: "))
url = url.strip()

def run(playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=True)
    page = browser.new_page()
    request_url = ""
    video_info = {
        "master_url": None,
        "master_headers": None,
        "title": None
    }

    # Define a resource blocker.
    excluded_resource_types = ["stylesheet",
                               "image", "font", "manifest", "fetch", "media"]

    def block_aggressively(route):
        if (route.request.resource_type in excluded_resource_types):
            route.abort()
        else:
            route.continue_()

    def handle_request(request):
        nonlocal request_url
        request_url = request.url

        # Get the master url and headers from the network tab

        if "master.m3u8" in request.url:
            video_info["master_url"] = request.url
            video_info["master_headers"] = request.headers
            title = page.title()
            if len(title) > 95:
                title = title[:92] + "..."
            video_info["title"] = title
            
            page.close()

    page.on("request", handle_request)
    page.route("**/*", block_aggressively)
    try:
        page.goto(url)
    except:
        pass

    browser.close()

    # Return the video info.
    return video_info