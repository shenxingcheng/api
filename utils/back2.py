import pymysql


# 创建数据库链接
def db_conn(host, prot, user, password, db):
    conn = pymysql.Connect(host=host, port=prot, user=user, password=password, db=db)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    return cur


# 数据库查询
def query_data(cur, sql):
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        print(item)
    return item


# 修改
def change_dat(cur, sql, conn):
    try:
        cur.execute(sql)
        conn.commit() # 修改之前必须提交
    except Exception:
        conn.rollback()  # 事务回滚，多条数据，一条失败，回滚


# 关闭链接
def close(cur, conn):
    cur.close()
    conn.close()


if __name__ == '__main__':
    cur = db_conn('115.28.108.130', 3306, 'test', '123456', 'newecshop')
    # query_data(cur, "select * from ecs_goods where goods_name = 'Dell电脑';")
    query_data(cur, "select * from ecs_goods limit 1;")
