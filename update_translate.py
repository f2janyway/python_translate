import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
driver = webdriver.Chrome('C:\\Users\\jyg41\\Desktop\\chromedriver')
dic = {"en":
[["<en-US>", "</en-US>"],["<en-AU>","</en-AU>"],["<en-CA>","</en-CA>"],["<en-GB>","</en-GB>"],["<en-IN>","</en-IN>"],["<en-SG>","</en-SG>"],["<en-ZA>","</en-ZA>"]],
"af":["<af>","</af>"],
"ar":["<ar>","</ar>"],
"az":["<az-AZ>","</az-AZ>"],
"de":["<de-DE>","</de-DE>"],
"el":["<el-GR>","</el-GR>"],
"es":[["<es-419>","</es-419>"],["<es-ES>","</es-ES>"],["<es-US>","</es-US>"]],
"et":["<et>","</et>"],
"fi":["<fi-FI>","</fi-FI>"],
"tl":["<fil>","</fil>"],
"fr":[["<fr-FR>","</fr-FR>"],["<fr-CA>","</fr-CA>"]],
"hi":["<hi-IN>","</hi-IN>"],
"hy":["<hy-AM>","</hy-AM>"],
"id":["<id>","</id>"],
"it":["<it-IT>","</it-IT>"],
"iw":["<iw-IL>","</iw-IL>"],
"ja":["<ja-JP>","</ja-JP>"],
"kk":["<kk>","</kk>"],
"ko":["<ko-KR>","</ko-KR>"],
"mn":["<mn-MN>","</mn-MN>"],
"ms":[["<ms-MY>","</ms-MY>"],["<ms>","</ms>"]],
"ne":["<ne-NP>","</ne-NP>"],
"nl":["<nl-NL>","</nl-NL>"],
"no":["<no-NO>","</no-NO>"],
"pt":[["<pt-BR>","</pt-BR>"],["<pt-PT>","</pt-PT>"]],
"ru":["<ru-RU>","</ru-RU>"],
"si":["<si-LK>","</si-LK>"],
"sw":["<sw>","</sw>"],
"th":["<th>","</th>"],
"tr":["<tr-TR>","</tr-TR>"],
"uk":["<uk>","</uk>"],
"vi":["<vi>","</vi>"],
"zh-CN":[["<zh-CN>","</zh-CN>"],["<zh-TW>","</zh-TW>"],["<zh-HK>","</zh-HK>"]]
}

# text 변수만 잘 정리하면 쭉 나온다.
text = 'Added%20sound%20function'
enText = 'Added sound function '
f = open('C:\\Users\\jyg41\\Desktop\\memo_translate.txt',mode='w',encoding='utf-8')
for key in dic:
    # print(len(dic[key]),dic[key])
    driver.get('https://translate.google.com/#view=home&op=translate&sl=en&tl='+key+'&text=' + text)
    time.sleep(1)
    sel = 'div.frame > div.page.tlid-homepage.homepage.translate-text > div.homepage-content-wrap > div.tlid-source-target.main-header > div.source-target-row > div.tlid-results-container.results-container > div.tlid-result.result-dict-wrapper > div.result.tlid-copy-target > div.text-wrap.tlid-copy-target > div > span.tlid-translation.translation > span'
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    contents = soup.select(sel)
    s= ""
    # print(contents,key)
    for el in contents:
        s += el.text 
    
    if len(dic[key]) == 2:
        if len(dic[key][0] ) == 2:
            for i in dic[key]:
                print(i[0])
                print(s)
                print(i[1])

        else:
            print(dic[key][0])
            print(s)
            print(dic[key][1])
    else:
        for e in dic[key]:
            if key != 'en':
                print(e[0])
                print(s)
                print(e[1])
            else:
                print(e[0])
                print(enText)
                print(e[1])



# # lang = ('en','es','hi'
# # ,'id','ja','vi','zh-CN','ar','ru','de','it','th','pt','fr','fi','tl','tr','kk','ms','mn','uk','sw','si','hy','az','af','et','ne','el','no','nl','iw')
# # ko = ('영어','스페인','힌디','인도네시아','재팬','베트남','중국','아랍','러시아','독일','이탈리아','태국','포루투갈','프랑스','핀란드','필리핀','터키','카자흐','말레이어','몽골',
# # '우크라이나','스와힐리어','스리랑카','아르메니아','아르바이잔어','아프리칸어','에스토니아','네팔','그리스','노르웨이','네덜란드','히브리')
# f = open('C:\\Users\\jyg41\\Desktop\\update_translate.txt',mode='w',encoding='utf-8')
# for i in range(0,len(lang)) :
  
#     driver.get('https://translate.google.com/#view=home&op=translate&sl=en&tl='+lang[i]+'&text=' + text)
#     time.sleep(2)
#     sel = 'div.frame > div.page.tlid-homepage.homepage.translate-text > div.homepage-content-wrap > div.tlid-source-target.main-header > div.source-target-row > div.tlid-results-container.results-container > div.tlid-result.result-dict-wrapper > div.result.tlid-copy-target > div.text-wrap.tlid-copy-target > div > span.tlid-translation.translation > span'
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     contents = soup.select(sel)
#     s = '\n' + lang[i] + "/" +ko[i] + '\n'
#     for el in contents:
#       s += el.text +'\n'
#     f.write(s)
#     print(s)



