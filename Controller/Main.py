import requests
import json
import sys
sys.path.insert(0, '/Users/pzeeuw/Documents/CSAP/VSCode Environment/SaseDashboard/Model')
sys.path.insert(0, '/Users/pzeeuw/Documents/CSAP/VSCode Environment/SaseDashboard/View')
import Thousand_Eyes_data, DUO_data, Umbrella_data
import Grafana_data


def main():
    url = "https://api.thousandeyes.com/v6/status"
    username = "PhillyZ"
    password = "RossyB"
    token = Thousand_Eyes_data.getToken(url, username, password)
    print("token")

if __name__ == "__main__":
    main()
