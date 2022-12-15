file = open("test.txt", "w")
file.write("hello world")
file.close()

with open("test.txt", "w") as file:
    file.write("hello world")

lines = ["first", "second", "third"]
with open("test.txt", "w") as file:
    for line in lines:
        file.write(line + '\n')

with open("test.txt", "r") as file:
    for line in file:
        print(line)

file = open("test.txt", "r")
a = file.readlines()
file.close()
print(a)


a[0] = a[0][:-1]
print(a[0])
if 'first' in a:
    print('Jr')
