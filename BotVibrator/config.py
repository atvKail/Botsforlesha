def compare_pass():
    file = open("conf/admin.txt", "r")
    a = file.read()
    file.close()
    return a


def write_newgenpass(a):
    file = open("conf/welcomepass.txt", "w")
    file.writelines(a)
    file.close()


def look_input():
    file = open("conf/welcomepass.txt", "r")
    a = file.read()
    file.close()
    return a


def updateadmin(a):
    file = open("conf/admin.txt", "w")
    file.writelines(a)
    file.close()
