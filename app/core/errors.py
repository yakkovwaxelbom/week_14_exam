class MySQLAlreadyExist(Exception):
    def __init__(self, msg: str):
        self.msg = f'mysql server already exist: {msg}'
        super().__init__(self.msg)
        

class MySQLNotExist(Exception):
    def __init__(self, msg: str):
        self.msg = f'mysql server not exist: {msg}'
        super().__init__(self.msg)
        

class MySQLGeneralError(Exception):
    def __init__(self, msg: str):
        self.msg = f'error trying to interact to mysql server: {msg}'
        super().__init__(self.msg)


class SQLSchemaNotExist(FileNotFoundError):
    def __init__(self, msg: str):
        self.msg = f'sql schema not exist: {msg}'
        super().__init__(self.msg)
