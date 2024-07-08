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

    # print(response.json())
    return (response.json())


def get_clean_company_post_data(company_name):

    data = scrape_company_post(company_name)

    if data['success'] == True:

        final_list = []
        # count = 1
        for i in data['response']:

            final_dict = dict()
            # final_dict['post_count'] = count
            final_dict['postText'] = i.get('postText')
            final_dict['postLink'] = i.get('postLink')
            final_dict['socialCount'] = i.get('socialCount')
            final_dict['postedAt'] = i.get('postedAt')
            final_dict['postedAgo'] = i.get('postedAgo')
            final_list.append(final_dict)
            # count += 1

        return final_list
    else:
        return data