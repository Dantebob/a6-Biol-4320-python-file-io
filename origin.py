#! /bin/python3

import re

def re_file_search(in_file, out_file, pattern):
    """
    re_file_search takes in_file and out_file as arguements then reads in_file and writes matches found in in_file and the position where they were found to out_file.
     Prameters
     ----------------------
     re object is used to search for pattern

     Returns
     -----------
     None

     Creates
     -----------------------------
     text file listing positions of matches and the string recognized at that position.
    """
    re_pattern_obj = re.compile(pattern, re.IGNORECASE)
    with open(in_file, 'r') as in_stream:
        with open(out_file, 'w') as out_stream:
            line_num = 0
            for line in in_stream:
                line_num += 1
                line = line.strip()
                word_list = line.split()
                word_num = 0
                for word in word_list:
                    word_num += 1
                    if re_pattern_obj.search(word):
                        out_stream.write('[{0},{1}] {2}\n'.format(line_num, word_num, word))
    print("Done!")

if __name__ == '__main__':
    in_file = "origin.txt"
    out_file = "output2.txt"
    search_str = "Inherit"
    re_file_search(in_file, out_file, search_str)
