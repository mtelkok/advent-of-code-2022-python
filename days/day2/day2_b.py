def getlines():
    file=open('.\..\..\Input\input-day2.txt')
    lines = file.read().splitlines()
    return lines

def get_winner_for_this_round(line):
    sum_winner=0
    if "X" in line:
        if "A" in line:
            sum_winner += 3
        elif "B" in line:
            sum_winner += 1
        else:
            sum_winner += 2
    elif "Y" in line:
        if "A" in line:
            sum_winner += 4
        elif "B" in line:
            sum_winner += 5
        else:
            sum_winner += 6
    else:
        if "A" in line:
            sum_winner += 8
        elif "B" in line:
            sum_winner += 9
        else:
            sum_winner += 7
    return sum_winner

def total(liness):
    sum_total=0
    for line in liness:
        sum_total+=get_winner_for_this_round(line)
    return sum_total
print(total(getlines()))
