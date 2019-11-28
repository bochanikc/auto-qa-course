import random
import pytest
import pprint


@pytest.mark.parametrize('brewery_type, brewery_type_in_response', [('micro', 'micro'), ('brewpub', 'brewpub')])
def test_api_by_brewery_request(api_brewery, brewery_type, brewery_type_in_response):
    res = api_brewery.get(
        path="/breweries",
        params={'by_type': brewery_type}
    )

    random_brewery_number = random.randint(1, 20)
    # print(pprint.pprint(res.json()[random_brewery_number]))
    assert res.json()[random_brewery_number]['brewery_type'] == brewery_type_in_response


@pytest.mark.parametrize('city', ['""', 0])
def test_api_invalid_city(api_brewery, city):
    res = api_brewery.get(
        path="/breweries",
        params={'by_city': city}
    )

    assert res.json() == []


@pytest.mark.parametrize('per_page', [15, 30, 50])
def test_api_brewery_per_page_and_go_to_page(api_brewery, per_page):
    random_page_number = random.randint(1, 10)
    res = api_brewery.get(
        path="/breweries",
        params={
            'page': random_page_number,
            'per_page': per_page}
    )

    random_brewery_number = random.randint(1, per_page)
    #print(pprint.pprint(res.json()[random_brewery_number]['id']))
    assert res.json()[random_brewery_number]['id'] > 0