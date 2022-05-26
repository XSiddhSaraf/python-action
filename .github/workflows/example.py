
import os

def main():
  print("Greetings from Github action!")
  token  = os.environ.get("AZURE_SECRET_TOKEN")
  
  if not token:
    raise RuntimeError("AZURE_SECRET_TOKEN env var is not set!")
  
  print("All good")

  
if __name__ == '__main__':
  main()
