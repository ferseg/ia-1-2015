from FileValidation import *

import re

def open_file():
    file = open("input.txt","r");
    return file;

def read_file(file):
    data_file = file.read();
    return data_file;

#get all matches of the re in data
def get_babylon_tower(data):
    babylon_tower = re.findall(r"\b(F[1-4])(=)([BROGH],[BROGH],[BROGH],[BROGH])((,)([BROGH]))?\b",data);
    return babylon_tower;

#print all the matches of the babylon_tower format
def get_babylon_tower_rows(babylon_tower):
    for row in babylon_tower:
        print(row)       
    
def main():
    #open file
    file = open_file();
    #read file's text
    file_text = read_file(file);
    #get the first structure of a babylon tower
    babylon_tower = get_babylon_tower(file_text);
    #print the rows of the regex applied to the .txt input file
    get_babylon_tower_rows(babylon_tower);
    #apply all the validations to the babylon tower entered
    return validate_tower(babylon_tower);
    

main();
