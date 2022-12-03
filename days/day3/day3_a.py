def getlines():
    file=open('.\..\..\Input\input-day3.txt')
    lines = file.read().splitlines()
    return lines

def find_item_per_rucksack(line):
    count=0
    compartment1=[]
    compartment2=[]
    count=len(line)
    count=count/2
    count=int(count)
    for i in range(len(line)):
        if i in range(count):
            compartment1.append(line[i])
        else:
            compartment2.append(line[i])
    item_that_both_compartment_has=[]
    for i in range(len(line)):
        if line[i] in compartment1 and line[i] in compartment2:
            if not line[i] in item_that_both_compartment_has:
                item_that_both_compartment_has.append(line[i])
            else:
                continue
    return item_that_both_compartment_has

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
    for line in lines:
        sum_total+=get_value_of_the_item(find_item_per_rucksack(line))
    return sum_total
print(get_the_total_value(getlines()))
