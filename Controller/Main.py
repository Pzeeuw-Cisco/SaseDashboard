import requests
import json
from SaseDashboard.Model.Thousand_Eyes_data import getToken as TE


def main():
    url = "https://api.thousandeyes.com/v6/status"
    username = "PhillyZ"
    password = "RossyB"
    token = TE(url, username, password)
    print("token")

if __name__ == "__main__":
    main()
