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
    response = requests.get(euro_url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    scrap = soup.find('div', {'class': 'YMlKec fxKbKc'})
    euro = scrap.text.strip()
    return float(euro)


def scrape(cityname, checkindate, checkoutdate):
    url = f'https://www.booking.com/searchresults.html?ss={cityname}&lang=en-us&src=searchresults&dest_type=city&ac_langcode=en&checkin={checkindate}&checkout={checkoutdate}&group_adults=2&no_rooms=1&group_children=0&selected_currency=EUR'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/51.0.2704.64 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    hotels = soup.findAll('div', {'data-testid': 'property-card'})
    hotels_data = []
    print(url)
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
        euroPrice = check_element(price_element)
        euroPrice = euroPrice.split(" ")[1]
        euroPrice = euroPrice.replace(",", "")
        priceInTl = str(round(float(euroPrice) * get_live_euro(headers), 2))
        tlPrice = "TL " + priceInTl

        # Append hotels_data with info about hotel
        hotels_data.append({
            'name': name,
            'address': address,
            'distanceToCityCenter': distanceToCityCenter,
            'rating': review,
            'priceInEuro': int(euroPrice),
            'priceInTl': tlPrice,
        })
    sortedlist = sorted(hotels_data, key=lambda d: d['priceInEuro'])
    for hotel in sortedlist:
        amount = hotel['priceInEuro']
        hotel['priceInEuro'] = 'EUR ' + str(amount)
    hotels = pd.DataFrame(sortedlist)
    hotels.head()
    hotels.to_csv('test_hotels.csv', header=True, index=False)
