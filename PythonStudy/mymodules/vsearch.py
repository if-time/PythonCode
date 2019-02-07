def searchvowels(word:str) -> set:
        """Return any vowels found in a supplied word."""
        vowels = set('aeiou')
        return vowels.intersection(set(word))

def searchletters(phrase:str, letters:str) -> set:
        """Return a set of the 'letters' found in 'phrase'."""
        return set(letters).intersection(set(phrase))

def searchletters(phrase:str, letters:str='aeiou') -> set:
        """Return a set of the 'letters' found in 'phrase'."""
        return set(letters).intersection(set(phrase))
