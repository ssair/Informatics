from random import uniform

def estimate_pi(n):
    num_point_circle = 0 #кол-во точек внутри круга
    num_point_total = n

    for i in range(n):
        x = uniform(0,1)
        y = uniform(0,1)
        distance = x**2 + y**2

        if distance <= 1: #определяем, что точка попала внутрь круга
            num_point_circle += 1

    return 4 * num_point_circle/num_point_total


n = 10000000 #общее количество точек (чем больше точек, тем лучше точность)
pi = estimate_pi(n)

print(pi)