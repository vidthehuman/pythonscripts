def extract_data(url):
    import requests
    response = requests.get(url)
    return response.json()
def star_user(data):
    starred_user_data = []
    for user in data:
        starred_user_data.append(user)
    return starred_user_data
data = extract_data('https://hub.dummyapis.com/employee')
starred_user = star_user(data)
print(starred_user)