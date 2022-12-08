#inputu aç
def getlines():
    file=open('.\..\..\Input\input-day5.txt')
    lines = file.read().splitlines()
    return lines

#part2'yi okut
def read_part_2(part2_lines):
    new_list = []
    for line in part2_lines:
        line = line.replace("move","")
        line = line.replace("from","")
        line = line.replace("to","")
        new_list.append(line)
    return new_list

#part1'i matris haline getir
def read_part_1(part1_lines):
    list_of_lists=[[],[],[],[],[],[],[],[],[]]
    for line in part1_lines[:-1]:
        for i in range(1,10):
            if i*4-3<len(line):
                if line[i*4-3]==" ":
                    continue
                list_of_lists[i-1].append(line[i*4-3])

    return list_of_lists

def move_from_list(list_of_lists, from_index, to_index, how_many):
    from_index=int(from_index)-1
    to_index=int(to_index)-1
    how_many=int(how_many)
    help=[]
    howmany=how_many
    while how_many>0:
        bonibon=list_of_lists[from_index].pop(0)
        help.insert(0,bonibon)
        how_many-=1
    while howmany>0:
        bonibon = help.pop(0)
        list_of_lists[to_index].insert(0, bonibon)
        howmany-=1
    return list_of_lists

#inputu okut
lines = getlines()
part_1, part_2 = [], []
mid_element = lines.index('')

#inputu ikiye böl
for i in range(mid_element):
    part_1.append(lines[i])
for i in range(mid_element + 1, len(lines)):
    part_2.append(lines[i])
part1=read_part_1(part_1)
part2=read_part_2(part_2)

for line in part2:
    numbers=line.split(" ")
    part1=move_from_list(part1,int(numbers[3]),int(numbers[5]),int(numbers[1]))

def biggest_line(lines):
    biggest=len(lines[0])
    for line in lines:
        if len(line)>biggest:
            biggest=len(line)
    return biggest

print(part1)