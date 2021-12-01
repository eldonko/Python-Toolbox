# imports
import sys
import os
import tkinter as tk
from tkinter import filedialog

"""
This scripts automatically generates a folder structure for a new library/class. It should be run from 
the command line. Mandatory command line inputs are:

library/class name (name): name of the library/class

Usage: python create_library.py <name>
"""


def main(argv):
    if len(argv) != 1:
        raise ValueError()

    lib_name = argv[0]

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory()

    # Create the library folder
    lib_path = os.path.join(file_path, lib_name)
    os.mkdir(lib_path)

    # Create the sub folders
    os.mkdir(os.path.join(lib_path, 'Code'))
    os.mkdir(os.path.join(lib_path, 'Code Testing'))
    os.mkdir(os.path.join(lib_path, 'Demos'))
    os.mkdir(os.path.join(lib_path, 'Development'))
    os.mkdir(os.path.join(lib_path, 'Documentation'))

    class_file = open(os.path.join(lib_path, 'Development') + r'\\' + lib_name + '.py', 'w')
    class_file.write('\n\nclass ' + lib_name + ': \n')
    class_file.write('\tpass')
    class_file.close()

    test_file = open(os.path.join(lib_path, 'Code Testing') + r'\\' + 'test_' + lib_name + '.py', 'w')
    test_file.write('from ' + lib_name + '.Development.' + lib_name + ' import ' + lib_name)
    test_file.write('\n\ndef main():\n\tpass')
    test_file.write('\n\nif __name__ == \'__main__\':\n\tmain()')
    test_file.close()

    print('Library directory created successfully')


if __name__ == "__main__":
    main(sys.argv[1:])


