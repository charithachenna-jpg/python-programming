try:
         file=open("output.txt","r")
except IOError:
         print("Error:Unable to read the file")
finally:
         file.close()
