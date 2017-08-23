# Given a string, find the first non-repeating character in it.
# For example, if the input string is "abcdecaktb", then output should be "d"


def first_np_repeat_char(string):
    char_mapping = {}
    i = 0
    for s in string:
        if char_mapping.get(s):
            char_mapping[s] = (char_mapping[s][0], char_mapping[s][1]+1)
        else:
            char_mapping[s] = (i, 1)
        i += 1
    j = None
    c = None
    for k, v in char_mapping.items():
        if v[1] == 1 and (v[0] < j or j is None):
            j = v[0]
            c = k
    return c

if __name__ == '__main__':
    string = 'abcdecaktb'
    print 'First non repeating character of ' \
          'string {} is {}'.format(
        string, first_np_repeat_char(string))
