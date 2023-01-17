class Math:
    
    # 정적 매서드(static method)
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def sub(x, y):
        return x - y
    
print(Math.add(3, 4))
print(Math.sub(3, 4))

