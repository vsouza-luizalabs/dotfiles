import os
import click
import yaml

def install():
    osx()


    return True

def osx():

    stram = open("./osx/osx.yml", "r")
    read = yaml.load(stram)
    
    try:
    
        print read['computer_name']
        print read['host_name']
    
    except KeyError:
        print "ERROR"

def check():
    return False

if __name__ == "__main__":
    osx()
