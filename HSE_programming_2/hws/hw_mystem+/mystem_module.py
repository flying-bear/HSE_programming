import os

def mystem_xml_directory(inp):
    lst = os.listdir(inp)
    for fl in lst:
        print(fl + ' in mystem xml process')
        os.system("mystem.exe --format xml -i -n " + inp + os.sep + fl + " ks-yanao\mystem-xml" + os.sep + fl)


def mystem_plain_directory(inp):
    lst = os.listdir(inp)
    for fl in lst:
        print(fl + ' in mystem plain process')
        os.system("mystem.exe -i -n " + inp + os.sep + fl + " ks-yanao\mystem-plain" + os.sep + fl)


def mystem_xml(inp, fl):
    print(fl + ' in mystem xml process')
    command = "mystem.exe --format xml -i -n " + r" ks-yanao\plain" + os.sep + inp + os.sep + fl + " ks-yanao\mystem-xml" + os.sep + inp + os.sep + fl
    os.system(command)


def mystem_plain (inp, fl):
    print(fl + ' in mystem plain process')
    command = "mystem.exe -i -n " + r" ks-yanao\plain" + os.sep + inp + os.sep + fl + " ks-yanao\mystem-plain" + os.sep + inp + os.sep + fl
    os.system(command)
