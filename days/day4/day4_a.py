def getlines():
    file=open('.\..\..\Input\input-day4.txt')
    lines = file.read().splitlines()
    return lines

def split_elf(line):
    list=line.split(",")
    first_elf,second_elf=list[0],list[1]
    list2=first_elf.split("-")
    list3=second_elf.split("-")
    first_elf_start,first_elf_finish=int(list2[0]),int(list2[1])
    second_elf_start,second_elf_finish=int(list3[0]),int(list3[1])
    return [first_elf_start,first_elf_finish,second_elf_start,second_elf_finish]

def does_contain(elf_list):
    first_elf_start = elf_list[0]
    first_elf_finish = elf_list[1]
    second_elf_start = elf_list[2]
    second_elf_finish= elf_list[3]
    return (second_elf_start>=first_elf_start and first_elf_finish>=second_elf_finish) or (first_elf_start>=second_elf_start and second_elf_finish>=first_elf_finish)
def count(lines):
    sum=0
    for line in lines:
        position_list=split_elf(line)
        contains=does_contain(position_list)
        if contains==True:
            sum+=1
    return sum
print(count(getlines()))