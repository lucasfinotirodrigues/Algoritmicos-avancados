primeiro = 0
segundo = 0

while(segundo < 50):
  print(segundo)
  segundo = segundo + primeiro
  primeiro = segundo - primeiro
  if(segundo == 0):
    segundo = segundo + 1