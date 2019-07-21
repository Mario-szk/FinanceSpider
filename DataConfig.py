import pymysql

# 配置的连接信息
host = 'localhost'
user = 'root'
password = 'root'
db = 'newtest'
charset = 'utf8'


def connect ():
    global host,user,password,db,chasrset
    connect = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
    cursor = connect.cursor()       #创建一个游标对象 cursor
    return connect,cursor


def createTable (cursor,sql):
    sqlUnits = """CREATE TABLE `units_gather` (
  `date` datetime NOT NULL,
  `rongzi_yue` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzi_shizhibi` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzi_mairue` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzi_jiaoebi` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzi_changhuange` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongquan_yuliang` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongquan_maichu` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongquan_changhuan` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongquan_yuliangbiliutongpan` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzirongquanyue` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `yuechazhi` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `code` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `id` int(255) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=445 DEFAULT CHARSET=latin1;"""



    sqlModelGain = """ 
        CREATE TABLE `jrj_gather` (
  `date` varchar(10) CHARACTER SET utf8 NOT NULL,
  `rongzi_yue` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzi_yuezengjian` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzi_shizhi` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzi_mairue` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzi_changhuange` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongquan_yuliang` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongquan_maichu` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongquan_changhuan` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzirongquanyue` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `chazhi` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongzi_gegu` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  `rongquan_gegu` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
    """

    if sql is 'sqlModelGain':
        cursor.execute(sqlModelGain)
    elif sql is 'sqlUnits':
        cursor.execute(sqlUnits)

    return


def dataUnits (connect,cursor,unit,list):
    sql = "insert into units_gather(date,rongzi_yue,rongzi_shizhibi,rongzi_mairue,rongzi_jiaoebi,rongzi_changhuange,rongquan_yuliang,rongquan_maichu,rongquan_changhuan,rongquan_yuliangbiliutongpan,rongzirongquanyue,yuechazhi,code) value (" + "'" + list[0] + "'" + "," + "'" + list[1] + "'" + "," + "'" + list[2] + "'" + "," + "'" + list[3] + "'" + "," + "'" + list[4] + "'" + "," + "'" + list[5] + "'" + "," + "'" + list[6] + "'" + "," + "'" + list[7] + "'" + "," + "'" + list[8] + "'" + "," + "'" + list[9] + "'" + "," + "'" + list[10] + "'" + "," + "'" + list[11] + "'""," +"'"+unit+"'"+") "

    cursor.execute(sql)
    connect.commit()
    return

def dataModelGain (connect,cursor,list):
    sql = "insert into jrj_gather(date,rongzi_yue,rongzi_yuezengjian,rongzi_shizhi,rongzi_mairue,rongzi_changhuange,rongquan_yuliang,rongquan_maichu,rongquan_changhuan,rongzirongquanyue,chazhi,rongzi_gegu,rongquan_gegu) value (" + "'" + list[0] + "'" + "," + "'" + list[1] + "'" + "," + "'" + list[2] + "'" + "," + "'" + list[3] + "'" + "," + "'" + list[4] + "'" + "," + "'" + list[5] + "'" + "," + "'" + list[6] + "'" + "," + "'" + list[7] + "'" + "," + "'" + list[8] + "'" + "," + "'" + list[9] + "'" + "," + "'" + list[10] + "'" + "," + "'" + list[11] + "'" + "," + "'" + list[12] + "'" + ") "

    cursor.execute(sql)
    connect.commit()
    return

def dataClose (connect):
    connect.close
    return

