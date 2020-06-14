import json
import requests
  

def get_all_complaints():
    """ Info

        Args:
            
        Returns:
            
    """
    url = "https://phl.carto.com/api/v2/sql?q=SELECT * FROM ppd_complaints"

    payload = "{\"page\": 1, \"pageSize\": 7, \"sortStyle\": \"descending\", \"placeFilter\": \"e\"}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data = payload)


    return response.text.encode('utf8')

