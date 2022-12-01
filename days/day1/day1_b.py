def getlines():
    file=open('.\..\..\Input\input-day1.txt')
    lines = file.read().splitlines()
    return lines

def get_elf_list(lines):
    sum=0
    elf_list=[]
    for line in lines:
        if line=="":
            elf_list.append(sum)
            sum=0
        else:
            sum=sum+float(line)
    return elf_list

def find_biggest_elf(list_elf):
    max_cal=list_elf[0]
    for sum in list_elf:
        if sum>max_cal:
            max_cal=sum
    return max_cal

def find_biggest_three_elf(list_elf):
    biggest=find_biggest_elf(list_elf)
    list_elf.remove(biggest)
    second_biggest=find_biggest_elf(list_elf)
    list_elf.remove(second_biggest)
    third_biggest=find_biggest_elf(list_elf)
    return biggest+second_biggest+third_biggest
print(find_biggest_three_elf(get_elf_list(getlines())))
