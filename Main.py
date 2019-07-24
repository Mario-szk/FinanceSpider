
import ModelGain,Units
import DataConfig


ModelGain.run()
list = ['sh601318','sh600831','sz000063','sz002415']
# 数据库配置
connect,cursor = DataConfig.connect()
DataConfig.createTable(cursor, 'sqlUnits')
for i in list:
    connect, cursor = DataConfig.connect()
    Units.run(i,connect,cursor)
    DataConfig.dataClose(connect)