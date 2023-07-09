import urllib.request

url = "http://ura.pw/shodou/img/28/214.png"
savename = "test.png"

# 데이터를 메모리에 올리면서 저장(urlopen())
mem = urllib.request.urlopen(url).read()

with open(savename, mode='wb') as f:
    f.write(mem)
    print("저장되었습니다.")
