# Algorithmus, der mir die 1000. Primzahl nach der 1 ausgibt

def prim(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
        return False
  return True

def finde_n_prim(n):
  count = 0
  num = 2
  while count < n:
    if prim(num):
      count += 1
    num += 1
  return num - 1

n = int(input("Gib den Wert von n ein um die n-te Primzahl zu finden: "))
nte_prim = finde_n_prim(n)
print("Die", n, "-te Primzahl ist:", nte_prim)