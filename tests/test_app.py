def test_health_ok(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}

def test_index(client):
    res = client.get('/')
    data = res.get_json()
    assert res.status_code == 200
    assert data["app"].startswith("ACEest")
    assert "Welcome" in data["message"]

def test_bmi_valid(client):
    res = client.post('/bmi', json={"weight_kg": 80, "height_cm": 180})
    assert res.status_code == 200
    data = res.get_json()
    assert "bmi" in data and "category" in data
    # 80 / (1.8^2) = 24.69 -> "normal"
    assert round(data["bmi"], 2) == 24.69
    assert data["category"] == "normal"

def test_bmi_missing_fields(client):
    res = client.post('/bmi', json={"weight_kg": 80})
    assert res.status_code == 400
    assert "required" in res.get_json()["error"]

def test_bmi_invalid_values(client):
    res = client.post('/bmi', json={"weight_kg": -1, "height_cm": 180})
    assert res.status_code == 400
    assert "positive" in res.get_json()["error"]
