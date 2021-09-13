import requests as req

r_url = "https://weather.tsukumijima.net/api/forecast/city/"
print("471010 = 那覇  471020 = 名護")

code = input(str("ここに上記の数字を入力: "))
input_code = f"{r_url}{code}"

url = req.get(input_code).json()["forecasts"]
daLa = url[0]["dateLabel"]
telo = url[0]["telop"]

print("検索結果を表示します")

today_weather = f" ({daLa}の天気は{telo}です)"
print(today_weather)

cr = url[0]["chanceOfRain"]["T06_12"]
today_cr = f" (午前の降水確率は{cr}です)"
print(today_cr)

cr2 = url[0]["chanceOfRain"]["T12_18"]
today_cr2 = f" (午後の降水確率は{cr2}です)"
print(today_cr2)

print("-----明日の天気予報-----")

tomorrow = url[1]["dateLabel"]
tomorrow_telo = url[1]["telop"]
tomorrow_cr = url[1]["chanceOfRain"]["T06_12"]
tomorrow_cr2 = url[1]["chanceOfRain"]["T12_18"]

tomorrw_weather = f" ({tomorrow}の天気は{tomorrow_telo}です。)"
print(tomorrw_weather)

tomorrow_crn = f" (午前の降水確率は{tomorrow_cr}です)"
print(tomorrow_crn)

tomorrow_crn2 = f" (午後の降水確率{tomorrow_cr2}はです)"
print(tomorrow_crn2)
