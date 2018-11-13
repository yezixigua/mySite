from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import time

Base = declarative_base()


# 保存ip的对象类型， 映射一个数据表
class Visitor(Base):
    __tablename__ = 'Visitor'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    time = Column('time', String(50))
    ip = Column('ip', String(50))


# 暂时这样放着吧，还没啥用
class Role(Base):
    __tablename__ = 'Role'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50))


# 连接数据库的一些变量， 会需要全局引用
# print(os.getcwd())
DB_CONNECT_STRING = 'sqlite:///db/test3.db'
engine = create_engine(DB_CONNECT_STRING, echo=False)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()


def init_data():
    # 1. 创建表（如果表已经存在，则不会创建）
    Base.metadata.create_all(engine)


def add_data(data_ip):
    # 2. 插入数据
    session1 = DB_Session()
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    u = Visitor(time=localtime, ip=data_ip)
    session1.add(u)
    session1.commit()
    session1.close()



def add_data_demo():
    # 2. 插入数据
    u = Visitor(time='tobi', ip='wdtf')
    u1 = Visitor(time='tobi', ip='wdtf')
    u2 = Visitor(time='tobi', ip='wdtf')
    r = Role(name='user')
    # 2.1 使用add，如果已经存在，会报错
    session.add(u)
    session.add(u1)
    session.add(u2)
    session.add(r)
    session.commit()
    print(r.id)


#
# # 3 修改数据
# # 3.1 使用merge方法，如果存在则修改，如果不存在则插入（只判断主键，不判断unique列）
# r.name = 'admin'
# session.merge(r)
#

def update_data(id_data, ip='0.0.0.0'):
    # 3.2 也可以通过这种方式修改
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    session.query(Visitor).filter(Visitor.id == id_data).update({'ip': ip, 'time': localtime})


def delete_data(id_data):
    # 4. 删除数据
    session.query(Role).filter(Role.id == id_data).delete()


def query_data(id):
    # 5. 查询数据
    # 5.1 返回结果集的第二项
    user = session.query(Visitor).get(id)
    print(user.id, user.time, user.ip)


def query_all():
    # 5. 查询数据
    users = session.query(Visitor)[:]
    for user in users:
        print(user.id, user.time, user.ip)

#
# # 5.3 查询条件
# user = session.query(User).filter(User.id < 6).first()
#
# # 5.4 排序
# users = session.query(User).order_by(User.name)
#
# # 5.5 降序（需要导入desc方法）
# from sqlalchemy import desc
# users = session.query(User).order_by(desc(User.name))
#
# # 5.6 只查询部分属性
# users = session.query(User.name).order_by(desc(User.name))
# for user in users:
#     print user.name
#
# # 5.7 给结果集的列取别名
# users = session.query(User.name.label('user_name')).all()
# for user in users:
#     print user.user_name
#
# # 5.8 去重查询（需要导入distinct方法）
# from sqlalchemy import distinct
# users = session.query(distinct(User.name).label('name')).all()
#
# # 5.9 统计查询
# user_count = session.query(User.name).order_by(User.name).count()
# age_avg = session.query(func.avg(User.age)).first()
# age_sum = session.query(func.sum(User.age)).first()
#
# # 5.10 分组查询
# users = session.query(func.count(User.name).label('count'), User.age).group_by(User.age)
# for user in users:
#     print 'age:{0}, count:{1}'.format(user.age, user.count)
#
# # 6.1 exists查询(不存在则为~exists())
# from sqlalchemy.sql import exists
# session.query(User.name).filter(~exists().where(User.role_id == Role.id))
# # SELECT name AS users_name FROM users WHERE NOT EXISTS (SELECT * FROM roles WHERE users.role_id = roles.id)
#
# # 6.2 除了exists，any也可以表示EXISTS
# session.query(Role).filter(Role.users.any())
#
# # 7 random
# from sqlalchemy.sql.functions import random
# user = session.query(User).order_by(random()).first()


def test():
    init_data()
    query_all()
    add_data('1.1.1.1')
    query_all()


if __name__ == '__main__':
    test()
    session.close()

