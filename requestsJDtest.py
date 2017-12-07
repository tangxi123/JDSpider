# -*- encoding:utf-8 -*-
import urllib.parse
import requests
import re, json, threading
from bs4 import BeautifulSoup
headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Cookie":"__utmz=122270672.1501576393.1.1.utmcsr=e.jd.com|utmccn=(referral)|utmcmd=referral|utmcct=/30093055.html; ipLoc-djd=1-72-2799-0; qrsc=3; mt_xid=V2_52007VwMSUlpQUlIdSBxsVWMAQFBZXFFGTBtLWxliURpVQVBUUh9VEQkBM1RHAFhZUlsbeRpdBWEfElFBWVdLH0gSXgxsBxZiX2hSah9OHVwBZQcTUW1YV1wY; unpl=V2_ZzNtbUNRFBEhDRRTeR5cAGJUQlwSBUESJwESU34QWw1vUEZZclRCFXMURldnGFkUZwMZXktcRh1FCHZXfBpaAmEBFl5yAR1LI1USFi9JH1c%2bbUgbF0tAHXwIQ119GVwNZgIibUFXcxV0OEZUex5UBW8BE1hyZ0QlRThGXHgaVQ1XAiJcchUXSXwBT1x4EBEFZwMVVUJfQRRwOEdkeA%3d%3d; CCC_SE=ADC_J7ngNvXfn4aVXLVdVq7lOwFUnsnJ9q3D3la0Xg2C%2fPfdjjSFJMDv%2bCfPwAD3q%2fq%2bEK%2bhmBzJ%2f5aJypQJYGPqjSRS6dkLenLPoMiqalnVqxXuC85V7m8YV%2fQI9rV9Ki8IPqLIbavWnTwTlB3uETmNCzmIkdmLVUMOEtQi9kwxQdTBtWXEvSsrnbU0E0xGNBu%2f7dMdwZwhRmxeuPk9PmxZa0uVwwKE2tNjXESkbCrmLr9fUGr7P4Yj0k9EvWlHy6yn5YLKTr843dGfX%2fpTeGsSjjZmup7KbOgQtgAxWN%2fpNEhToZIQm53fgi9YXKMMxyr%2f6rJGKMktR67AY%2bGBkbdxAgf%2fvbRWT1cGv%2fE4fTXdNb5xYFapAko2F%2fOodurTzCUb5%2f%2fS2T1H%2fyPlujmmoOGPdOVF5jlLZCYc%2b%2fBnd0LVSHilMcBV1BmhITQYUstTtcEr%2f5mCN0VUVDvwy83UtTle%2bYgrBSn5tWiZ7mTCE3EwNFOfeF0oDCetGUqEkvbIfAJurj6svvl%2bP6%2b1UV3rWAVhn64k8HiqyVLBc%2bWd7IBin%2b5SR40cBzQ2zX1yT%2bv%2fc6mJRcPT7LDRU6WYdGq5o8Tu54jCbOqFQ3MXzMX5GL9xvLGrrXB8lmmt1ltL27v%2fOPQjtwIJIWTr387ouejxyi%2bbM0%2bHs2UxyZZOyLUaqLmFwRKPqw%2fS69Pk220kiP0KFh9M; __jdv=122270672|google-search|t_262767352_googlesearch|cpc|kwd-298148711900_0_07f5e4c636144fa0ac36c8e648699be5|1512358555108; __jda=122270672.1116919304.1503563219.1512365779.1512367760.12; __jdb=122270672.2.1116919304|12.1512367760; __jdc=122270672; rkv=V0900; xtest=3696.cf6b6759; __jdu=1116919304; 3AB9D23F7A4B3C9B=NHOYHBRI4PQ6ZBCK4MWF2CZQR5E35AECJJAEFJ2QKB2WBZA6RDEBHOQD3C4IMW3J64645A7OV4XHRBKCWN57XB3JGU",
        "DNT":"1",
        "Host":"search.jd.com",
        "Referer":"https://search.jd.com/Search?keyword=%E8%A3%A4%E5%AD%90&enc=utf-8&pvid=ef723dd699054903860a6673a5f5a7ae",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
r = requests.get("https://search.jd.com/Search?keyword=%E8%A3%A4%E5%AD%90&enc=utf-8&pvid=453b410509574c4d857c78201c3c0e40", headers = headers)
r.encoding = 'utf-8'  # 设置编码
html = r.text  # 生成html文件
soup = BeautifulSoup(html, 'html.parser')
shopids = set()
lis = soup.find_all("li", class_='gl-item')
for li in lis:
    spans = li.find_all("span")
    i = 0
    print(spans[2])
    for span in spans:
        i = i+1
        if span['class'][0] == "p-promo-flag":
            print(i)
            #查找shopid
            divs = li.find_all('div')
            for div in divs:
                shopid = div.get("data-shopid")
                if shopid:
                    shopids.add(int(shopid))
                    #print(shopid)



shopnames = set()
for shopid in shopids:
    data = {'ids': shopid}
    r = requests.get("https://search.jd.com/shop_new.php", headers = headers, params=data)
    result = r.json()
    print(r.url)
    for shop in result:
        shopname = shop['shop_name']
        shopnames.add(shopname)
print(shopnames)
# for li in lis:
#     print(li.find('span'))
# print(r.cookies)
# coo = r.cookies
# print(requests.utils.dict_from_cookiejar(coo))
#
# data ={
#     'keyword':'裤子',
#     'enc':'utf-8',
#     'qrst':'1',
#     'rt':'1',
#     'stop':'1',
#     'vt':'2',
#     'page':'14',
#     's':'80',
#     'scrolling':'y',
#     'log_id':'1512453810.41561',
#     'tpl':'3_L',
#     'show_items':''
#     }
#
# r2 = requests.get("https://search.jd.com/s_new.php", headers = headers, params= data)
# r2.encoding = 'utf-8'
# html2 = r2.text
# print(html2)

# r3 = requests.get("https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2560&productId=10365010082&score=0&sortType=5&page=5&pageSize=10&isShadowSku=0&rid=0&fold=1")
# #r3.encoding = 'utf-8'
# fetchJSON_comment = r3.text
# print('type(fetchJSON_comment): %s'%type(fetchJSON_comment))
# print('fetchJSON_comment: %s'%fetchJSON_comment)
# comments = re.findall('fetchJSON_comment98vv2560\((.*?)\);',fetchJSON_comment)
# comments_json = json.loads(comments[0])
# maxPage = comments_json['maxPage']
# print("maxPage: %s"%maxPage)
# finalComments = comments_json['comments']
# for comment in finalComments:
#     content = comment['content']
#     score = comment['score']
#     print('comment: %s'%comment)
#     print('content: %s'%content)
#     print('score: %s'%score)

# def getProductComments(produtId, page):
#     comment_url = "https://sclub.jd.com/comment/productPageComments.action"
#     data = {
#         'callback':'fetchJSON_comment98vv5',
#         'productId':produtId,
#         'score':'0',
#         'sortType':'5',
#         'page':page,
#         'pageSize':'10',
#         'isShadowSku':'0',
#         'fold':'1'
#             }
#     fetchJSON_comment = requests.get(comment_url, params = data).text #获取返回的内容
#     fetchJSON_comment_string = re.findall('\((.*?)\);',fetchJSON_comment) # 使用正则表达式，提取返回的json字符串
#     fetchJSON_comment_json = json.loads(fetchJSON_comment_string[0]) #将字符串转换为json
#     comments = fetchJSON_comment_json['comments'] #获取评论
#     for comment in comments:
#         content = comment['content']
#         score = comment['score']
#         print("content: %s"%content)
#         print("score: %s"%score)
#
# if __name__ == "__main__":
#     comment_url = "https://sclub.jd.com/comment/productPageComments.action"
#     data = {
#         'callback': 'fetchJSON_comment98vv5',
#         'productId':'10319922809',
#         'score': '0',
#         'sortType': '5',
#         'page': 0,
#         'pageSize': '10',
#         'isShadowSku': '0',
#         'fold': '1'
#     }
#     fetchJSON_comment = requests.get(comment_url, params=data).text  # 获取返回的内容
#     fetchJSON_comment_string = re.findall('\((.*?)\);', fetchJSON_comment)  # 使用正则表达式，提取返回的json字符串
#     fetchJSON_comment_json = json.loads(fetchJSON_comment_string[0])  # 将字符串转换为json
#     maxPage = int(fetchJSON_comment_json['maxPage'])  # 获取最大评论页数
#     for page in range(maxPage-1):
#         getProductComments('10319922809', page)
#     # threads = []
#     # for page in range(maxPage-1):
#     #     t = threading.Thread(target=getProductComments('10319922809', page), args = [])
#     #     threads.append(t)
#     #     for t in threads:
#     #         t.start()
#     #         t.join()
#     #     print('end')







