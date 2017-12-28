"""Quiz: Most Frequent Word"""

def most_frequent(s):
    
    word_list = {}
    
    """Return the most frequently occuring word in s."""
    
    # HINT: Use the built-in split() function to transform the string s into an
    #       array
    
    words = s.split(" ")
    words.sort()
    #print(words)
    
    # HINT: Iterate through the array and count each occurance of every word
    #       using the .count() list method
    
    for word in words:
        print(word)
        word_list[word] = words.count(word)
            
    #print(word_list)
    
    # HINT: Find the number of times the most common word appears using max()
    
    keys = word_list.keys()
    values = word_list.values()
    max_val = values.index(max(values))
    
    # HINT: Locate the index of the most frequently seen word

    result = keys[max_val]
    
    # HINT: Return the most frequent word. Remember that if there is a tie,
    #       return the first (tied) word in alphabetical order.

    return result


def test_run():
    """Test most_frequent() with some inputs."""
    print most_frequent("cat bat mat cat bat cat") # output: 'cat'
    print most_frequent("betty bought a bit of butter but the butter was bitter") # output: 'butter'


if __name__ == '__main__':
    test_run()
