import pymysql
from common.log import log
from settings import DB_CONFIG

class MysqlAuto:
    def __init__(self):
        # 读取配置文件，初始化pymysql数据库连接
        #** 接受字典类型的实际可变参数
        self.db = pymysql.connect(**DB_CONFIG)
        # 创建数据库游标  返回字典类型的数据
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        log.info(f"{DB_CONFIG['host']}数据库连接成功！")
        # 获取单条数据
    def get_fetchone(self, sql):
        # 执行sql
        self.cursor.execute(sql)
        # 查询单条数据，结果返回
        return self.cursor.fetchone()
        # 获取多条数据
    def get_fetchall(self, sql):
        # 执行sql
        self.cursor.execute(sql)
        # 查询多条数据，结果返回
        return self.cursor.fetchall()
        # 执行更新类sql
    def sql_execute(self, sql):
        try:
            # db对象和指针对象同时存在
            if self.db and self.cursor:
                # 执行sql
                log.info(f"执行sql语句：{sql}")
                print("sql是",sql)
                self.cursor.execute(sql)
                log.debug(self.cursor.fetchall())
                # 提交执行sql到数据库，完成insert或者update相关命令操作，非查询时使用
                self.db.commit()
                return  True
        except Exception as e:
            log.error(f"执行sql语句失败：{sql}，原因：{e}")
            # 出现异常时，数据库回滚
            self.db.rollback()
            # 返回结果为失败
            return False
        # 关闭对象，staticmethod静态方法，可以直接使用类名.静态方法。
    @staticmethod
    def close(self):
        # 判断游标对象是否存在
        if self.cursor is not None:
            # 存在则关闭指针
            self.cursor.close()
        # 判断数据库对象是否存在
        if self.db is not None:
            # 存在则关闭数据库对象
            self.db.close()
        log.info(f"{DB_CONFIG['host']}数据库连接关闭成功！")

