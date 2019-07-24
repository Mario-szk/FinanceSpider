
import pymysql

# 配置的连接信息
host = 'localhost'
user = 'root'
password = 'root'
db = 'test'
charset = 'utf8'


def connect ():
    global host,user,password,db,chasrset
    connect = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
    cursor = connect.cursor()       #创建一个游标对象 cursor
    return connect,cursor


def createTable (cursor,sql):
    sqlUnits = """CREATE TABLE `units_gather` (
  `code` varchar(100) DEFAULT NULL COMMENT '股票代码',
  `date` date NOT NULL COMMENT '交易日期',
  `rongzi_yue` int(100) DEFAULT NULL COMMENT '余额',
  `rongzi_shizhibi` int(100) DEFAULT NULL COMMENT '占流通市值比（单位：%）',
  `rongzi_mairue` int(100) DEFAULT NULL COMMENT '买入额',
  `rongzi_jiaoebi` int(100) DEFAULT NULL COMMENT '占成交额比（单位：%）',
  `rongzi_changhuange` int(100) DEFAULT NULL COMMENT '偿还额',
  `rongquan_yuliang` int(100) DEFAULT NULL COMMENT '余量',
  `rongquan_maichu` int(100) DEFAULT NULL COMMENT '卖出量',
  `rongquan_changhuan` int(100) DEFAULT NULL COMMENT '偿还量',
  `rongquan_yuliangbiliutongpan` int(100) DEFAULT NULL COMMENT '融券余量\r\n/流通盘',
  `rongzirongquanyue` int(100) DEFAULT NULL COMMENT '融资融券\r\n余额',
  `yuechazhi` int(100) DEFAULT NULL COMMENT '余额差值',
  `id` int(255) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;"""



    sqlModelGain = """ 
        CREATE TABLE `jrj_gather` (
  `date` date NOT NULL COMMENT '交易日期',
  `rongzi_yue` int(100) DEFAULT NULL COMMENT '余额',
  `rongzi_yuezengjian` int(100) DEFAULT NULL COMMENT '余额增减',
  `rongzi_shizhi` int(100) DEFAULT NULL COMMENT '融资余额/流通市值（单位：%）',
  `rongzi_mairue` int(100) DEFAULT NULL COMMENT '买入额',
  `rongzi_changhuange` int(100) DEFAULT NULL COMMENT '偿还额',
  `rongquan_yuliang` int(100) DEFAULT NULL COMMENT '余量',
  `rongquan_maichu` int(100) DEFAULT NULL COMMENT '卖出量',
  `rongquan_changhuan` int(100) DEFAULT NULL COMMENT '偿还量',
  `rongzirongquanyue` int(100) DEFAULT NULL COMMENT '融资融券\r\n余额',
  `chazhi` int(100) DEFAULT NULL COMMENT '余额差值',
  `rongzi_gegu` int(100) DEFAULT NULL COMMENT '融资个股',
  `rongquan_gegu` int(100) DEFAULT NULL COMMENT '融券个股',
  PRIMARY KEY (`date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
    """

    if sql is 'sqlModelGain':
        cursor.execute(sqlModelGain)
    elif sql is 'sqlUnits':
        cursor.execute(sqlUnits)

    return


def dataUnits (connect,cursor,unit,list):
    sql = "insert into units_gather(code,date,rongzi_yue,rongzi_shizhibi,rongzi_mairue,rongzi_jiaoebi,rongzi_changhuange,rongquan_yuliang,rongquan_maichu,rongquan_changhuan,rongquan_yuliangbiliutongpan,rongzirongquanyue,yuechazhi) value ("+"'"+unit+"'" + "," + "'" + list[0] + "'" + "," + "'" + list[1] + "'" + "," + "'" + list[2] + "'" + "," + "'" + list[3] + "'" + "," + "'" + list[4] + "'" + "," + "'" + list[5] + "'" + "," + "'" + list[6] + "'" + "," + "'" + list[7] + "'" + "," + "'" + list[8] + "'" + "," + "'" + list[9] + "'" + "," + "'" + list[10] + "'" + "," + "'" + list[11] + "'"+ ") "

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

