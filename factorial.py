def main():
  
  while True:
    num = int(input('\nDigite um valor entre 0 e 997 para saber seu fatorial: '))
    
    def fatorial(n):
      if n <= 1:
        return 1
      return n * fatorial(n-1)
    
    print('-' * 20)
    print(fatorial(num))
    
if __name__ == "__main__":
  main()
