from time import sleep
import webbrowser
import ctypes

####################################################################
                    # MADE BY ÖSI ASSI #
####################################################################

# consolename
titel = "TikTok Follower FAKE Generator!"
ctypes.windll.kernel32.SetConsoleTitleW(titel)

# ad <3
webbrowser.open("https://linktr.ee/oesi_assi")

####################################################################
                        # MAIN #
####################################################################

# username
name = input("Enter the username: ")
print("")

# follower
fol = int(input("How many followers should be generated: "))
    
# Fake generator
for i in range(3):
    print("...")
    sleep(1)

for i in range(fol):
    print(" user%d" % (1+i))
    if i == fol/2-1:
        for x in range(3):
            print("...")
            sleep(1)

# open tiktok
print(" %d (Fake)users were added to the account: %s" % (fol, name))
sleep(2)
webbrowser.open("https://www.tiktok.com/@%s" % name)
sleep(4)
webbrowser.open("https://youtu.be/dQw4w9WgXcQ")

# end
print("")
input("Press Enter to close the window.")