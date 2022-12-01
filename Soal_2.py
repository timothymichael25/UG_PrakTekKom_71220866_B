print ("========== Alat Cek Palindrome ==========")
print ("Masukan kata anda")
a = str(input(">> "))

def funPalindrome():
    if a == a[::-1]:
        print ("Palindrome")
        print ("Jika dibalik ",a)
    else:
        print ("Bukan Palindrome")
        print ("Jika dibalik ",a)

funPalindrome()