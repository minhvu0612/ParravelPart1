from multiprocessing import pool as pl
import Factorial as Fact

divide = 500

'''
Đa xử lý : 1 luồng => nhiều luồng


N => []
'''

# Chia số thành các khoảng xử lý nhỏ hơn
def ParravelDivide(n):
    list = []
    for i in range(1, n, int(n/divide) + 1):
        list.append(i)
    list.append(n)
    new_list = []
    for i in range(len(list) - 1):
        new_list.append([list[i + 1] - 1, list[i]])
    return new_list

# Chia thành các luồng xử lý song song
def ParravelFactorial(n):
    list = ParravelDivide(n)
    with ThreadPool() as pool:
        results = pool.map(Fact.Multiplication, list)
    result = 1
    for i in results:
        result *= i
    return result
'''
pc1 => a
pc2 => b
pc3 => c

rs = a.b.c.n'''