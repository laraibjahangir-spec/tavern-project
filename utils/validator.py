def validate_response(response):
    data = response.json()
    assert isinstance(data , list)
    assert len(data) > 0

    for item in data:  
        assert "userId" in item
        assert "id" in item
        assert "title" in item
        assert "body" in item

#def validate_single_post(response , post_no=None):
#        data = response.json()
#        assert len(data) > 0
#
#        if isinstance(data , list):
#            post = next(items for item in data if item["id"] == post_id , None)
#        else:
#            post = data
#        assert "id" in 
            
        

            