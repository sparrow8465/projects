import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수 인코딩 -> 딕셔너리형의 자료형을 url로
values = {
    'stnld' : '108'
}

params = urllib.parse.urlencode(values)
print(params)
# 요청 전용 url 생성
url = API + "?" + params
# print("url=", url)

# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
#print(text)


