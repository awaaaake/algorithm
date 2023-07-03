# class Fibonacci:
#     topDown_memo = []
#     bottomup_table = []

#     @staticmethod
#     def main():
#         n = 30
#         Fibonacci.topDown_memo = [0] * (n + 1)
#         Fibonacci.bottomup_table = [0] * (n + 1)

#         import time
#         start_time = time.time()
#         print(Fibonacci.naiveRecursion(n))
#         end_time = time.time()
#         print("일반 재귀 소요 시간:", end_time - start_time)

#         print()

#         start_time = time.time()
#         print(Fibonacci.topDown(n))
#         end_time = time.time()
#         print("Top-Down DP 소요 시간:", end_time - start_time)

#         print()

#         start_time = time.time()
#         print(Fibonacci.bottomUp(n))
#         end_time = time.time()
#         print("Bottom-Up DP 소요 시간:", end_time - start_time)

#     @staticmethod
#     def naiveRecursion(n):
#         if n <= 1:
#             return n
#         return Fibonacci.naiveRecursion(n - 1) + Fibonacci.naiveRecursion(n - 2)

#     @staticmethod
#     def topDown(n):
#         if n < 2:
#             return Fibonacci.topDown_memo[n] = n
#         if Fibonacci.topDown_memo[n] > 0:
#             return Fibonacci.topDown_memo[n]
#         Fibonacci.topDown_memo[n] = Fibonacci.topDown(n - 1) + Fibonacci.topDown(n - 2)
#         return Fibonacci.topDown_memo[n]

#     @staticmethod
#     def bottomUp(n):
#         Fibonacci.bottomup_table[0] = 0
#         Fibonacci.bottomup_table[1] = 1
#         for i in range(2, n + 1):
#             Fibonacci.bottomup_table[i] = Fibonacci.bottomup_table[i - 1] + Fibonacci.bottomup_table[i - 2]
#         return Fibonacci.bottomup_table[n]


# if __name__ == '__main__':
#     Fibonacci.main()

# """
# 결과
# 832040
# 일반 재귀 소요 시간: 0.009

# 832040
# Top-Down DP 소요 시간: 0.0

# 832040
# Bottom-Up DP 소요 시간: 0.0
# """
