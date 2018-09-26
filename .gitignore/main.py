import os
text_file = open("snakeLevel.txt", "w");
text_file.write("0")
text_file.close();
os.system("pycurses.py")