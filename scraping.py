from bs4 import BeautifulSoup
import requests
import pandas as pd


def check_element(element):
    if element is not None:
        return element.text.strip()
    else:
        return "Not given"


def get_live_euro(header):
    euro_url = 'https://www.google.com/finance/quote/EUR-TRY?sa=X&ved=2ahUKEwjmhcjYu4CGAxUxQ_EDHWe5CMEQmY0JegQIGhAw'
    response_ = requests.get(euro_url, headers=header)
    soup_ = BeautifulSoup(response_.text, 'html.parser')
    scrap = soup_.find('div', {'class': 'YMlKec fxKbKc'})
    euro = scrap.text.strip()
    return euro


cityName = "Rome"
checkInDate = "2024-06-20"
checkOutDate = "2024-06-26"
#currency = selected currency
url = f'https://www.booking.com/searchresults.html?ss={cityName}&ssne={cityName}&ssne_untouched={cityName}&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-126693&dest_type=city&checkin={checkInDate}&checkout={checkOutDate}&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/51.0.2704.64 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
hotels = soup.findAll('div', {'data-testid': 'property-card'})
hotels_data = []
# Loop over the hotel elements and extract the desired data
for hotel in hotels[:10]:
    # Extract the hotel name
    name_element = hotel.find('div', {'data-testid': 'title'})
    name = check_element(name_element)

    address_element = hotel.find('span', {'data-testid': 'address'})
    address = check_element(address_element)

    distanceToCityCenter_element = hotel.find('span', {'data-testid': 'distance'})
    distanceToCityCenter = check_element(distanceToCityCenter_element)

    reviewScore_element = hotel.find('span', {'class': 'a3332d346a'})
    reviewScore = check_element(reviewScore_element)
    reviewScoreList = reviewScore.split("'")
    review = reviewScoreList[0]

    price_element = hotel.find('span', {'class': 'f6431b446c fbfd7c1165 e84eb96b1f'})
    price = check_element(price_element)
    price = price.replace(" "," ")
    price = price.replace("€", "EUR")

    # Append hotels_data with info about hotel
    hotels_data.append({
        'name': name,
        'address': address,
        'distanceToCityCenter': distanceToCityCenter,
        'reviewScore': review,
        'price': price,
    })
hotels = pd.DataFrame(hotels_data)
hotels.head()
hotels.to_csv('test_hotels.csv', header=True, index=False)