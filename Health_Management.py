
import datetime
def gettime():
    return datetime.datetime.now()

def add(n,items,a):
    if items==1:
        if action == 1:
            newname = n+"food" + ".txt"
            # print(newname)
            text = input("start writing")
            tem = str(gettime())
            f = open(newname, "a+")
            f.write('\n[{}]{}'.format(tem, text))
            print("data Entered Successfully")

        elif action == 2:
            f = open("newname", "r")
            print("here is Your data")
            print(f.read())

        else:
            f = open("newname", "r+")
            f.truncate(0)
            print("Logs Deleted")

        print("Items Logged for food")

    elif items==2:
        if action == 1:
            newname = n+"Exer"+ ".txt"
            # print(newname)
            text = input("start writing")
            # t = str(gettime())
            tem = str(gettime())
            f = open(newname, "a+")
            # f.write('\n[{}]{}'.format(t, text))
            f.write('\n [ {} ] {}'.format(tem, text))
            print("data Entered Successfully")

        elif action == 2:
            f = open("newname", "r")
            print("here is Your data")
            print(f.read())

        else:
            f = open("newname", "r+")
            f.truncate(0)
            print("Logs Deleted")
        print("Items Logged for Exercise")

print("***** Welcome to Health Management System *****")
action = int(input("Select the action "
      "\n1.Log"
      "\n2.REtrive"
      "\n3.Delete"))
name = input("Enter Your Name")
items = int(input("1.Log Food"
                  "\n2.Log Exercise"))

add(name,items,action)


