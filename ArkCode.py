#quick made by Shiroikage
import sys
import time

def base_convert(i, b):
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b
    return result

def word_in(a):
    print("Letter: ",a)
    zehnb  = ord(a)
    print("ASCII: ", zehnb)
    vierb = base_convert(zehnb,4)
    print("Base 4: ", vierb)
    return vierb


def main():
    line = input("Enter words and separate with SPACE\n")
    i = 0
    j = 0
    final = []
    file = open("output_code.txt","w")
    for c in line:   
        if(line[i] != ' '):    
            result = word_in(line[i])
            for e in result:
                if(e == 0):
                    file.write('a')
                elif(e == 1):
                    file.write('d')
                elif(e == 2):
                    file.write('s')
                elif(e == 3):
                    file.write('w')
                j = j + 1
        else:
            file.write(' \n')
            print("NEW WORD")
            j = j + 1
        i = i+1
    file.close
    print("Window will close in 10 sec. Your ARK Code is in --> output_code.txt\n You can just copy and paste it to https://ark.gamepedia.com/Template:ARKCode\n")
    time.sleep(10)

main()    
