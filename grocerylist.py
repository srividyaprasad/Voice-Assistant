import text_to_speech as t

path=r"C:\Users\srivi\OneDrive\Desktop\miniproject\grocerylist.txt"
def main(x, item):

    if x=='add':
        f=open(path, 'a')
        f.write('\n')
        f.write(item)
        f.close()
        t.speak(item+" has been added to grocery list")
        
    if x=='remove':
        f = open(path,'r')
        lst = []
        for line in f:
                if item in line:
                    line = line.replace(item,'')
                    lst.append(line)
        f.close()
        f = open(path,'w')
        for line in lst:
            f.write(line)
        f.close()
        t.speak(item+" has been removed from grocery list")

    if x=='read':
        n=0
        t.speak('here is your grocery list')
        f = open(path,'r')
        for line in f:
            n+=1
            t.speak(str(n))
            t.speak(line)