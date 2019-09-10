"""
making decsions
<, > , <=, >= , ==, !=
1<3 and 2>3
input
"""
def input_score():
    while True: 
        score = input('Pls input your score of CSCI 13200: ')
        score = int(score)
        if 0<=score<=100:
            break
        else:
            print('the score should be greater than 0 and less than 100. Pls input again')
    return score

def evaluate_performance(score):
    if 90<=score<=100:
        performance = 'A'
    elif 80<=score:
        performance = 'A-'
    elif 70<=score:
        performance = 'B+'
    elif 60<=score:
        performance = 'B'
    else:
        performance = 'F'
    return performance

def show_my_performance(performance):
    print('your performance for CSCI13200 is ', performance)

score_here = input_score()
performance = evaluate_performance(score_here)
show_my_performance(performance)
