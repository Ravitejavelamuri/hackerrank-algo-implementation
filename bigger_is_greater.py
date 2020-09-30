for _ in range(int(input())):
    s = input()
    has_g = False
    for i in range(len(s)-1)[::-1]:
        if ord(s[i]) < ord(s[i+1]):
            for j in range(i+1,len(s))[::-1]:
                if ord(s[i]) < ord(s[j]):
                    lis = list(s)
                    lis[i],lis[j]=lis[j],lis[i]
                    print("".join(lis[:i+1]+lis[i+1:][::-1]))
                    has_g = True
                if has_g == True:
                    break
                if has_g == False:
                    print("no answer")
                if has_g == True:
                    break
   
