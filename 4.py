def singkatan(s):
    a = ""
    for kata in s:
        if kata in s.upper():
            a += kata
   
    return a

def main():
    kata = raw_input("Masukan angka: ")
    print(singkatan(kata))
main()
