def simple_list(n: int):
    """
    Выводит список чисел до N с параметром - простое или составное
    """
    A =[True] * n
    A[0] = A[1] = False
    for k in range(2, n):
        if A[k]:
            for m in range(2*k, n, k):
                A[m] = False

    for k in range(n):
        print(k, "-", "простое" if A[k] else "составное")


simple_list(20)

# https://habr.com/ru/post/133037/?ysclid=l6w48od35g544340977