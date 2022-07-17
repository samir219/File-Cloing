import os
if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("spartan").menu()
   except Exception as e:
       exit(str(e))
