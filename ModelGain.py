
import time
import DataConfig
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import decimal


def get_content (html,num):

    cont_list = BeautifulSoup(html, 'lxml').find_all('tr')[num]
    cont_lists = [item.text for item in cont_list]

    #单位统一
    wan = '万'
    for j in range(13):
        result = wan in cont_lists[j]
        if result:
            data = str(decimal.Decimal(re.findall('\-\d+\.\d+|\d+\.\d+|--', cont_lists[j])[0]) / 10000)
            cont_lists[j] = data


    #匹配数字
    content = []
    for i in range(13):
        if i is 0:
            content.append(cont_lists[i])
        elif i>0 and i<=10:
            content.append(re.findall('\-\d+\.\d+|\d+\.\d+|--', cont_lists[i])[0])
            if content[-1] == '--':
                content[-1] = '0'
        else:
            content.append(cont_lists[i])

    return content


def data_input (list,connect,cursor):
    if len(list) == 13:
        DataConfig.dataModelGain(connect,cursor,list)
    else:
        return 'none'


def page_roll (driver,html,connect,cursor):
    # page
    for j in range(1,114):
        # last
        if j is 113:
            # get
            for i in range(2, 22):  # 2,17
                list = get_content(html,i)
                if list is 'stop':
                    print(list)
                    # record
                    with open("./log/testModelGain.txt", "a") as f:
                        f.write("页面加载错误\r\n")
                    break
                else:
                    isNone = data_input(list,connect,cursor)
                    if isNone is 'none':
                        with open("./log/testModelGain.txt", "a") as f:
                            f.write('第' + str(j) + '页，第' + str(i - 2) + '行录入失败，数据加载失败\r\n')
                    print(list)

                # record
                with open("./log/testModelGain.txt", "a") as f:
                    f.write('第' + str(j) + '页录入完成\r\n')

                return
        else:
            # get
            for i in range(2, 22):  # 2.22
                list = get_content(html, i)
                if '正在加载中......' in list:
                    print(list)
                    # record
                    with open("./log/testModelGain.txt", "a") as f:
                        f.write("页面加载错误\r\n")
                    break
                else:
                    isNone = data_input(list,connect,cursor)
                    if isNone is 'none':
                        with open("./log/testModelGain.txt", "a") as f:
                            f.write('第' + str(j) + '页，第' + str(i - 1) + '行录入失败，数据加载失败\r\n')
                    print(list)

        # 下一页
        driver.execute_script("document.getElementsByClassName('next')[0].click()")  # 此处的坑就是dom操作
        time.sleep(12)
        # 得到页面源码
        html = driver.page_source
        # record
        with open("./log/testModelGain.txt", "a") as f:
            f.write('第' + str(j) + '页录入完成\r\n')

    return




def run ():
    url = 'http://stock.jrj.com.cn/rzrq/jyzs.shtml'

    driver = webdriver.PhantomJS()
    driver.get(url)     #得到你的网页链接

    html = driver.page_source

    # 数据库配置
    connect, cursor = DataConfig.connect()
    DataConfig.createTable(cursor, 'sqlModelGain')

    # 数据获取
    page_roll(driver,html,connect,cursor)

    DataConfig.dataClose(connect)

    driver.close()      # 浏览器还在

    driver.quit()       # 退出浏览器

