Word=input()
Word_list=list(Word)
Word_list.reverse()
Word_R=''.join(Word_list)

if Word==Word_R:
    print(1)
else:
    print(0)