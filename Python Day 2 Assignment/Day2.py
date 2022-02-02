lottery = "hello coders"
#winner codes: e c d s
print('Enter any letter from "',lottery,'"to win the lottery: ')
win = input("").lower()
if win == lottery[1] or win == lottery[6] or win == lottery[8] or win == lottery[11]:
    print('Congratulations, You have Won the lottery')
else:
    print('Oops Sorry, You have loose the lottery')