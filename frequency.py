def most_frequent(string):
    d = dict()
    for key in string:
        d[key] = d.get(key, 0) + 1
    return d

def letters_in_decreasing_order_of_frequency(string):
    frequencies = most_frequent(string)
    frequencies = dict(sorted(frequencies.items(),key=lambda x:(x[1]),reverse=True))
    return frequencies
string = 'Mississippi'
print (letters_in_decreasing_order_of_frequency(string))
