import requests

login_url = "https://shop.hakhub.net/wp-login.php"
item_utl = "https://shop.hakhub.net/wp-comments-post.php"
account_form_data = {"log":"customer01", "pwd":"customer01!!"}

with requests.Session() as s:
    r = s.post(login_url, account_form_data)
    comment_form_data = {
        'rating': 5,
        'comment' : 'Eagle은 자동으로 쓴 글입니다.',
        'comment_post_ID': '70',
        'comment_parent' : 0
    }
    r=s.post(item_utl, cookies= s.cookies, data=comment_form_data)
    if r.status_code == 200:
        print('댓글 작성 성공')
    elif r.status_code == 403:
        print('댓글 작성 권한이 없거나 로그인에 실패')
    elif r.status_code == 409:
        print('이미 댓글을 달아버림')
    elif r.status_code == 429:
        print('댓글을 너무 빨리 달아부러쓰')
    else:
        print(f"댓글 작성 오류 코드 : {r.status_code}")
