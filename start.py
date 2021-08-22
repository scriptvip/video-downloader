import os
os.system("clear")
def banner ():
    print(" _     _   _   _____   _____   _____       ")
    print("| |   / / | | |  _  \ | ____| /  _  \      ")
    print("| |  / /  | | | | | | | |__   | | | |      ")
    print("| | / /   | | | | | | |  __|  | | | |      ")
    print("| |/ /    | | | |_| | | |___  | |_| |      ")
    print("|___/     |_| |_____/ |_____| \_____/      ")
    print("            Abdo sleem (*__^) ")
    print (" ")
    
banner()
print ("  |-----------------|")
print ("  |  [1] YouTube    |")
print ("  |-----------------|")
print ("  |  [2] Facebook   |")
print ("  |-----------------|")
print(" ")
print (" ")
cho = int(input ("    what your choice ==> "))
if cho == 1 :
    os.system("clear")
    
    banner()
    print(" ")
    print("   |----------------------------------|")
    print("   |  [1] download highest_resolution |")
    print("   |----------------------------------|")
    print("   |  [2] download 720_resolution     |")
    print("   |----------------------------------|")
    print("   |  [3] download 480_resolution     | ")
    print("   |----------------------------------| ")
    print("   |  [4] download 360_resolution     | ")
    print("   |----------------------------------| ")
    print("   |  [5] download lowest_resolution  | ")
    print("   |----------------------------------| ")
    print("  ")
    ch = int(input (" what's your choice ( 1,2,3,4,5 ) ==> "))
    print(" ")
    if ch == 1:
        #os.system("clear")
        os.system("python3 youtube_h.py")
    if ch == 2:
        #os.system("clear")
        os.system("python3 youtube_7.py")
    if ch == 3:
        #os.system("clear")
        os.system("python3 youtube_4.py")
    if ch == 4:
        #os.system("clear") 
        os.system("python3 youtube_3.py")   
    if ch == 5:
        #os.system("clear")
        os.system("python3 youtube_l.py")
if cho == 2 :
    os.system("clear")
    os.system("python3 facebook.py")

else :
    os.system("python3 start.py")