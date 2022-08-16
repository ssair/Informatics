N = 20
A =[True] * N
A[0] = A[1] = False
for k in range(2, N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False

for k in range(N):
    print(k, "-", "простое" if A[k] else "составное")

# https://habr.com/ru/post/133037/?ysclid=l6w48od35g544340977