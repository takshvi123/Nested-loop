word=input("Please Enter a Word ")
cha=input("Enter the Character you want to be searched ")
i=0
c=0
num=len(word)
while i<num:
    if word[i]==cha:
        c=c+1
    i=i+1    
print(f"The Number Of Times {cha} apperes in {word} is {c}")
print("Have a NICE DAY ")