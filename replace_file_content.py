import fnmatch
import os
import sys
from os.path import exists


def findAndReplace(directory, find, replace, filepatterns):
    count = 0
    dump = open(directory + "/modify.txt", "a+")
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filepattern in filepatterns:
            for filename in fnmatch.filter(files, "*"+str(filepattern)):
                if filename == "modify.txt":
                    continue
                print("Checking file: " + filename)
                filepath = os.path.join(path, filename)
                with open(filepath) as f:
                    s = f.read()
                    s2 = s
                s = s.replace(find, replace)

                if s != s2:
                    line = "Replaced in content word " + find + " with " + replace + " in file " + filename
                    dump.write(line + "\n")
                    count += 1
                with open(filepath, "w") as f:
                    f.write(s)
    dump.close()
    print()
    print("Changed: ", count, " file(s)")


def findAndReplaceFilenames(starting_dir, string_to_replace, replacement_string, filepatterns):
    files_changed_count = 0
    dump = open(starting_dir + "/modify.txt", "a+")

    for path, dirs, files in os.walk(os.path.abspath(starting_dir)):
        for filepattern in filepatterns:
            for filename in fnmatch.filter(files, "*"+str(filepattern)):
                if filename == "modify.txt":
                    continue
                if exists(str(path) + '/' + str(filename)) is False:
                    print("This file name does NOT exist.")
                    break

                new_name = filename.replace(string_to_replace, replacement_string)

                if filename != new_name:
                    print("Old filename is: " + str(filename))
                    print('New filename is:', new_name)

                    dump.write("Rename file from " + filename + " to " + new_name + "\n")

                    path_with_old_file = path + "/" + filename
                    path_with_new_file = path + "/" + new_name

                    # Note: rename() - is a top-level function.
                    os.rename(path_with_old_file, path_with_new_file)
                    files_changed_count = files_changed_count + 1

    print()
    print('Renamed: ', files_changed_count, ' file(s)')
    dump.write("Renamed " + str(files_changed_count) + ' file(s) \n')
    dump.close()


def main():
    find, replace, mode, fileExt = get_input()
    dire = os.getcwd()
    print("Using directory: " + dire)

    if exists(dire) is False:
        print("This path does NOT exist.")
    else:
        if mode == "1":
            print("Doing content replacement...")
            findAndReplace(dire, find, replace, fileExt)
        elif mode == "2":
            print("Doing filenames replacement...")
            findAndReplaceFilenames(dire, find, replace, fileExt)
        else:
            print("That mode is not available!")
            exit(400)

    dump = open(dire + "/modify.txt", "a+")
    dump.write("-------------------------------------------------------------------------------------\n")
    dump.close()


def get_input():
    print()
    print()
    print(" You entered", len(sys.argv) - 1, "arguments at the command line.")

    if len(sys.argv) != 5:
        # Ordinary exception now vs. IndexError: list index out of range.
        raise Exception(
            " Error: Wrong number of arguments. Enter 4 arguments: 1. "
            "string to replace 2. replacement string 3.File extensions 4. mode ")

    # Read in parameters.
    string_to_replace = sys.argv[1]
    replacement_string = sys.argv[2]
    fileExt = list(sys.argv[3].split(","))
    mode = sys.argv[4]

    print(' String to replace:\t', string_to_replace)
    print(' Replacement string:\t', replacement_string)
    print(' File extensions:\t', fileExt)
    print(' Replacement mode:\t', mode)
    print()
    return string_to_replace, replacement_string, mode, fileExt


if __name__ == '__main__':
    main()
