import os

def mystem_xml(inp):
    lst = os.listdir(inp)
    for fl in lst:
        os.system(r"C:\My\studies\HSE\programming\HSE_programming_2\cws\CW3\mystem.exe --format xml -i -n " + inp + os.sep + fl + " Красный_север\mystem-xml" + os.sep + fl)

def mystem_plain (inp):
    lst = os.listdir(inp)
    for fl in lst:
        os.system(r"C:\My\studies\HSE\programming\HSE_programming_2\cws\CW3\mystem.exe -i -n " + inp + os.sep + fl + " Красный_север\mystem-plain" + os.sep + fl)
