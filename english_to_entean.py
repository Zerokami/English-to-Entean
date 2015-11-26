FULL_ENGLISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
FULL_ENTEAN_ALPHABET = "AZYXEWVTISRLPNOMQKJHUGFDCBazyxewvtisrlpnomqkjhugfdc"


def get_letter(letter):
    """Return english letter translated to entean."""
    alpha_place = FULL_ENGLISH_ALPHABET.find(letter)

    return FULL_ENTEAN_ALPHABET[alpha_place] if alpha_place >= 0 else letter


def to_entean(text):
    """Return text translated from english to entean."""

    entean_output = ""

    for word in text.split(" "): 
        entean_word = ""

        for letter in word:
            entean_letter = get_letter(letter)
            entean_word += entean_letter

        entean_output += " " + entean_word

    return entean_output.strip()


def main(text=None, with_output=True):

    if text is None:
        text = input("Enter English text: ")

    if with_output:    
        print(text)
    
    entean_text = to_entean(text)
    
    if with_output:
        print(entean_text)
    

if __name__ == "__main__":
    main()
