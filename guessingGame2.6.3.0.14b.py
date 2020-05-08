import random
import sys
import math
from datetime import datetime

# seed value
random.seed(datetime.now())
# Max value
MAX = (2**53)-1

# Returns 1 if the guess is too high
# 0 If the guess is correct
# -1 If the guess is too low
def guessCheck(guess, num):
    if guess > num:
        return 1
    elif guess < num:
        return -1
    else:
        return 0

# Binary search
def search():
    count = 0
    high = MAX -1
    low = 0
    while low <= high:
        guess = math.floor((low+high)/2)
        response = guessCheck(guess, num)
        if response == -1:
            low = guess + 1
            count+=1
        elif response == 1:
            count+=1
            high = guess - 1
        else:
            print("\n\nBinary Search")
            print(f"Found the number ({num}) in {count} guesses. Last guess:{guess}")
            return guess

# Create a range, and pick a random number from within it
L = random.randint(1, MAX-1) # Low end of range
H = random.randint(L + 1, MAX) # High end of range
num = random.randint(L, H) # The actual random number to look for

print(f"Looking for {num}")
search()

"""
 _____                     _   _     _                 _          _                                   
|  ___|                   | | | |   (_)               | |        | |                                  
| |____   _____ _ __ _   _| |_| |__  _ _ __   __ _    | |__   ___| | _____      __     ___ __ _ _ __  
|  __\ \ / / _ \ '__| | | | __| '_ \| | '_ \ / _` |   | '_ \ / _ \ |/ _ \ \ /\ / /    / __/ _` | '_ \ 
| |___\ V /  __/ |  | |_| | |_| | | | | | | | (_| |   | |_) |  __/ | (_) \ V  V /    | (_| (_| | | | |
\____/ \_/ \___|_|   \__, |\__|_| |_|_|_| |_|\__, |   |_.__/ \___|_|\___/ \_/\_/      \___\__,_|_| |_|
                      __/ |                   __/ |                                                   
                     |___/                   |___/                                                    
 _                                                       _           _                 _              
| |                                                     | |         | |               | |             
| |__   ___      ___ ___  _ __ ___  _ __ ___   ___ _ __ | |_ ___  __| |     ___  _   _| |_            
| '_ \ / _ \    / __/ _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \| __/ _ \/ _` |    / _ \| | | | __|           
| |_) |  __/   | (_| (_) | | | | | | | | | | |  __/ | | | ||  __/ (_| |   | (_) | |_| | |_            
|_.__/ \___|    \___\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__\___|\__,_|    \___/ \__,_|\__|  
"""

# Always guess max so I can cut down 50% of the set of possibilities
# everytime it's higher
guess = MAX

# try the first guess
response = guessCheck(guess, num)
count = 0 # debugging

"""
 $$$$$$\                                      $$\                  $$$$$$\                  $$\           
$$  __$$\                                     $$ |                $$  __$$\                 $$ |          
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$ |$$\   $$\       $$ /  \__| $$$$$$\   $$$$$$$ | $$$$$$\  
\$$$$$$\  $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$ |$$ |  $$ |      $$ |      $$  __$$\ $$  __$$ |$$  __$$\ 
 \____$$\ $$ /  $$ |$$$$$$$$ |$$$$$$$$ |$$ /  $$ |$$ |  $$ |      $$ |      $$ /  $$ |$$ /  $$ |$$$$$$$$ |
$$\   $$ |$$ |  $$ |$$   ____|$$   ____|$$ |  $$ |$$ |  $$ |      $$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|
\$$$$$$  |$$$$$$$  |\$$$$$$$\ \$$$$$$$\ \$$$$$$$ |\$$$$$$$ |      \$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$\ 
 \______/ $$  ____/  \_______| \_______| \_______| \____$$ |       \______/  \______/  \_______| \_______|
          $$ |                                    $$\   $$ |                                              
          $$ |                                    \$$$$$$  |                                              
          \__|                                     \______/  
"""
while response != 0:
    if response == 1:
        lastHigh = guess
        guess = math.floor(guess/2)

    elif response == -1:
        guess = math.floor((guess + lastHigh)/2)
    
    count+=1
    response = guessCheck(guess, num)

# debugging
print("====================\nOriginal Alg")
print(f"Found the number ({num}) in {count} guesses. Last guess:{guess}")


"""
$$$$$$$\            $$\                                  $$$$$$\                  $$\           
$$  __$$\           $$ |                                $$  __$$\                 $$ |          
$$ |  $$ | $$$$$$\  $$$$$$$\  $$\   $$\  $$$$$$\        $$ /  \__| $$$$$$\   $$$$$$$ | $$$$$$\  
$$ |  $$ |$$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\       $$ |      $$  __$$\ $$  __$$ |$$  __$$\ 
$$ |  $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |      $$ |      $$ /  $$ |$$ /  $$ |$$$$$$$$ |
$$ |  $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|
$$$$$$$  |\$$$$$$$\ $$$$$$$  |\$$$$$$  |\$$$$$$$ |      \$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$\ 
\_______/  \_______|\_______/  \______/  \____$$ |       \______/  \______/  \_______| \_______|
                                        $$\   $$ |                                              
                                        \$$$$$$  |                                              
                                         \______/    
"""
# with open("test.txt","w+") as f:        #debugging
#     f.write(f"number to find: {num}\n")
#     while response != 0:
#         if response == 1:
#             lastHigh = guess
#             guess = math.floor(guess/2)
#             # print(guess)

#         elif response == -1:
#             guess = math.floor((guess + lastHigh)/2)
#             # print(guess)
#         count+=1

#         #debugging stuff
#         diff = num - guess
#         f.write(f"{diff}   guess {guess}     last high: {lastHigh}")
#         f.write("\n")

#         response = guessCheck(guess, num)
# # debugging
# print(f"Found the number ({num}) in {count} guesses. Last guess:{guess}")







