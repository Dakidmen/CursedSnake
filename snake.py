import random;
import curses;
import os;

screen = curses.initscr()
weight, height = screen.getmaxyx();
curses.curs_set(0);
sh, sw = screen.getmaxyx();
w = curses.newwin(sh, sw, 0,0);
w.keypad(1);

def levelPass(what):
    text_file = open("snakePass.txt", "w");
    text_file.write(what)
    text_file.close();

def quitGame(score):
    record(score);
    scoreboard(score);
    curses.endwin();
    os.system("pycurses.py")
    quit();

def readLevel():
    arr = []
    inp = open("snakeLevel.txt","r")
    #read line into array 
    for line in inp.readlines():
        # loop over the elemets, split by whitespace
        for i in line.split():
            # convert to integer and append to the list
            arr.append(int(i))
            inp.close()
    level = arr;
    return level

def mode(level):
    if level == [1]:
        speed = 1;
        return speed;
    elif level == [2]:
        speed = 2;
        return speed;
    elif level == [3]:
        speed = 3;
        return speed;
    elif level == [4]:
        speed = 4;
        return speed;
w.timeout(1);

snk_x = sw/4;
snk_y = sh/2;

snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
];

#Starting food:
food = [sh//2, sw//2];
w.addch(food[0], food[1], 'O');


#Starting X:
global X_list;
X_list = [];

for i in range(4):

    X = [
        random.randint(1, sh-1),
        random.randint(1, sw-1)
    ];
    X_list.append(X);
    w.addch(X[0], X[1], 'X');

def add_X():

    #X = X if X not in snake else None;~
    new_X = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ];

    w.addch(new_X[0], new_X[1], 'X');

    X_list.append(new_X);


key = curses.KEY_RIGHT;

def myScore(points):
    points += 1
    points /= 0.33
    points = int(points)
    return points;

def record(finalScore):
    arr = []
    inp = open("SnakeScoreboard.txt","r")
    #read line into array 
    for line in inp.readlines():
        # loop over the elemets, split by whitespace
        for i in line.split():
            # convert to integer and append to the list
            arr.append(int(i))
            inp.close()
    for i in arr:
        if int(finalScore) >= int(i):
            text_file = open("SnakeRecord.txt", "w");
            text_file.write("%s" %finalScore);
            text_file.close();
                


def scoreboard(finalScore):
    text_file = open("SnakeScoreboard.txt", "w");
    text_file.write("%s"%finalScore)
    text_file.close();



score = 0;
foodCount = 0;

while True:
    next_key = w.getch();
    key = key if next_key == -1 else next_key;

    
    #if snake gets X:
    if snake[0] in X_list:
        levelPass("false");
        quitGame(score);
    

    #if snake loses:
    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        levelPass("false");
        quitGame(score);
    #level change:
    if foodCount == 6:
        levelPass("true");
        quitGame(score);
    #adding more body to snake:
    speed = mode(readLevel());
    new_head = [snake[0][0], snake[0][1]];
    #           x coord       y coord
    if key == curses.KEY_DOWN:
        new_head[0] += int(speed);
    if key == curses.KEY_UP:
        new_head[0] -= int(speed);
    if key == curses.KEY_LEFT:
        new_head[1] -= int(speed);
    if key == curses.KEY_RIGHT:
        new_head[1] += int(speed);
    
    snake.insert(0,new_head);

    #if snake gets food:
    if snake[0] == food:
        points = myScore(score);
        score += points;
        food = None;
        while food is None:
            foodCount += 1;
            new_food = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = new_food if new_food not in snake else None;
        w.addch(food[0], food[1], 'O');
        #adds 2 new X:
        add_X();
        
    

    else:
        tail = snake.pop();
        w.addch(int(tail[0]), int(tail[1]), ' ');
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD);
