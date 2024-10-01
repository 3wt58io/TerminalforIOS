import os
code = input("send raw file\n")
def extract_last_segment(url):
    # Split the URL by '/' and get the last segment after 'raw'
    segments = url.split('/')
    if 'raw' in segments:
        return segments[segments.index('raw') + 1]
    return None
print(extract_last_segment(code))

os.system(f"wget {code}")
cmd = input("d for delete/r for rename\n").lower()

def main(): 
    start = True
    while start:
      codename = extract_last_segment(code)
      if cmd == "r":
         codename = input("new name: ")
         os.system(f"mv {extract_last_segment(code)} {codename}")
      elif cmd == "d":
          os.system(f"rm {codename}")
      elif cmd == "run":
          os.system(f"wget {code}")
      if codename != extract_last_segment(code):
          
          os.system(f"rm {codename}")
          os.system(f"mv {extract_last_segment(code)} {codename}")
          os.system(f"python3 {codename}")
      elif cmd == "end":
          start = False
       os.system("sync")   
# Make sure to call the main function
if __name__ == "__main__":
    main()
