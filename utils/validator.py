def validate_response(response):
    data = response.json()
    assert isinstance(data , list)
    assert len(data) > 0

    for item in data:  
        assert "userId" in item
        assert "id" in item
        assert "title" in item
        assert "body" in item          