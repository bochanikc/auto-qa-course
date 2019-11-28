def test_url_status_200(api_client):
    res = api_client.get(
        path="/"
    )
    print('1')
    assert res.status_code == 200
