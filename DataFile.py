import re


def open_file():
    file = open("input.txt","r");
    return file;

def read_file(file):
    data_file = file.read();
    return data_file;

#get all matches of the re in data
def get_babylon_tower(data):
    babylon_tower = re.findall(r"\b(F[1-4])(=)([POGYH],[POGYH],[POGYH],[POGYH])((,)([POGYH]))?\b",data);
    return babylon_tower;

#print all the matches of the babylon_tower format
def get_babylon_tower_rows(babylon_tower):
    for row in babylon_tower:
        print(row)

def test():
    get_babylon_tower_rows(get_babylon_tower(read_file(open_file())));

test();
