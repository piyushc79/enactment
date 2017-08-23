# Reverse words in a given string


def reverse_string_word(string):
    temp = ''
    n = len(string)
    for i in range(n):
        c = string[n-1-i]
        if c == ' ':
            if temp:
                print temp,
                temp = ''
        else:
            temp = c + temp
    if temp:
        print temp


if __name__ == '__main__':
    s = 'geeks quiz practice code'
    print s
    reverse_string_word(s)