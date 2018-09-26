import sys,os
import curses

def levelPass():
    arr = []
    inp = open("snakePass.txt","r")
    #read line into array 
    for line in inp.readlines():
        # loop over the elemets, split by whitespace
        if line == "false":
            return False;
        else :
            return True;
def level():
    if levelPass() == True:
        arr = []
        inp = open("snakeLevel.txt","r")
        #read line into array 
        for line in inp.readlines():
            # loop over the elemets, split by whitespace
            for i in line.split():
                # convert to integer and append to the list
                arr.append(int(i))
                level = int(i)
                inp.close();
        level += 1;
        text_file = open("snakeLevel.txt", "w");
        text_file.write("%s" %level);
        text_file.close();
        phrase = "-------------------------------- Next level: %s --------------------------------"%level;
        return phrase;
    else:
        text_file = open("snakeLevel.txt", "w");
        text_file.write("1")
        text_file.close();
        phrase = "-------------------------------- Next level: 1 --------------------------------";
        return phrase;

def readRecord():
    arr = []
    inp = open("SnakeRecord.txt","r")
    #read line into array 
    for line in inp.readlines():
        # loop over the elemets, split by whitespace
        for i in line.split():
            # convert to integer and append to the list
            arr.append(int(i))
            inp.close()
    return arr
def readPoints():
    arr = []
    inp = open("SnakeScoreboard.txt","r")
    #read line into array 
    for line in inp.readlines():
        # loop over the elemets, split by whitespace
        for i in line.split():
            # convert to integer and append to the list
            arr.append(int(i))
            inp.close()
    return arr;
def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            import snake
        elif k == curses.KEY_UP:
            import snake
        elif k == curses.KEY_RIGHT:
            import snake
        elif k == curses.KEY_LEFT:
            import snake
        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        record = readRecord();
        points = readPoints();
        phrase = level();
        keystr = "{}".format(phrase)[:width-1];
        title = "Latest score: {}".format(points)[:width-1]
        subtitle = "Current Record: {}".format(record)[:width-1]
        statusbarstr = "Press 'arrows' to START | Press 'q' to exit | ------------Thank you for playing!------------- by: Miguel de Vasconcelos"

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

        # Rendering some text
        whstr = "Map size | Width: {} , Height: {} |".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.move(cursor_y, cursor_x)
        stdscr.addstr(start_y + 5, start_x_keystr, keystr)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
