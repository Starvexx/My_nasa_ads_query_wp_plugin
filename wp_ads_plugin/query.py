#! /usr/bin/env python3

import requests
import json
from urllib.parse import urlencode, quote_plus

# The NASA-ADS API token
token = "<your_NASA-ADS_API_token>"

# The ID of the ADS library containing all the entries.
library_id = "<the_ADS_library_ID>"

# Get the bibcode for each entry in the ADS library.
results = requests.get(
        "https://api.adsabs.harvard.edu/v1/biblib/libraries"+"/"+library_id,
        headers={'Authorization': 'Bearer ' + token}
        )

bibcodes = results.json()['documents']

refereed = []
non_refereed = []

# Query the ADS using the bibcodes obtained from the ADS library.
for bibcode in bibcodes:
    # Build the query
    encoded_query = urlencode(
            {"q": f"identifier:{bibcode}",
            "fl": "bibcode, property",
            "rows": 1})

    # Execute the query
    res = requests.get(
            "https://api.adsabs.harvard.edu/v1/search/query?{}".format(encoded_query), \
            headers={'Authorization': 'Bearer ' + token}
            )
    res = res.json()["response"]['docs'][0]['property']

    # Filter the result into refereed and non refereed publications.
    if "REFEREED" in res:
        refereed.append(bibcode)
    elif "NOT REFEREED":
        non_refereed.append(bibcode)

# Format the output.
custom_format = '<li><a href="%u"><b>%T</b></a><br> <i>%l</i> (%Y), %J, %V, %p., %d</li>'

payload_refereed = {'bibcode': refereed,
                    'format': custom_format,
                    'sort': 'date asc'}

payload_non_refereed = {'bibcode': non_refereed,
                        'format': custom_format,
                        'sort': 'date asc'}

# Build the query payload
serialized_payload_refereed = json.dumps(payload_refereed)
serialized_payload_non_refereed = json.dumps(payload_non_refereed)

# Export the ADS data entries in the specified custom format from above
lib_entries_refereed = requests.post(
        "https://api.adsabs.harvard.edu/v1/export/custom", 
        headers={'Authorization': 'Bearer ' + token},
        data=serialized_payload_refereed)

lib_entries_non_refereed = requests.post(
        "https://api.adsabs.harvard.edu/v1/export/custom",
        headers={'Authorization': 'Bearer ' + token},
        data=serialized_payload_non_refereed)

# print(lib_entries.json()["msg"]+"\n")

# Create the HTML code of the formatted ADS entries.
print('<h3>Refereed publications</h3>')
print("<ul>")
print(lib_entries_refereed.json()["export"])
print("</ul><br>")
print('<h3>Non refereed publications</h3>')
print("<ul>")
print(lib_entries_non_refereed.json()["export"])
print("</ul>")
