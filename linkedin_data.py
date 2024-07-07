import requests


def scrape_company_data(company_name):
    url = "https://linkedin-data-api.p.rapidapi.com/get-company-details"

    querystring = {"username":company_name}

    headers = {
        "x-rapidapi-key": "fef0f36761msh7f7079330e839fbp14e3ebjsna3e9db8b6c39",
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return (response.json())

def scrape_company_post(company_name):


    url = "https://linkedin-data-scraper.p.rapidapi.com/company_updates"

    payload = {
        "company_url": f"http://www.linkedin.com/company/{company_name}",
        "posts": 10,
        "comments": 10,
        "reposts": 10
    }
    headers = {
        "x-rapidapi-key": "fc4ebbb663mshf2e046498795d65p12cc0cjsnc16f16184e29",
        "x-rapidapi-host": "linkedin-data-scraper.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())
    return (response.json())
