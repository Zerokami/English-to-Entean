import sys

PY2 = sys.version_info[0] == 2 #Returns True if Python version is 2 

if PY2:
    from string import maketrans
    input = raw_input
else:
    maketrans = str.maketrans

FULL_ENGLISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
FULL_ENTEAN_ALPHABET =  "AZYXEWVTISRLPNOMQKJHUGFDCB"

FULL_ENGLISH_ALPHABET += FULL_ENGLISH_ALPHABET.lower()
FULL_ENTEAN_ALPHABET += FULL_ENTEAN_ALPHABET.lower()

translaton_table = maketrans(FULL_ENGLISH_ALPHABET, FULL_ENTEAN_ALPHABET)


def to_entean(text):
    return(text.translate(translation_table))
    

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
