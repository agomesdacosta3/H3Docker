from app import app

def test_home_route():
	response = app.test_client().get("/")
	assert response.status_code == 200
	assert b"<p>Hello welcome in the app!</p>" in response.
