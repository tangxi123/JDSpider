# -*- encoding:utf-8 -*-
import requests
import re
import datetime, time
import os
import json
from bs4 import BeautifulSoup
def getJDComments(product):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "__utmz=122270672.1501576393.1.1.utmcsr=e.jd.com|utmccn=(referral)|utmcmd=referral|utmcct=/30093055.html; ipLoc-djd=1-72-2799-0; qrsc=3; mt_xid=V2_52007VwMSUlpQUlIdSBxsVWMAQFBZXFFGTBtLWxliURpVQVBUUh9VEQkBM1RHAFhZUlsbeRpdBWEfElFBWVdLH0gSXgxsBxZiX2hSah9OHVwBZQcTUW1YV1wY; unpl=V2_ZzNtbUNRFBEhDRRTeR5cAGJUQlwSBUESJwESU34QWw1vUEZZclRCFXMURldnGFkUZwMZXktcRh1FCHZXfBpaAmEBFl5yAR1LI1USFi9JH1c%2bbUgbF0tAHXwIQ119GVwNZgIibUFXcxV0OEZUex5UBW8BE1hyZ0QlRThGXHgaVQ1XAiJcchUXSXwBT1x4EBEFZwMVVUJfQRRwOEdkeA%3d%3d; CCC_SE=ADC_J7ngNvXfn4aVXLVdVq7lOwFUnsnJ9q3D3la0Xg2C%2fPfdjjSFJMDv%2bCfPwAD3q%2fq%2bEK%2bhmBzJ%2f5aJypQJYGPqjSRS6dkLenLPoMiqalnVqxXuC85V7m8YV%2fQI9rV9Ki8IPqLIbavWnTwTlB3uETmNCzmIkdmLVUMOEtQi9kwxQdTBtWXEvSsrnbU0E0xGNBu%2f7dMdwZwhRmxeuPk9PmxZa0uVwwKE2tNjXESkbCrmLr9fUGr7P4Yj0k9EvWlHy6yn5YLKTr843dGfX%2fpTeGsSjjZmup7KbOgQtgAxWN%2fpNEhToZIQm53fgi9YXKMMxyr%2f6rJGKMktR67AY%2bGBkbdxAgf%2fvbRWT1cGv%2fE4fTXdNb5xYFapAko2F%2fOodurTzCUb5%2f%2fS2T1H%2fyPlujmmoOGPdOVF5jlLZCYc%2b%2fBnd0LVSHilMcBV1BmhITQYUstTtcEr%2f5mCN0VUVDvwy83UtTle%2bYgrBSn5tWiZ7mTCE3EwNFOfeF0oDCetGUqEkvbIfAJurj6svvl%2bP6%2b1UV3rWAVhn64k8HiqyVLBc%2bWd7IBin%2b5SR40cBzQ2zX1yT%2bv%2fc6mJRcPT7LDRU6WYdGq5o8Tu54jCbOqFQ3MXzMX5GL9xvLGrrXB8lmmt1ltL27v%2fOPQjtwIJIWTr387ouejxyi%2bbM0%2bHs2UxyZZOyLUaqLmFwRKPqw%2fS69Pk220kiP0KFh9M; __jdv=122270672|google-search|t_262767352_googlesearch|cpc|kwd-298148711900_0_07f5e4c636144fa0ac36c8e648699be5|1512358555108; __jda=122270672.1116919304.1503563219.1512365779.1512367760.12; __jdb=122270672.2.1116919304|12.1512367760; __jdc=122270672; rkv=V0900; xtest=3696.cf6b6759; __jdu=1116919304; 3AB9D23F7A4B3C9B=NHOYHBRI4PQ6ZBCK4MWF2CZQR5E35AECJJAEFJ2QKB2WBZA6RDEBHOQD3C4IMW3J64645A7OV4XHRBKCWN57XB3JGU",
        "DNT": "1",
        "Host": "search.jd.com",
        "Referer": "https://search.jd.com/Search?keyword=%E8%A3%A4%E5%AD%90&enc=utf-8&pvid=ef723dd699054903860a6673a5f5a7ae",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    pageCounts = getProductPages(product) #获取商品页数
    print('pageCounts: %s'%pageCounts)
    if pageCounts == 0:
        return None
    else:
        #res = requests.get('https://search.jd.com/Search', headers=headers, params=data)  # 第一次请求
        # res.encoding = 'utf-8'  # 设置编码
        # html = res.text  # 生成html文件
        # soup = BeautifulSoup(html, 'html.parser')
        # lis = soup.find_all("li", class_='gl-item')
        # for li in lis:
        #     commentsCount = li.find_all("div", "p-commit")[0].strong.a.string
        #     if '万' in commentsCount:
        #         print("数量超过一万，创建txt文件")
        #         #shopName = li.find_all("span", "J_im_icon")[0].a.string
        #         productName = "".join(re.findall(r'>(.*?)<',str(li.find_all("div", "p-name p-name-type-2")[0].a.em)))
        #         today = str(datetime.date.today())
        #         #print(shopName)
        #         print(productName)
        #         print(today)
        #         open("output\\"+"-"+today+"-"+productName+".txt", 'w').close()
        #         fileName = "output\\"+"-"+today+"-"+productName+".txt"
        #         print("进入店铺获取评论，并将评论写入文件中")
        #         # commentUrl = li.find_all("div", "p-commit")[0].strong.a['href']
        #         # print(commentUrl)
        #         #productId = '10319922809'
        #         productId = li.get("data-pid")
        #         maxPage = getCommentMaxPage(productId)
        #         # for page in range(maxPage): #循环获取每页评论
        #         #     getProductComments(productId, page, fileName)
        #     else:
        #         print("评论数小于一万")

        for i in range(1, pageCounts+1):
            page = i*2-1
            data1 = {
                'keyword': product,
                'enc': 'utf-8',
                'qrst': '1',
                'rt': '1',
                'stop': '1',
                'vt': '2',
                'page': page,
                's': '80',
                'scrolling': 'y',
                'log_id': '1512453810.41561',
                'tpl': '3_L',
                'show_items': ''
            }
            res = requests.get("https://search.jd.com/s_new.php", headers = headers, params= data1)  # 第一次请求
            res.encoding = 'utf-8'  # 设置编码
            html = res.text  # 生成html文件
            soup = BeautifulSoup(html, 'html.parser')
            lis = soup.find_all("li", class_='gl-item')
            for li in lis:
                datatype = li.get("data-type")
                #print("datatype: %s"%datatype)
                if datatype:
                    lis.remove(li)
            data_pids = []  # 获取第二个请求参数url中的item-id
            for li in lis:
                data_pid = li.get("data-pid")
                data_pids.append(data_pid)
                # print(li)
                # print(data_pid)
                p_promo_flag = li.find("p-promo-flag")
                if p_promo_flag:
                    print('p_promo_flag: %s'%p_promo_flag)
                commentsCount = li.find_all("div", "p-commit")[0].strong.a.string

                if '万' in commentsCount:
                    print("数量超过一万，创建txt文件")

                    # shopName = li.find_all("span", "J_im_icon")[0].a.string
                    shopName = getShopName(li)
                    #print(shopName)

                    productName = "".join(
                        re.findall(r'>(.*?)<', str(li.find_all("div", "p-name p-name-type-2")[0].a.em))).replace('/', '').replace('*', 'x')
                    #productName = productName.replace('/', '').replace('*', 'x')

                    today = str(datetime.date.today())
                    print(shopName)
                    print(productName)
                    print(today)

                    open("output\\" + shopName+"-" + today + "-" + productName + ".txt", 'w+').close()
                    fileName = "output\\" +shopName+ "-" + today + "-" + productName + ".txt"
                    print("进入店铺获取评论，并将评论写入文件中")
                    # commentUrl = li.find_all("div", "p-commit")[0].strong.a['href']
                    # print(commentUrl)
                    # productId = '10319922809'
                    productId = li.get("data-pid")
                    maxPage = getCommentMaxPage(productId)
                    for page in range(maxPage): #循环获取每页评论
                        getProductComments(productId, page, fileName)
                else:
                    print("评论数小于一万")
            print(data_pids)
            page2 = page + 1
            data2 = {
                'keyword': product,
                'enc': 'utf-8',
                'qrst': '1',
                'rt': '1',
                'stop': '1',
                'vt': '2',
                'page': page2,
                's': '80',
                'scrolling': 'y',
                'log_id': '1512453810.41561',
                'tpl': '3_L',
                'show_items': ''.join(data_pids)
            }
            res = requests.get("https://search.jd.com/s_new.php", headers=headers, params=data2)  # 第一次请求
            res.encoding = 'utf-8'  # 设置编码
            html = res.text  # 生成html文件
            soup = BeautifulSoup(html, 'html.parser')
            lis = soup.find_all("li", class_='gl-item')
            for li in lis:
                datatype = li.get("data-type")
                print("datatype: %s"%datatype)
                if datatype:
                    lis.remove(li)
            for li in lis:
                commentsCount = li.find_all("div", "p-commit")[0].strong.a.string
                if '万' in commentsCount:
                    print("数量超过一万，创建txt文件")
                    shopName = getShopName(li)
                    productName = "".join(
                        re.findall(r'>(.*?)<', str(li.find_all("div", "p-name p-name-type-2")[0].a.em))).replace('/', '').replace('*', 'x')
                    today = str(datetime.date.today())
                    # print(shopName)
                    print(productName)
                    print(today)
                    open("output\\" + shopName+"-" + today + "-" + productName + ".txt", 'w+').close()
                    fileName = "output\\" + shopName+"-" + today + "-" + productName + ".txt"
                    print("进入店铺获取评论，并将评论写入文件中")
                    # commentUrl = li.find_all("div", "p-commit")[0].strong.a['href']
                    # print(commentUrl)
                    # productId = '10319922809'
                    productId = li.get("data-pid")
                    maxPage = getCommentMaxPage(productId)
                    for page in range(maxPage): #循环获取每页评论
                        getProductComments(productId, page, fileName)
                else:
                    print("评论数小于一万")

def getShopName(li):
    # print(li)
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "__utmz=122270672.1501576393.1.1.utmcsr=e.jd.com|utmccn=(referral)|utmcmd=referral|utmcct=/30093055.html; ipLoc-djd=1-72-2799-0; qrsc=3; mt_xid=V2_52007VwMSUlpQUlIdSBxsVWMAQFBZXFFGTBtLWxliURpVQVBUUh9VEQkBM1RHAFhZUlsbeRpdBWEfElFBWVdLH0gSXgxsBxZiX2hSah9OHVwBZQcTUW1YV1wY; unpl=V2_ZzNtbUNRFBEhDRRTeR5cAGJUQlwSBUESJwESU34QWw1vUEZZclRCFXMURldnGFkUZwMZXktcRh1FCHZXfBpaAmEBFl5yAR1LI1USFi9JH1c%2bbUgbF0tAHXwIQ119GVwNZgIibUFXcxV0OEZUex5UBW8BE1hyZ0QlRThGXHgaVQ1XAiJcchUXSXwBT1x4EBEFZwMVVUJfQRRwOEdkeA%3d%3d; CCC_SE=ADC_J7ngNvXfn4aVXLVdVq7lOwFUnsnJ9q3D3la0Xg2C%2fPfdjjSFJMDv%2bCfPwAD3q%2fq%2bEK%2bhmBzJ%2f5aJypQJYGPqjSRS6dkLenLPoMiqalnVqxXuC85V7m8YV%2fQI9rV9Ki8IPqLIbavWnTwTlB3uETmNCzmIkdmLVUMOEtQi9kwxQdTBtWXEvSsrnbU0E0xGNBu%2f7dMdwZwhRmxeuPk9PmxZa0uVwwKE2tNjXESkbCrmLr9fUGr7P4Yj0k9EvWlHy6yn5YLKTr843dGfX%2fpTeGsSjjZmup7KbOgQtgAxWN%2fpNEhToZIQm53fgi9YXKMMxyr%2f6rJGKMktR67AY%2bGBkbdxAgf%2fvbRWT1cGv%2fE4fTXdNb5xYFapAko2F%2fOodurTzCUb5%2f%2fS2T1H%2fyPlujmmoOGPdOVF5jlLZCYc%2b%2fBnd0LVSHilMcBV1BmhITQYUstTtcEr%2f5mCN0VUVDvwy83UtTle%2bYgrBSn5tWiZ7mTCE3EwNFOfeF0oDCetGUqEkvbIfAJurj6svvl%2bP6%2b1UV3rWAVhn64k8HiqyVLBc%2bWd7IBin%2b5SR40cBzQ2zX1yT%2bv%2fc6mJRcPT7LDRU6WYdGq5o8Tu54jCbOqFQ3MXzMX5GL9xvLGrrXB8lmmt1ltL27v%2fOPQjtwIJIWTr387ouejxyi%2bbM0%2bHs2UxyZZOyLUaqLmFwRKPqw%2fS69Pk220kiP0KFh9M; __jdv=122270672|google-search|t_262767352_googlesearch|cpc|kwd-298148711900_0_07f5e4c636144fa0ac36c8e648699be5|1512358555108; __jda=122270672.1116919304.1503563219.1512365779.1512367760.12; __jdb=122270672.2.1116919304|12.1512367760; __jdc=122270672; rkv=V0900; xtest=3696.cf6b6759; __jdu=1116919304; 3AB9D23F7A4B3C9B=NHOYHBRI4PQ6ZBCK4MWF2CZQR5E35AECJJAEFJ2QKB2WBZA6RDEBHOQD3C4IMW3J64645A7OV4XHRBKCWN57XB3JGU",
        "DNT": "1",
        "Host": "search.jd.com",
        "Referer": "https://search.jd.com/Search?keyword=%E8%A3%A4%E5%AD%90&enc=utf-8&pvid=ef723dd699054903860a6673a5f5a7ae",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

    if li.find("span",class_="p-promo-flag"):
        # 查找shopid
        divs = li.find_all('div')
        for div in divs:
            # print("........hello........")
            # print("div: %s" % div)
            shopid = div.get("data-shopid")
            if shopid:
                print("shopid: %s" % shopid)
                data = {'ids': shopid}
                r = requests.get("https://search.jd.com/shop_new.php", headers=headers, params=data)
                result = r.json()
                print(r.url)
                for shop in result:
                    shopName = shop['shop_name']
                    print(shopName)
                    return shopName

    elif li.find_all("span","J_im_icon"):
        shopName = li.find_all("span", "J_im_icon")[0].a.string
        print(shopName)
        return shopName
    else:
        shopName = "【京东自营，品质保障】"
        return shopName



def getProductPages(product):
    data = {'keyword':product,
            'enc':'utf-8',
            'pvid':'e246b4b298134e259b984b733a64c394'}  # 传入参数
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Cookie':'__utmz=122270672.1501576393.1.1.utmcsr=e.jd.com|utmccn=(referral)|utmcmd=referral|utmcct=/30093055.html; ipLoc-djd=1-72-2799-0; qrsc=3; unpl=V2_ZzNtbUNRFBEhDRRTeR5cAGJUQlwSBUESJwESU34QWw1vUEZZclRCFXMURldnGFkUZwMZXktcRh1FCHZXfBpaAmEBFl5yAR1LI1USFi9JH1c%2bbUgbF0tAHXwIQ119GVwNZgIibUFXcxV0OEZUex5UBW8BE1hyZ0QlRThGXHgaVQ1XAiJcchUXSXwBT1x4EBEFZwMVVUJfQRRwOEdkeA%3d%3d; __jdv=122270672|google-search|t_262767352_googlesearch|cpc|kwd-298148711900_0_07f5e4c636144fa0ac36c8e648699be5|1512358555108; mt_xid=V2_52007VwMSUlpQUlIdSBxsVmEHQQYNW1BGTEkZDhliCxNRQVEBXEtVHwsBYFcQAV4IUQhKeRpdBWEfElFBWVdLH0wSXgJsAxBiX2hSah9OHV8GYQAXVm1YV1wY; xtest=3696.cf6b6759; rkv=V0900; __jda=122270672.1116919304.1503563219.1512375844.1512440318.14; __jdc=122270672; 3AB9D23F7A4B3C9B=NHOYHBRI4PQ6ZBCK4MWF2CZQR5E35AECJJAEFJ2QKB2WBZA6RDEBHOQD3C4IMW3J64645A7OV4XHRBKCWN57XB3JGU; __jdu=1116919304',
        'DNT':'1',
        'Host':'search.jd.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    }
    res = requests.get('https://search.jd.com/Search', headers=headers, params=data)  # 第一次请求
    res.encoding = 'utf-8'  # 设置编码
    html = res.text  # 生成html文件
    soup = BeautifulSoup(html, 'html.parser')
    str1 = soup.find_all('script')[-6].string  # 查找到总页数：page_count所在的行
    page_count = re.findall(r'page_count:"(.*?)"', str1)  # 根据正则表达式获取总页数
    pagecounts = int(page_count[0])
    # 如果总页数超过10，则页数为10，大于0小于10时，页数为个位数，等于0时，给出提示信息
    if pagecounts > 10:
        pagecounts = 10
    elif pagecounts > 0 and pagecounts < 10:
        pagecounts = pagecounts
    else:
        pagecounts = 0
        print("没有相关产品请重新查询")
    return pagecounts

def getProducts(productId):
    pass

def getProductComments(produtId, page, filename):
    comment_url = "https://club.jd.com/comment/skuProductPageComments.action"
    data = {
        'productId': produtId,
        'score': '0',
        'sortType': '5',
        'page': page,
        'pageSize': '10',
        'isShadowSku': '0',
        'fold': '1'
    }
    fetchJSON_comment = requests.get(comment_url, params=data).text  # 获取返回的内容
    print('fetchJSON_comment: %s'%fetchJSON_comment)
    # fetchJSON_comment_string = re.findall('\((.*?)\);', fetchJSON_comment)  # 使用正则表达式，提取返回的json字符串
    # print('fetchJSON_comment_string: %s'%fetchJSON_comment_string)
    fetchJSON_comment_json = json.loads(fetchJSON_comment)  # 将字符串转换为json
    print('fetchJSON_comment_json: %s'%fetchJSON_comment_json)
    comments = fetchJSON_comment_json['comments']  # 获取评论
    f = open(filename, "a")
    for comment in comments:
        content = comment['content']
        score = str(comment['score'])
        print("score: %s" % score)
        print("content: %s" % content)
        f.write("score: %s\n" % score.encode('gbk', errors='replace').decode('gbk'))
        f.write("content: %s\n" % content.encode('gbk', errors='replace').decode('gbk'))

def getCommentMaxPage(productId):
    comment_url = "https://sclub.jd.com/comment/skuProductPageComments.action"
    data = {
        'callback': 'fetchJSON_comment98vv5',
        'productId': productId,
        'score': '0',
        'sortType': '5',
        'page': 0,
        'pageSize': '10',
        'isShadowSku': '0',
        'fold': '1'
    }
    fetchJSON_comment = requests.get(comment_url, params=data).text  # 获取返回的内容
    fetchJSON_comment_string = re.findall('\((.*?)\);', fetchJSON_comment)  # 使用正则表达式，提取返回的json字符串
    fetchJSON_comment_json = json.loads(fetchJSON_comment_string[0])  # 将字符串转换为json
    maxPage = int(fetchJSON_comment_json['maxPage'])  # 获取最大评论页数
    return maxPage






if __name__ == "__main__":
    getJDComments("裤子")