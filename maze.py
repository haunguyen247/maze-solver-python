import csv, os, sys, random, time

def get_maze(file):
    with open(file, 'r') as read:
        reader = csv.reader(read)
        maze = []
        for line in reader:
            maze.append(line)
    return maze

def display_maze(m, path):
    m2 = m.copy()
    os.system('clear')

    for step in path:
        maze[step[0]][step[1]] = "."
    m2[path[-1][0]][path[-1][1]] = "M"

    draw = ""
    for row in m2:
        for item in row:
            item = str(item).replace('1','█')
            item = str(item).replace('0',' ')
            item = str(item).replace('2',' ')
            draw += item
        draw += '\n'
    print(draw)


def move(path):
    time.sleep(0.3)
    curr = path[-1]
    display_maze(maze, path)
    
    next_steps = [(curr[0], curr[1] + 1), (curr[0], curr[1] - 1), (curr[0] + 1, curr[1]), (curr[0] - 1, curr[1])]
    random.shuffle(next_steps)

    for next_step in next_steps:
        x, y = next_step[0], next_step[1]
        if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
            continue
        elif maze[x][y] in ["1", "2"]:
            continue
        elif next_step in path:
            continue

        elif maze[x][y] == "B":
            path = path + (next_step, )
            display_maze(maze, path)
            print("solution found!\n")
            
            sys.exit()

        else:   
            new_path = path + (next_step, )
            move(new_path)
            maze[x][y] = "2"
            display_maze(maze, path)
            time.sleep(0.3)

maze = get_maze("maze.csv")

move(((1,0), ))


   
