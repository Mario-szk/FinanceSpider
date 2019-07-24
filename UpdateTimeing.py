
import DataConfig
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import decimal


def get_content (html,num):

    cont_list = BeautifulSoup(html, 'lxml').find_all('tr')[num]
    cont_lists = [item.text for item in cont_list]

    # 单位统一
    wan = '万'
    for i in range(13):
        result = wan in cont_lists[i]
        if result:
            data = str(decimal.Decimal(re.findall('\-\d+\.\d+|\d+\.\d+|--', cont_lists[i])[0]) / 10000)
            cont_lists[i] = data


    #匹配数字
    content = []
    for i in range(13):
        if i is 0:
            content.append(cont_lists[i])
        elif i>0 and i<=10:
            content.append(re.findall('\d+\.\d+', cont_lists[i])[0])
        else:
            content.append(cont_lists[i])

    return content


def data_input (list,connect,cursor):
    if len(list) == 13:
        DataConfig.dataModelGain(connect,cursor,list)
    else:
        return 'none'


def page (html,connect,cursor):
    # get
    list = get_content(html,2)
    if '正在加载中......' in list:
        print(list)
        # record
        with open("./log/daliy.txt", "a") as f:
                f.write("页面加载错误\r\n")
    else:
        isNone = data_input(list, connect, cursor)
        if isNone is 'none':
            with open("./log/daliy.txt", "a") as f:
                f.write('数据加载失败\r\n')
        print(list)


    # record
    with open("./log/daliy.txt", "a") as f:
        f.write('录入完成\r\n')

    return


def modelGain ():
    url = 'http://stock.jrj.com.cn/rzrq/jyzs.shtml'

    driver = webdriver.PhantomJS()
    driver.get(url)  # 得到你的网页链接

    html = driver.page_source

    # 数据库配置
    connect,cursor = DataConfig.connect()

    # 数据获取
    page(html, connect, cursor)

    DataConfig.dataClose(connect)

    driver.close()  # 浏览器还在

    driver.quit()  # 退出浏览器


######################################


def get_content_unit (html,num):
    cont_list = BeautifulSoup(html, 'lxml').find_all('tr')[num]
    cont_lists = [item.text for item in cont_list]

    # 单位统一
    wan = '万'
    for i in range(12):
        result = wan in cont_lists[i]
        if result:
            data = str(decimal.Decimal(re.findall('\-\d+\.\d+|\d+\.\d+|--', cont_lists[i])[0]) / 10000)
            cont_lists[i] = data

    #匹配数字
    content = []
    for i in range(12):
        if i is 0:
            content.append(cont_lists[i])
        else:
            content.append(re.findall('\d+\.\d+', cont_lists[i])[0])

    return content


def data_input_unit (list,unit,connect,cursor):
    if len(list) == 12:
        DataConfig.dataUnits(connect,cursor,unit,list)
    else:
        return 'none'


def page_unit (html,unit,connect,cursor):
    # get
    list = get_content_unit(html,2)
    if '正在加载中......' in list:
        print(list)
        # record
        with open("./log/daliyUnit.txt", "a") as f:
            f.write("页面加载错误\r\n")
    else:
        isNone = data_input_unit(list, unit, connect, cursor)
        if isNone is 'none':
            with open("./log/daliyUnit.txt", "a") as f:
                f.write('数据加载失败\r\n')
        print(list)

    # record
    with open("./log/daliyUnit.txt", "a") as f:
        f.write('录入完成\r\n')

    return


def split (unit):
    unit_split = unit[2:8]
    return unit_split


def run (unit):

    url = 'http://stock.jrj.com.cn/share,'+split(unit)+',rzrq.shtml'

    driver = webdriver.PhantomJS()
    driver.get(url)     #得到你的网页链接

    html = driver.page_source

    # 数据库配置
    connect,cursor = DataConfig.connect()

    # 数据获取
    page_unit(html,unit,connect,cursor)

    DataConfig.dataClose(connect)

    driver.close()      # 浏览器还在

    driver.quit()       # 退出浏览器

def func():
    modelGain()
    list = ['sh601318', 'sh600831', 'sz000063', 'sz002415']
    for i in list:
        run(i)
    # timer = threading.Timer(86400, func)
    # timer.start()

#定时器,参数为(多少时间后执行，单位为秒，执行的方法)
# timer = threading.Timer(86400, func)
# timer.start()

func()