from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 id="title">스크레이핑이란?</h1>
    <p id="body">웹 페이지를 분석하는 것 </p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

#find()함수를 사용하면 제일 첫번째의 테그만 가져온다
title = soup.find("h1", id="title")
body = soup.find("p", id="body")

print("#title=" + title.string)
print("#body=" + body.string)