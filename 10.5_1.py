def Statistic(file):
    f = open(file)
    dictionary = {}
    for line in f.readlines():
        if len(line)>10:
            #print(type(line))
            mark = [',','.',':','\\',';','?','(',')']
            for m in mark:
                line = line.replace(m,' ')
            #print(line)

            lineattr = line.strip().split(" ")
            #print(lineattr)
            for char in lineattr:
                if char not in dictionary:
                    dictionary[char]=1
                else:
                    dictionary[char]+=1
    #print(dictionary)

    a = sorted(dictionary.items(),key = lambda x:x[1],reverse = True)
    return a


def printWords(file,n):
    a =  Statistic(file)
    for i in range(n):
        print(a[i])

file = 'C:\\Users\\24116\\Desktop\\poem.txt'
printWords(file,20)
