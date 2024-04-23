import requests
import warnings


def request_data(url):
    warnings.simplefilter("ignore")

    try:
        response = requests.get(url, verify=False)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        pass
        # print(e)

    return False
