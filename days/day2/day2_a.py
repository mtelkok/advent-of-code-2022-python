def getlines():
    file=open('.\..\..\Input\input-day2.txt')
    lines = file.read().splitlines()
    return lines

def get_shape(line):
    sum_shape=0
    if "X" in line:
        sum_shape+=1
    elif "Y" in line:
        sum_shape+=2
    else:
        sum_shape+=3
    return sum_shape

def get_winner_for_this_round(line):
    sum_winner=0
    if "X" in line:
        if "A" in line:
            sum_winner += 3
        elif "B" in line:
            sum_winner += 0
        else:
            sum_winner += 6
    elif "Y" in line:
        if "A" in line:
            sum_winner += 6
        elif "B" in line:
            sum_winner += 3
        else:
            sum_winner += 0
    else:
        if "A" in line:
            sum_winner += 0
        elif "B" in line:
            sum_winner += 6
        else:
            sum_winner += 3
    return sum_winner

def total(liness):
    sum_total=0
    for line in liness:
        sum_total+=get_winner_for_this_round(line)+get_shape(line)
    return sum_total

print(total(getlines()))

