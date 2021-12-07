# /test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "CRUD FastApi Mysql","Authors":"Afrizals Blog"}

def test_crud_user():
    # create data
    response = client.post(
        "/pegawai/",
        json={
                "nama_pegawai": "asep",
                "alamat_pegawai": "bangka belitung",
                "ttl_pegawai": "1997-06-04",
                "telp_pegawai": "4045",
                "email_pegawai": "asep@domain.com"
            },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['data']['email_pegawai'] == "asep@domain.com"
    assert "id" in data['data']
    user_id = data['data']['id']

    # read detail data
    response = client.get(f"/pegawai/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['data']['email_pegawai'] == "asep@domain.com"
    assert data['data']['id'] == user_id

    # update data
    response = client.post(
        f"/pegawai/{user_id}",
        json={
                "nama_pegawai": "asep update",
                "alamat_pegawai": "surabaya",
                "ttl_pegawai": "1997-10-03",
                "telp_pegawai": "4045",
                "email_pegawai": "asep_update@domain.com"
            },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['data']['nama_pegawai'] == "asep update"
    assert data['data']['email_pegawai'] == "asep_update@domain.com"

    # delete data
    response = client.delete(
        f"/pegawai/{user_id}"
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['message'] == f"sukses menghapus data dengan id {user_id}"