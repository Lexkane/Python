# prints contents of the directory
import os


def main():
    pass


def magic(dir):
    acc = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            acc.append(os.path.join(root, file))
    return acc


dirs_to_print = input("Which dirs you wish to print")

if dirs_to_print is "":
    for k in magic('/home/'):
        print(k)

elif dirs_to_print is not None:
    for k in magic(dirs_to_print):
        print(k)
