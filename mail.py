s=input()
for i in range(0,len(s)):
    if s.count("@")==1 and s.count(".")==1:
        if s[i]=="@":
            a=i
        if s[i]==".":
            b=i
            if b-a>=5 and a>=3:
                if s[-4:-1]==".co" and s[-1]=="m" and s[a+1:b]=="gmail":
                    print("YES")
                    break
                else:
                    print("NO")
                    break
            else:
                print("NO")
                break
    else:
        print("NO")
        break
