import json


def open_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    data = json.loads(text)
    return data


def xmlfy(line_dict):
    xmline = ''
##{"text":" "}
##{"text":"пожар","analysis":[{"lex":"пожар","gr":"S,m,inan=acc,sg"},{"lex":"пожар","gr":"S,m,inan=nom,sg"}]}
##{"text":". "}
 
##<w>пожар<ana lex="пожар" gr="S,m,inan=acc,sg" /><ana lex="пожар" gr="S,m,inan=nom,sg" /></w>. 
##</se>
    sent = ['. ', '! ', '? ', '!!! ', '.', '!', '?', '... ']
    if not analysis in line_dict:
        if line_dict[text] in sent: 
            xmline = line_dict[text] + '\n</se>\n<se>\n'
        else:
            xmline = line_dict[text]
    else:
        xmline = '<w>' + line_dict[text]
        for ana in line_dict[analysis]:
            xmline += '<ana lex="' + ana[lex] + '" gr="' + ana[gr] + '"  />'
        xmline += '</w>'
    return xmline


def create_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        text = f.write()
    return True

def main():
    xmltext = '<?xml version="1.0" encoding="utf-8"?>\n<html><body>\n\n<se>'
    data = open_json('text.json')
    for i in data:
        xmltext += xmlfy(i)
    xmltext = xmltext[:-11] + '\n' + xmltext[-11:-6] ## отрезаем лишнее \n<se>\n с конца, добавляем перенос строки перед последним </se>
    xmltext += '\n</body></html>'
    create_file(xmltext, 'text.html')
if __name__ == "__main__":
    main()
