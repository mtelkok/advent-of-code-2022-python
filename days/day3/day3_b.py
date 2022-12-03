def getlines():
    file=open('.\..\..\Input\input-day3.txt')
    lines = file.read().splitlines()
    return lines

def find_same_item_per_three_rucksack(lines3):
    line1=lines3[0]
    line2=lines3[1]
    line3=lines3[2]
    item=[]
    for i in line1:
        if not i in item and i in line2 and i in line3:
            item.append(i)
    for i in line2:
        if not i in item and i in line1 and i in line3:
            item.append(i)
    for i in line3:
        if not i in item and i in line1 and i in line2:
            item.append(i)
    return item

def get_value_of_the_item(line):
    count=0
    s = 'abcdefghijklmnopqrstuvwxyz'
    s2 = ('abcdefghijklmnopqrstuvwxyz').upper()
    for item in line:
        if item.islower():
            count+=s.find(item)+1
        else:
            count+=s2.find(item)+27
    return count

def get_the_total_value(lines):
    sum_total=0
    for i in range(0,len(lines),3):
        sum_total+=get_value_of_the_item(find_same_item_per_three_rucksack([lines[i],lines[i+1],lines[i+2]]))
    return sum_total
print(get_the_total_value(getlines()))
