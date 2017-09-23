import os
inp = "input_texts"
lst = os.listdir(inp)
for fl in lst:
    os.system(r"C:\My\studies\HSE\programming\HSE_programming_2\cws\CW3\mystem.exe --format xml -i -n " + inp + os.sep + fl + " output_texts" + os.sep + fl)
