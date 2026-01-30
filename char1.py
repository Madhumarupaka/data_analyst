# string operations
def string_supp( string1 ):
    lower=""
    upper=""
    digit=""
    special=""
    for x in string1:
        if x.islower():
            lower+=x
        elif x.isupper():
            upper+=x
        elif x.isdigit():
            digit+=x
        else:
            special+=x
    print("lower:",lower)
    print("upper:",upper)
    print("digit:",digit)
    print("special_char:",special)


#input string
string1="Madhu@4223KAnna"
string_supp(string1)
