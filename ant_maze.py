maze = [[0] for k in range(10)]

a = 1
finish = 0

for i in range(0,10):
    maze[i] = list(map(int,input(":").split()))
    a -= 1

    while True:
        if maze[i][a] == 1:
            a += 1
        elif maze[i][a] == 0:
            maze[i][a] = 9
            a += 1
            if maze[i][a] == 1:
                break
        elif maze[i][a] == 2:
            maze[i][a] = 9
            for k in range(i+1,10):
                maze[k] = list(map(int,input(":").split()))
                finish = 1
            break
        if a == 10:
            a = 1
            break

    if finish == 1:
        break

print(maze)
