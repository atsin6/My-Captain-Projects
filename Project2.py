filename = input("filename : ")
output = filename.split(".")[-1]
if output == 'py' :
    print('Python')
elif output == 'c':
    print('C language')
elif output == ('CPP'):
    print('C++')
else :
    print('unknown extention')
