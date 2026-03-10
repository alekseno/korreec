import httpx
from config import BASE_URL

def test_create_task():
    
    body = {
        "content": "my test",
        "user_id": "string",
        "is_done": False
    }
    path = "/create-task"
    response = httpx.put(BASE_URL + path, json = body)
     
    assert response.status_code == httpx.codes.OK, f"Код ответа ожидался 200, по факту пришел {response.status_code}"
    
    data = response.json()
    print(data)

    
    