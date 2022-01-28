import text_to_speech as t

path=r"C:\Users\srivi\OneDrive\Desktop\miniproject\todolist.txt"
def main(x, task):

    if x=='add':
        f=open(path, 'a')
        f.write(task[1])
        f.close()
        t.speak(task+" has been added to to do list")

    if x=='remove':
        f = open(path,'r')
        lst = []
        for line in f:
                if task in line:
                    line = line.replace(task,'')
                    lst.append(line)
        f.close()
        f = open(path,'w')
        for line in lst:
            f.write(line)
        f.close()
        t.speak(task+" has been removed from to do list")

    if x=='read':
        n=0
        t.speak('here is your to do list')
        f = open(path,'r')
        for line in f:
            n+=1
            t.speak(str(n))
            t.speak(line)
