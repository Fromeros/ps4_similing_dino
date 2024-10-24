## Code Created to use the Met Museum API (https://metmuseum.github.io/)

import urllib.request, urllib.parse, urllib.error
import json


# URL for search by: artist, title
service_url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?'

while True:
    art_name = input('Enter an artist or title: ')
    if len(art_name) < 1:
        break

    # Encode the art_name for use in the URL
    params = {'q': art_name}
    url = service_url + urllib.parse.urlencode(params)

    print('Retrieving', url)

    # Open the URL and retrieve data
    incoming = urllib.request.urlopen(url)
    data = incoming.read().decode()

    print('Retrieved', len(data), 'characters')
    print('--------------------------------------------------------------------')
    print('--------------------------------------------------------------------')

    try:
        # Load JSON data
        js = json.loads(data)
    except:
        js = None
        print('Failed to retrieve object ID number')
        continue

    # Getting more detailed information based on the object code
    if 'objectIDs' in js and js['objectIDs'] is not None:
        object_ids = js['objectIDs']

        # URL for getting more info, using art ID
        info_url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'

        try:
            # For each object ID, fetch detailed information
            for object_id in object_ids:
                # URL for the detailed info using the object ID
                obj_url = info_url + str(object_id)
                print('Retrieving detailed info for object ID:', object_id)

                # Get the detailed object info
                obj_uh = urllib.request.urlopen(obj_url)
                obj_data = obj_uh.read().decode()

                # Parse JSON for the object detail
                obj_js = json.loads(obj_data)
                # Print relevant details about the art object
                print(f"Title: {obj_js.get('title', 'N/A')}")
                print(f"Artist: {obj_js.get('artistDisplayName', 'N/A')}")
                print(f"Object Date: {obj_js.get('objectDate', 'N/A')}")
                print(f"Medium: {obj_js.get('medium', 'N/A')}")
                print(f"Link to Image: {obj_js.get('primaryImage', 'N/A')}")
                print('--------------------------------------------------------------------')

        except:
            print("Error retrieving detailed info for object ID:", object_id)

    else:
        print("No results found for", art_name)
