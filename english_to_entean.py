
FULL_ENGLISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
FULL_ENTEAN_ALPHABET =  "AZYXEWVTISRLPNOMQKJHUGFDCBazyxewvtisrlpnomqkjhugfdcb"


tran_tab = str.maketrans(FULL_ENGLISH_ALPHABET, FULL_ENTEAN_ALPHABET)

def to_entean(text):
    return(text.translate(tran_tab))
    

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
