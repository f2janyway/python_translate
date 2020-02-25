import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
driver = webdriver.Chrome('C:\\Users\\jyg41\\Desktop\\chromedriver')
text = 'easy%20multi%20timer'
lang = ('es','hi'
,'id','ja','vi','zh-CN','ar','ru','de','it','th','pt','fr','fi','tl','tr','kk','ms','mn','uk','sw','si','hy','az','af','et','ne','el','no','nl','iw')
ko = ('스페인','힌디','인도네시아','재팬','베트남','중국','아랍','러시아','독일','이탈리아','태국','포루투갈','프랑스','핀란드','필리핀','터키','카자흐','말레이어','몽골',
'우크라이나','스와힐리어','스리랑카','아르메니아','아르바이잔어','아프리칸어','에스토니아','네팔','그리스','노르웨이','네덜란드','히브리')
# print(lang)
# print(ko)
f = open('C:\\Users\\jyg41\\Desktop\\title_translate.txt',mode='w',encoding='utf-8')
for i in range(0,len(lang)) :
#   # req = requests.get('https://translate.google.com/#view=home&op=translate&sl=ko&tl='+i+'&text=' + text)
  
  driver.get('https://translate.google.com/#view=home&op=translate&sl=en&tl='+lang[i]+'&text=' + text)
  time.sleep(2)
  sel = 'div.frame > div.page.tlid-homepage.homepage.translate-text > div.homepage-content-wrap > div.tlid-source-target.main-header > div.source-target-row > div.tlid-results-container.results-container > div.tlid-result.result-dict-wrapper > div.result.tlid-copy-target > div.text-wrap.tlid-copy-target > div > span.tlid-translation.translation > span'
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')
  contents = soup.select(sel)
  # time.sleep(2)
  s = '\n' + lang[i] + "/" +ko[i] + '\n'
  for el in contents:
    s += el.text +'\n'
#   print(i)
#   print(contents[0].text)
  f.write(s)
  print(s)
#   print('=================================')
#   # arr[i] = contents
  
  

# ## HTTP Header 가져오기
# header = req.headers
# ## HTTP Status 가져오기 (200: 정상)
# status = req.status_code
# ## HTTP가 정상적으로 되었는지 (True/False)
# is_ok = req.ok



