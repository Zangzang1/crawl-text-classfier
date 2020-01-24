import requests
from bs4 import BeautifulSoup
import xlwt
import xlrd
from xlutils.copy import copy
from threading import Timer
import time
import random
import json



keys = [
'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19',
'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
'Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3'
]
def get_tweets_information(num):
    pagenum=num
    if pagenum ==0:
        url = 'http://www.twiview.com/'
    else:
        url = 'http://www.twiview.com/home-{}'.format(pagenum)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Connection': 'close'
    }
    num= (num+random.randint(0,10))  % 10
    headers['User-Agent']=keys[num]
    content = requests.get(url,headers=headers)
    requests.adapters.DEFAULT_RETRIES = 5
    content.enconding = 'utf-8'
    content = content.text
    if pagenum>0:
        content=content.replace('\\n','').replace('\\\"', "\"")
    soup = BeautifulSoup(content,'html.parser')

    links1 = soup.select('.twiimage-item .item-content')
    workbook = xlrd.open_workbook('tweetsinforamtion.xls')  # 打开工作簿
    worksheet = workbook.sheet_by_name('tweetsinforamtion')  # 获取工作簿中所有表格中的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    j=0
    for i in links1:
        User_name = i.select('.user-name span')[0].text#.encode('utf-8').decode('unicode_escape')
        new_worksheet.write(j + rows_old, 0, User_name)
        User_name2 = i.select('.user-name span')[1].text
        new_worksheet.write(j + rows_old, 1, User_name2)
        User_img = i.select('.user-img img')[0].get('src')
        new_worksheet.write(j + rows_old, 2, User_img)
        User_Posturl=i.select('.post-url')[0].get('href')
        new_worksheet.write(j + rows_old, 3, User_Posturl)
        User_text = i.select('.twiimage-text')[0].text.strip().lstrip()#.encode('utf-8').decode('unicode_escape')
        new_worksheet.write(j + rows_old, 4, User_text)
        User_posttime = i.select('.post-time')[0].text
        new_worksheet.write(j + rows_old, 5, User_posttime)
        User_like=i.select('.likes')[0].text
        new_worksheet.write(j + rows_old, 6, User_like)
        User_retweets=i.select('.retweets')[0].text
        new_worksheet.write(j + rows_old, 7, User_retweets)
        j=j+1
    new_workbook.save('tweetsinforamtion.xls')

def run_search(i):
    print("----------第"+str(i)+"次爬取---------")
    t = Timer(5, get_tweets_information,[i]) #,args=("num="+str(i))
    # 调用start之后启动,并且不会阻塞，因为单独开启了一个线程
    t.start()
    time.sleep(5)
    i=i+1
    run_search(i)
def creat_xlsbook():
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet =workbook.add_sheet('tweetsinforamtion',cell_overwrite_ok=True)
    head=['name','@name','headimg','postUrl','text','postTime','likes','retweets']
    for i in range(len(head)):
        worksheet.write(0, i,head[i])
    workbook.save('tweetsinforamtion.xls')
if __name__ == '__main__':
    creat_xlsbook()
    run_search(1)




