from apify_client import ApifyClient
import os


def scrape_profile(username):
    client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

    run_input = {
        "usernames": [username],
        "resultsLimit": 1,
        "searchLimit": 1,
        "resultsType": "details",
        "addProfileStats": True
    }

    run = client.actor("apify/instagram-profile-scraper").call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    if not items:
        return None

    return items[0]
