import json
from urllib import response


def test_create_campaigns(client):
    data = {"campaign_name":"test_camp", "budget_remaining": "1234", "buying_type": "AUCTION"}
    response = client.post("/campaign/",json.dumps(data))
    assert response.status_code == 200
    assert response.json()["budget_remaining"] == 1234
    assert response.json()["is_active"] == True
    assert response.json()['is_superuser'] == False