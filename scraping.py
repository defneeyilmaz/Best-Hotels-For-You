from bs4 import BeautifulSoup
import requests
import pandas as pd

#cityName = selected city name
#checkInDate = selected check in date
#checkOutDate = selected check out date
url = f'https://www.booking.com/searchresults.html?ss={cityName}&ssne={cityName}&ssne_untouched={cityName}&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-126693&dest_type=city&checkin={checkInDate}&checkout={chackOutDate}&group_adults=2&no_rooms=1&group_children=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/51.0.2704.64 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
hotels = soup.findAll('div', {'data-testid': 'property-card'})
hotels_data = []
# Loop over the hotel elements and extract the desired data
for hotel in hotels:
    # Extract the hotel name
    name_element = hotel.find('div', {'data-testid': 'title'})
    name = name_element.text.strip()
    # Append hotels_data with info about hotel
    hotels_data.append({
        'name': name
    })
hotels = pd.DataFrame(hotels_data)
hotels.head()
hotels.to_csv('test_hotels2.csv', header=True, index=False)