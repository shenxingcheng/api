import pymysql

conn = pymysql.Connect(host='115.28.108.130',
                       port=3306,
                       user='test',
                       password='123456',
                       db='newecshop'

                       )
# conn.select_db('newecshop')
# cur = conn.close() # 普通游标 [(1.'zhangsan'),(2,lisi)]
cur = conn.cursor(pymysql.cursors.DictCursor)  # 字典游标[{‘id’:1,'name':'zhangsan'},{'id':2,'name':'lisi'}]
cur.execute('select * from ecs_goods where goods_name = "Dell电脑"')
# cur.fetchone()  # 取一条结果
# cur.fetchmany(3)  # 取三条结果
result = cur.fetchall()  # 取所有结果
# for item in result:
#     print(item)
# print('姓名',item['name'])

# 修改操作
cur.execute('delete from ecs_goods where goods_id =302;')
conn.commit()  # 修改必须添加操作才能生效
# 修改之后查询是否修改成功
# cur.execute('select  * from ecs_goods where googs_id =302;')
# print(cur.fetchone())

cur.close()
conn.close()