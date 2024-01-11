#기존 코드가 너무 복잡하여 질문 및 피드백을 받은 후
#count()와 replace()를 활용하여 개선한 코드

Word=input()

data=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in data:
    if Word.count(i):
        Word=Word.replace(i,'a')

print(len(Word))