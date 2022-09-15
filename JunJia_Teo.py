import time
import enchant
import random
import string

#Challenge 1
print('{:^100s}'.format('\033[1m'+"[CHALLENGE 1]"+'\033[0m'))
time.sleep(1)
print('{:^92s}'.format("**The Runner-Up**"))

time.sleep(2)
print("\nAMY: Hi, I'm AMY, your bot")
time.sleep(2)
print("AMY: First, we need a list of integers")
time.sleep(2)
print("\nIf you wish to key in the list by yourself, input "+'\033[1;31;47m 0 \033[0;0m')
time.sleep(1)
print("If you wish to get a random list of number, input "+'\033[1;31;47m 1 \033[0;0m')
time.sleep(1)

while True:
    time.sleep(1)
    n=input("Your decision: ")
    try:
        n=int(n)
        if n==0 or n==1: 
            break
        else:
            print("Plese enter 0 or 1 iONLY")
    except:
        print("Please enter 0 or 1 ONLY to make decision.")

if n==0:
    print("\nEnter numbers seperated by space")
    lis=list(map(int,input("Enter the numbers: ").strip().split()))

if n==1:
    print("\x1B[3m" + "\nGenerating integer list in progress......"+'\x1B[0m')
    lis=[]
    count=random.randint(1,100)
    no=random.randint(1,100)
    for i in range(0, count):
        num = random.randint(1,no)
        lis.append(num)
    time.sleep(3)
    print("Here's your list..")
    time.sleep(1)
    print(lis)

time.sleep(3)
print('\x1B[3m'+"\nFinding......"+'\x1B[0m')
lis.sort(reverse=True)
lis=list(dict.fromkeys(lis))
time.sleep(2)
print("The second largest number is ", lis[1])

time.sleep(5)
#CHALLENGE 2
print("\n\n")
print('{:^100s}'.format('\033[1m'+"[CHALLENGE 2]"+'\033[0m'))
time.sleep(1)
print('{:^92s}'.format("**Grade of the Finals**"))
time.sleep(2)
print("AMY: You will need to insert the marks for the five(5) questions in your Final Exam.")
time.sleep(2)
print("AMY: I will calculate your grade.")
time.sleep(2)
print("AMY: Oh yeah, remember the marks should be 0-100")
lis=[]
for i in range(1,6):
    print("\nMark",i)
        
    while True:
        mark=input()
        try:
            mark=int(mark)
            break
        except ValueError:
            time.sleep(1)
            print("Please enter an integer between 0 and 100.")
            
    while mark<0 or mark>100:
        print("["+i+"]")
        mark=input("Enter value between 0 and 100: ")
        
    lis.append(mark)
    if mark>89:
        grade='A'
    elif mark>79:
        grade='B'
    elif mark>69:
        grade='C'
    elif mark>59:
        grade='D'
    else:
        grade='F'
    print("AMY: Grade for question", i, "is ",grade)
time.sleep(1)
print('\033[1m'+"\nCalculating overall grade......"+'\033[0m')
overall=(sum(lis))/5
if overall>89:
    grade='A'
elif overall>79:
    grade='B'
elif overall>69:
    grade='C'
elif overall>59:
    grade='D'
else:
    grade='F'

time.sleep(2)
print("AMY: Your overall grade is ",grade)
print("AMY: Wish you all the best next time")


time.sleep(5)
#CHALLENGE 3
print("\n\n\n")
print('{:^100s}'.format('\033[1m'+"[CHALLENGE 3]"+'\033[0m'))
d=enchant.Dict("en_US")
char_list=list(string.ascii_lowercase)
time.sleep(1)
print('{:^92s}'.format("**Guess the Word**"))
time.sleep(1)
print("AMY: Let's start the word game.")
time.sleep(1)
print("AMY: First, I will provide a letter range and you need to guess the English word")
time.sleep(1)

rand_char=random.choice(string.ascii_lowercase)
index=char_list.index(rand_char)
chosen_list=list(char_list[index:index+5])

print("Please guess a word in the range: "+chosen_list[0]+"-"+chosen_list[len(chosen_list)-1])
word=str(input("Word: "))
word=word.lower()

if d.check(word)==True:
    for i in word:
        if i not in chosen_list:
            print("AMY: Sorry, the word exists but not in my range...")
            quit()
    print("AMY: Congratulations!! You win!")
else:
    print("AMY: It's not a word...")