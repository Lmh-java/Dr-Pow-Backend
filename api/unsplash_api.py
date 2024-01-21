
import PIL.Image
import requests

from util.config import Config


# Search photo on splash and return a photo id
def search_photo(query, per_page=1) -> str:
    base_url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {Config.UNSPLASH_API_KEY}"
    }

    params = {
        "query": query,
        "per_page": per_page,
        "order_by": "relevant",
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()['results'][0]['id']
    else:
        print(f"Error: {response.status_code}")
        raise


# download photon from unsplash api and return the
def download_photo(photo_id) -> PIL.Image:
    base_url = "https://api.unsplash.com/photos/"
    headers = {
        "Authorization": f"Client-ID {Config.UNSPLASH_API_KEY}"
    }

    response = requests.get(base_url + photo_id, headers=headers)

    if response.status_code == 200:
        res_data = response.json()
        # read the image using PIL
        return PIL.Image.open(requests.get(res_data['urls']['regular'], stream=True).raw)
    else:
        print(f"Error: {response.status_code}")
        return None

