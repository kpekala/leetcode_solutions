
def countVowelPerm(n, lastVowel):
    if n == 0:
        return 1
    if lastVowel == 'a':
        return countVowelPerm(n-1, 'e')
    if lastVowel == 'e':
        return countVowelPerm(n-1, 'a') + countVowelPerm(n-1, 'i')
    if lastVowel == 'i':
        return sum([countVowelPerm(n-1, x) for x in ['a', 'e', 'o', 'u']])
    if lastVowel == 'o':
        return sum([countVowelPerm(n-1, x) for x in ['i', 'u']])
    if lastVowel == 'u':
        return countVowelPerm(n-1, 'a')

def countVowelPermutation(n: int) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    return sum([countVowelPerm(n-1, x) for x in vowels]) % (10e9+7)

print(countVowelPermutation(5))
        