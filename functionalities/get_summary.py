import requests
import json
from bs4 import BeautifulSoup
import os
class GetSummary:
    def __init__(self):
        self.server_url = "https://content-summar-expressjs.vercel.app/summary"
    # Unused Function / Not needed Currently
    def get_google_search_results(self ,query):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        search_url = f"https://www.google.com/search?q={query}"
        response = requests.get(search_url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.find('div' ,class_='tF2Cxc').find('a')['href']
        else:
            print("Failed to retrieve search results")
            return []    
    def get_response(self ,question):
        # print(f'data :  {question}')
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "data": question
        }
        try:
            response = requests.post(self.server_url, json=data, headers=headers)
            json_response = response.json()
            return json_response.get('message')
        except Exception as e:
            return f"Server Error ,{e}"
if __name__ == "__main__":
    object = GetSummary()
    query = "capital of new zeland"
    # results = object.get_google_search_results(query)
    print(object.get_response(query))
