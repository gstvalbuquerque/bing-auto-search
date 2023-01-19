# -*- coding: utf-8 -*-
import os
import requests
import pandas as pd

# Bing search keys
sub_key = os.environ['SUB_KEY']
endpoint = os.environ['BING_ENDPOINT'] + "/v7.0/search"


# Request config
headers = {"Ocp-Apim-Subscription-Key": sub_key}
params = {"textDecorations": True, "textFormat": "HTML"}


def search_terms(term: str) -> None:
    try:
        print(f"Searching for the estimated number os matches of {term}...")
        params.update({"q": term})
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        df = pd.json_normalize(data)
        number_of_matches = df.iloc[0]['webPages.totalEstimatedMatches']
        print(f"The estimated number of matches is: {number_of_matches}")

    except Exception as ex:
        raise Exception(ex)


term = str(input("Enter your search term: "))
search_terms(term)
