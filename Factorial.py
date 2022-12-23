import time

# Thuật toán tính giai thừa - Phương pháp đệ quy
def FactRecursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * FactRecursive(n - 1)
'''
n! = 1.2.3...n
0! = 1
1! = 1

FactRecursive(10) => 10 * FactRecursive(9) => 10 * 9 * FactRecursive(8) => 10.9.8...1'''

# Tính tích của khoảng từ k đến n
def Multiplication(list): # [n, k] => n là chặn trên, k chặn dưới
    result = list[1] = 1
    for i in range(list[1] + 1, list[0] + 1):
        result = result * i
    return result


# Thuật toán tính giai thừa - Đệ quy khoảng d = n - k
def FactCaculation(n, k):
    if n <= 0 or n == 1:
        return 1
    if n >= k:
        return Multiplication([n, k]) * FactCaculation(k - 1, k)
    if n < k:
        return n * FactCaculation(n - 1, k)
'''
10 => [1, 5, 10] => [1, [1, 4], [5, 9], 10]

rs = 1
rs = rs * Multiplication([4, 1]) => list[1] = 1, list[0] = 4 => range(2, 5) = [2,3,4] = 1.2.3.4
rs = rs * Multiplication([9, 5]) => rs * 5.6.7.8.9
rs = rs * 10 = 1.2.3.4.5.6.7.8.9.10

n = 7 k =10 => 6,10 => 5,10 => 4,10 => ... => 1.2.3.4.5.6.7'''

# Thuật toán lặp
def Fact(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result
'''
10 = Fact(10) = 1.2...10'''

# Hàm tính thời gian chạy của chương trình
def ExecuteTime(start_time):
    return time.time() - start_time
''' time.time() là tg hiện tai'''