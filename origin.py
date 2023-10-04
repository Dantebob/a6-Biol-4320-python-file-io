#! /bin/python3

import re

print('Opening dummy.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening output_2.txt')
    with open('output.txt', 'w') as out_stream:
        search_str = "inheritance"
        match_re_obj = re.findall()
        line_num_re_obj = re.span()
#        for line in in_stream:
#            line = line.strip()
#            word_list = line.split()
#            word_list.sort()
#            for word in word_list:
#                out_stream.write('{0}\n'.format(word))
print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('output_2.txt is closed?', out_stream.closed)

if __name__ == '__main__':
    print("hi")
