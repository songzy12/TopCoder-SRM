import string


class GoodLetters:

    def construct(self, good, N, G):
        count_good = G
        count_bad = N - G
        letters_good = set(good)
        letters_bad = set(string.ascii_uppercase) - letters_good
        if len(letters_good) < count_good or len(letters_bad) < count_bad:
            return ''
        return ''.join(letters_good)[:count_good] + ''.join(
            letters_bad)[:count_bad]

if __name__ == "__main__":    
    print(GoodLetters().construct(good="AEIOU", N=10, G=3))
