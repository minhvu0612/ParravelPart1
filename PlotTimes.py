import Factorial as Fact
import Parravel as Par

import matplotlib.pyplot as plt
import numpy as np
import time

from math import factorial # Python dùng cái này

# Lưu tg chạy của các P2
listfunc1 = [] 
listfunc2 = []
listfunc3 = []
listfunc4 = []

def PlotTimeExecute(n, listfunc1, listfunc2, listfunc3, listfunc4):
    loop = 1
    while loop <= 5:
        # Thời gian tính có đệ quy khoảng d
        start_time = time.time()
        x = Fact.FactCaculation(n, int(n/1000) + 1)
        listfunc1.append(Fact.ExecuteTime(start_time))

        # Thời gian tính lặp
        start_time = time.time()
        x = Fact.Fact(n)
        listfunc2.append(Fact.ExecuteTime(start_time))

        # Thời gian tính theo thuật toán song song
        start_time = time.time()
        x = ParravelFactorial(n)
        listfunc3.append(Fact.ExecuteTime(start_time))

        # Thời gian tính theo thư viện Python
        start_time = time.time()
        x = factorial(n)
        listfunc4.append(Fact.ExecuteTime(start_time))

        # Tăng loop
        loop += 1
        n = n * 2

    plt.plot([1, 2, 3, 4, 5], listfunc1, color = "green", label = "Recursion d")
    plt.plot([1, 2, 3, 4, 5], listfunc2, color = "blue", label = "Normal")
    plt.plot([1, 2, 3, 4, 5], listfunc3, color = "yellow", label = "Parravel")
    plt.plot([1, 2, 3, 4, 5], listfunc4, color = "red", label = "Lib Using")
    plt.ylabel('times')
    plt.legend(loc = "best")
    plt.savefig('times2000.png')

if __name__ == "__main__":
    PlotTimeExecute(2000, listfunc1, listfunc2, listfunc3, listfunc4)
