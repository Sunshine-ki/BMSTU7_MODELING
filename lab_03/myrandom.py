# Класс, реализующий простой рандомайзер
# Для генерации случайных чисел используется Линейный конгруэнтный метод 


# Таблица хороших констант для линейных конгруэнтных генераторов
# a       c      m
# 4096	150889	714025
# 36261	66037	312500
# 84589	45989	217728

# 1664525 1013904223 2^32
# 22695477 1 2^32
# 1103515245 12345 2^31 

class MyRandom:
    def __init__(self):
        self.current = 10
        self.m = 312500
        self.a = 36261
        self.c = 66037

    def get_number(self, low=0, high=100):
        self.current = (self.a * self.current + self.c) % self.m
        result = int(low + self.current % (high - low))
        return result
