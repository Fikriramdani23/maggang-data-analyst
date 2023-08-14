# mencari angka prima
def prima(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# mengakategorikan angka
def kategori_bilangan(angka):
    kategori = []

    if angka == 0:
        kategori.append("Nol")
    else:
        kategori.append("Bulat")
        if angka > 0:
            kategori.append("Cacah")
            kategori.append("Asli")
            if angka % 2 == 0:
                kategori.append("Genap")
            else:
                kategori.append("Ganjil")
            if prima(angka):
                kategori.append("Prima")
    
    return kategori

# menginput angka 
a = int(input("Ketik angka: "))
b = kategori_bilangan(a)
c = int(input("Ketik angka: "))
d = kategori_bilangan(c)
print(f"Angka {a} Tergolong : {', '.join(b)}")
print(f"Angka {c} Tergolong : {', '.join(d)}")