import requests as req

r_url = "https://zipcloud.ibsnet.co.jp/api/search"

code = str(input("7桁の数字を入力:  "))
input_code = f"{r_url}?zipcode={code}"

url = req.get(input_code).json()["results"]

post1 = url[0]["address1"]
post2 = url[0]["address2"]
post3 = url[0]["address3"]

print("検索結果を表示します")
final_post = f"（{post1}の{post2}{post3}でした）"

print(final_post)
