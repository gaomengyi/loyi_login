class Do_Data:
    def __init__(self):
        self.value = {}

    def has(self, key: str):
        # 判断是否有key值，布尔类型
        return bool(self.value.get(key))

    def find(self, key: str):
        # 获取key值，没有返回None
        return self.value.get(key)

    def get_token(self, token):
        return self.value.get(token)
