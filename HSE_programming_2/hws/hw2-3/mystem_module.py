import os

def mystem_xml(inp):
    lst = os.listdir(inp)
    for fl in lst:
        os.system(r"C:\My\studies\HSE\programming\HSE_programming_2\hws\hw2-3\mystem.exe --format xml -i -n " + inp + os.sep + fl + " C:\My\studies\HSE\programming\HSE_programming_2\hws\hw2-3\ks-yanao\mystem-xml" + os.sep + fl)

def mystem_plain (inp):
    lst = os.listdir(inp)
    for fl in lst:
        os.system(r"C:\My\studies\HSE\programming\HSE_programming_2\hws\hw2-3\mystem.exe -i -n " + inp + os.sep + fl + " C:\My\studies\HSE\programming\HSE_programming_2\hws\hw2-3\ks-yanao\mystem-plain" + os.sep + fl)



##inp = r'C:\My\studies\HSE\programming\HSE_programming_2\hws\hw2-3\ks-yanao\plain\2017\09'
##lst = os.listdir(inp)
##for fl in lst:
##    os.system(r"C:\My\studies\HSE\programming\HSE_programming_2\hws\hw2-3\mystem.exe -i -n " + inp + os.sep + fl + " C:\My\studies\HSE\programming\HSE_programming_2\hws\hw2-3\ks-yanao\mystem-plain" + os.sep + fl)
