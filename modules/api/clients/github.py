import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body

    # My tests
    def get_emoji(self):
        url = "https://api.github.com/emojis"

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Error fetching emojis: {response.status_code}")

        body = response.json()
        return body