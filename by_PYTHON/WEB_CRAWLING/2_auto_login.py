import requests

login_url = "https://shop.hakhub.net/wp-login.php"
account_form_data = {"log":"customer01", "pwd":"customer01!!"}

with requests.Session() as s:
    #form-data 형식은 data 인자를 생략해 작성 가능함.
    r=s.post(login_url, account_form_data)
    print(r.status_code)
    print(r.text)

