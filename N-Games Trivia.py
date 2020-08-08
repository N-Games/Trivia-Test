print('Hello, welcome to my Trivia!')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q= 4

if ans.lower() == 'yes': print('ok lets start shall we?')
ans = input('1. Is N-Games a furry?')
if ans.lower() == 'yes':
    score += 1
    print ('Correct')
else:
        print('Incorrect')
                               
ans = input('2. Does N-Games have a Discord server')
if ans.lower() == 'yes':
    score += 1
    print ('Correct')
else:
        print('Incorrect')

ans = input('3. Does N-Games have friends?')
if ans.lower() == 'yes':
    score += 1
    print ('Correct')
else:
        print('Incorrect')

ans = input('4. Is N-Games good in coding??')
if ans.lower() == 'no':
    score += 1
    print ('Correct')
else:
        print('Incorrect')

print('Thank you for playing')
mark =(score/total_q * 100)

print("Mark: ", str(mark) + '%')
print('check code here:')
