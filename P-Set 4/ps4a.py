# Problem Set 4A
# Name: Abdul Rafay
# Collaborators: none
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #base case: if the sequence is just one letter then it is its own permutation
    if len(sequence)==1:
        return [sequence]
    #recursive part
    #enumerate allows to list the individual letters along with their index
    #so for a (index 0) it will apply get_permutations on the sub sequence 'bc' and then on c
    #so 'c' will be k when returning. And 'b' will be k on returning for i=1
    #hence backtracking we will have cb and bc
    #add them to j which was 'a' we get abc, acb. So forth for b and c, we will get all the permutations
    else:
        result = []
        for i, j in enumerate(sequence):
            result += [j + k for k in get_permutations(sequence[:i] + sequence[i + 1:])]
        return result



if __name__ == '__main__':
   example_input = input('input sequence to permute')
   print('Input:', example_input)
   print('Actual Output:', get_permutations(example_input))
   print(len(get_permutations(example_input)))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)



