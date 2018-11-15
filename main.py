
USER=""
API_TOKEN=""
GIT_API_URL="https://api.github.com"

import requests
import base64
import json

def get_api(url):
    try:
        headers = {"Authorization" :  "token " + API_TOKEN}
        url = GIT_API_URL + url
        print(url)
        return requests.get(url, headers=headers)
    except Exception as e:
        print("Failed to get api request from " + url + str(e))

    return ""

def get_repos():
    res = get_api("/user/repos?per_page=100")
    res_o = json.loads(res.text)
    repos = list()
    for repo in res_o:
        repos.append({ "url" : repo["html_url"], "name" : repo["name"]})

    return repos

def download_repos():
    for repo in get_repos():     
        print("DOWNLOADING: " + str(repo))
        headers = {"Authorization" :  "token " + API_TOKEN}
        res = requests.get(repo["url"] + "/tarball/master", headers=headers)
        open(repo["name"] + ".tar.gz", "wb").write(res.content)
        

def main():
    download_repos()


if __name__ == "__main__":
    main()
