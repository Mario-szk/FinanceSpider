import time
import Database
from selenium import webdriver
from bs4 import BeautifulSoup

def get_content (html,num):
    cont_list = BeautifulSoup(html, 'lxml').find_all('tr')[num]
    cont_lists = [ item.text for item in cont_list ]
    return cont_lists


def data_input (list,connect,cursor):
    # connect = pymysql.connect(host='localhost',user='root',password='root',db='test',charset='utf8')
    # cursor = connect.cursor()

    if len(list) == 13:
        Database.dataModelGain(connect,cursor,list)
        # sql = "insert into jrj_gather(date,rongzi_yue,rongzi_yuezengjian,rongzi_shizhi,rongzi_mairue,rongzi_changhuange,rongquan_yuliang,rongquan_maichu,rongquan_changhuan,rongzirongquanyue,chazhi,rongzi_gegu,rongquan_gegu) value ("+"'"+list[0]+"'"+ "," +"'"+list[1]+"'"+ "," +"'"+list[2]+"'"+ "," +"'"+list[3]+"'"+ "," +"'"+list[4]+"'"+ "," +"'"+list[5]+"'"+ "," +"'"+list[6]+"'"+ "," +"'"+list[7]+"'"+ "," +"'"+list[8]+"'"+ "," +"'"+list[9]+"'"+ "," +"'"+list[10]+"'"+ "," +"'"+list[11]+"'"+ "," +"'"+list[12]+"'"+") "
        #
        # cursor.execute(sql)
        # connect.commit()
    else:
        return 'none'


def page_roll (driver,html,connect,cursor):
    # page
    for j in range(1,114):
        # last
        if j is 113:
            # get
            for i in range(2, 17):  # 2,17
                list = get_content(html, i)
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
        driver.execute_script('document.getElementsByClassName("next")[0].click()')  # 此处的坑就是dom操作
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
    connect, cursor = Database.connect()
    Database.createTable(cursor, 'sqlModelGain')

    # 数据获取
    page_roll(driver,html,connect,cursor)

    Database.dataClose(connect)

    driver.close()      # 浏览器还在

    driver.quit()       # 退出浏览器


