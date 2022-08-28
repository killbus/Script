from copy import deepcopy
import pymysql


class SQLHelper:
    def __init__(self, database, host="localhost", user="root", password="root") -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db = pymysql.connect(
            host=self.host, user=self.user, passwd=self.password, database=self.database)
        self.init()

    def close(self):
        try:
            self.db.close()
        except:
            pass

    def init(self):
        """
        重置条件变量;
        """
        self.table = None
        self.wheres = None
        self.fields = None
        self.orders = None
        self.limit = None
        self.offset = None
        self.values = None

    def join(self, code, ds: list):
        if(not ds):
            return ""
        res = ""
        for d in ds:
            if(res):
                res += f"{code}{d}"
            else:
                res += f"{d}"
        return res

    def setDB(self, db: str):
        """
        (可选)设置数据库,不设置则使用上次操作的数据库;
        """
        self.db.select_db(db)
        return self

    def setTable(self, table: str):
        """
        (必选)设置要操作的表;
        """
        self.table = table
        return self

    def setFields(self, fields: list):
        """
        (可选)设置insert、query或update字段,对于insert不设置则默认选择全部字段;
        """
        self.fields = list(fields)
        return self

    def setValues(self, values: list):
        """
        (必选)设置insert或update字段的值;
        """
        self.values = list(values)
        # 字符串类型值用''包括
        for i in range(len(self.values)):
            if(isinstance(self.values[i], str)):
                self.values[i] = f"'{self.values[i]}'"
        return self

    def setObj(self, obj: dict):
        """
        (可选)设置insert或update的对象;
        """
        self.setFields(obj.keys())
        self.setValues(obj.values())
        return self

    def setWheres(self, wheres: list):
        """
        (可选)设置update或query的条件;
        """
        # 多层对象必须需要深拷贝
        self.wheres = deepcopy(wheres)
        for i in range(len(self.wheres)):
            # kv默认用=号连接
            if(len(self.wheres[i]) == 2):
                self.wheres[i].insert(1, "=")
            # 字符串类型值用''包括
            if(len(self.wheres[i]) == 3 and isinstance(self.wheres[i][2], str)):
                self.wheres[i][2] = f"'{self.wheres[i][2]}'"
        return self

    def setLimit(self, limit: int):
        """
        (可选)设置query的数量;
        """
        self.limit = limit
        return self

    def setOffset(self, offset: int):
        """
        (可选)设置query的偏移量;
        """
        self.offset = offset
        return self

    def setOrders(self, orders: list):
        """
        (可选)设置query排序字段和排序方式(默认升序);
        """
        self.orders = deepcopy(orders)
        return self

    def builderSet(self) -> str:
        """
        构建SET子句
        """
        if(self.fields == None or self.values == None or len(self.fields) != len(self.values)):
            return None
        kvs = []
        for i in range(len(self.fields)):
            field = self.fields[i]
            value = self.values[i]
            kvs.append(f"{field} = {value}")
        return f"SET {self.join(',',kvs)} "

    def buildWhere(self) -> str:
        """
        构建WHERE子句;
        """
        if(self.wheres == None):
            return None
        isConnect = False
        ws = []
        for where in self.wheres:
            if(len(where) == 1):
                ws.append(where)
            else:
                # 默认AND连接条件
                if(isConnect):
                    ws.append("AND")
                ws.append(f"{where[0]} {where[1]} {where[2]}")
            isConnect = not isConnect
        return f"WHERE {self.join(' ',ws)} "

    def buildOrders(self) -> str:
        """
        构建ORDER BY子句
        """
        if(self.orders == None):
            return None
        ods = []
        for order in self.orders:
            # 默认升序
            if(isinstance(order, str)):
                ods.append(f"{order} ASC")
            # 自定义排序
            else:
                ods.append(f"{order[0]} {order[1]}")
        return f"ORDER BY {self.join(',',ods)} "

    def buildUpdate(self) -> str:
        """
        构建UPDATE语句;
        """
        if(self.table == None):
            return None
        sql = f"UPDATE {self.table} "
        setW = self.builderSet()
        if(setW == None):
            return None
        sql += setW
        where = self.buildWhere()
        if(where == None):
            return None
        sql += where
        return sql

    def buildInsert(self) -> str:
        """
        构建SELECT语句;
        """
        if(self.table == None):
            return None
        sql = f"INSERT INTO {self.table}({self.join(',',self.fields)}) VALUES({self.join(',',self.values)})"
        return sql

    def buildDelete(self) -> str:
        """
        构建DELETE语句,不允许没有where条件
        """
        if(self.table == None):
            return None
        where = self.buildWhere()
        if(not where):
            return None
        sql = f"DELETE FROM {self.table} {where}"
        return sql

    def buildQuery(self) -> str:
        """
        构建SELECT语句;
        """
        # 初步判断
        if(self.table == None):
            return None
        # 查询语句
        sql = "SELECT "
        # 选择字段
        if(self.fields != None):
            sql += f"{self.join(',',self.fields)} "
        else:
            sql += "* "
        # 选择表
        sql += f"FROM {self.table} "
        # 选择条件
        where = self.buildWhere()
        if(where):
            sql += where
        # 选择排序
        orders = self.buildOrders()
        if(orders):
            sql += orders
        # 选择数量限制
        if(self.limit != None):
            sql += f"LIMIT {self.limit} "
        # 选择偏移
        if(self.offset != None):
            sql += f"OFFSET {self.offset} "
        return sql

    def update(self) -> bool:
        """
        执行update操作,不允许没有where条件
        """
        sql = self.buildUpdate()
        self.init()
        cursor = self.execute(sql)
        if(cursor != None):
            return True
        else:
            return False

    def insert(self) -> bool:
        """
        执行insert操作;
        """
        sql = self.buildInsert()
        self.init()
        cursor = self.execute(sql)
        if(cursor != None):
            return True
        else:
            return False

    def delete(self) -> bool:
        """
        执行delete操作;
        """
        sql = self.buildDelete()
        self.init()
        cursor = self.execute(sql)
        if(cursor != None):
            return True
        else:
            return False

    def query(self) -> tuple:
        """
        执行query操作;
        """
        sql = self.buildQuery()
        self.init()
        cursor = self.execute(sql)
        if(cursor != None):
            return cursor.fetchall()
        else:
            return None

    def execute(self, sql: str):
        """
        执行SQL语句;
        """
        if(not sql):
            return None
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
            return cursor
        except Exception as e:
            print(str(e))
            return None


if __name__ == "__main__":
    db = SQLHelper("source")
    wheres = [["ip", "=", 1], ['port', "=", 2]]
    # # 插入-字典形式
    # proxy = {"ip": "127.0.0.1", "port": 10002}
    # db.setTable("proxies").setObj(proxy).insert()

    # # 插入-普通形式
    # fileds = ["ip", "port"]
    # values = ["127.0.0.1", 10002]
    # db.setTable("proxies").setFields(fileds).setValues(values).insert()

    # # 更新-字典形式
    # proxy = {"ip": "127.0.0.1", "port": 8080}
    # wheres = [['ip', "=", "127.0.0.1"]]
    # db.setTable("proxies").setObj(proxy).setWheres(wheres).update()

    # # 更新-普通形式
    # fileds = ["ip", "port"]
    # values = ["127.0.0.1", 8080]
    # wheres = [['ip', "=", "127.0.0.1"]]
    # db.setTable("proxies").setFields(fileds).setValues(
    #     values).setWheres(wheres).update()

    # # 查询
    # orders = ["ip", ("port", "DESC")]
    # wheres = [["port", ">", 1000]]
    # proxies = db.setTable("proxies").query()
    # proxies = db.setTable("proxies").setLimit(10).query()
    # proxies = db.setTable("proxies").setOrders(
    #     orders).setWheres(wheres).query()

    # # 复杂SQL语句，可以直接调用execute()
    # cursor = db.setTable("proxies").execute("your sql")
