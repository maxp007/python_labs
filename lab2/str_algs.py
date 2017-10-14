
def rew_str(str):
    strlist = list(str)
    temp='a'
    for i in range(0,len(strlist)):
        if i < int(len(strlist)/2 ):
            temp = strlist[i]
            strlist[i]= strlist[len(strlist)-i-1]
            strlist[len(strlist) - i - 1] = temp

    return ''.join(strlist)


string1 = "hello, world"
print(rew_str(string1))