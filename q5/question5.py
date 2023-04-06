def rev(s):
    a=s.split(" ")
    s1=""
    for i in range(len(a)):
        s1=s1+a[-i-1]+" "
    print(s1)


if __name__ == "__main__":
    s1="Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    s2="Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    print (s1)
    print()

    rev(s1)
    print()
    print (s2)
    print()
    rev(s2)
