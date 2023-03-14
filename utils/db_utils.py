import pymysql


class MySQLUtils:
    # 初始化的时候建立链接
    def __init__(self,host, prot, user, password, db):
        self.cur = None
        self.conn = None
        self.conn = pymysql.Connect(host=host, port=prot, user=user, password=password, db=db)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    # # # 创建数据库链接
    # def get_cur(self, host, prot, user, password, db):
    #     self.conn = pymysql.Connect(host=host, port=prot, user=user, password=password, db=db)
    #     self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    # 数据库查询
    def query_data(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        for item in result:
            print(item)
        return item

    # 修改
    def change_dat(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()  # 修改之前必须提交
        except Exception:
            self.conn.rollback()  # 事务回滚，多条数据，一条失败，回滚

    # 关闭链接
    def close(self):
        self.cur.close()
        print("游标关闭成功")
        self.conn.close()
        print("数据库链接关闭成功")


if __name__ == '__main__':
    Db = MySQLUtils('115.28.108.130', 3306, 'test', '123456', 'newecshop')
    # Db.get_cur('115.28.108.130', 3306, 'test', '123456', 'newecshop')
    Db.query_data("select * from ecs_goods where goods_name = 'Dell电脑';")
    Db.query_data("select * from ecs_goods limit 1;")
    Db.close()
