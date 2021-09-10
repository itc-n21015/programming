import json
import sys
import requests

post_code = input("郵便番号を入力してください(7桁)")
RECEST_URL = "http://zipcloud.ibsnet.co.jp/api/search?zipcode={0}".format(post_code)

address = ""
kana = ""

response = requests.get(RECEST_URL)
json_result = response.text
json_to_dic_result = json.loads(response.text)
if json_to_dic_result["message"] == None:
    result_dic = json_to_dic_result["results"][0]
else:
    print("住所は見つかりませんでした")
    sys.exit()

for i in range(1, 4):
    address += result_dic["address" + str(i)]
    kana += result_dic["kana" + str(i)]

context = {"郵便番号:": post_code, "カナ:": kana, "住所:": address}

print("  検索結果  ")
for k, v in context.items():
    print(k, v)
