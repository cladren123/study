p = int(input())
index = int(input())

def numbering(p):
    string = "0"
    for i in range(1,index):
        string2 = ""
        if string[index-1:index]:
            print(string[index-1:index])
            break
        else:
            while(i >0):
                string2 = str(i%p) +string2
                i = i//p
            string = string + string2

numbering(p)
