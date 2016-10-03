def formatter():
    string = raw_input('Enter the String : \n')
    string = string.replace('{', '&#224;')
    string = string.replace('}', '&#226;')
    string = string.replace(',', '&#117;')
    string = string.replace('/', '&#120;')
    string = string.replace('"', '&#107;')
    string = string.replace(';', '&#163;')
    string = string.replace(':', '&#162;')
    string = string.replace("'", '&#112;')
    string = string.replace('(', '&#113;')
    string = string.replace(")", '&#114;')
    string = string.replace("[", '&#192;')
    string = string.replace("]", '&#194;')
    string = string.replace("|", '&#225;')
    return string

print formatter()