def arkademy(n):
  result = []
  for x in range(1, n+1):
      if x % 3 == 0 and x % 7 == 0:
          result.append("arkademy")
      elif x % 3 == 0:
          result.append('arka')
      elif x % 7 == 0:
          result.append('demy')
      else:
          result.append(str(x))
  return result
def main():
    angka = int(input("Masukan angka: "))
    print(', '.join(arkademy(angka)))
main()
