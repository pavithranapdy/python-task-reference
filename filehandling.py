file=open("cmd.txt","r")  # syntax  open("filename", mode)
print(file.read())        # read the open file using (file.read())

#write mode
# Creates a new file if it does not exist
# Overwrites existing content
file = open("cmd.txt", "w")
file.write("Hello Python") 
file.close()

# a – Append mode
# Adds data at the end of the file
# File is created if it does not exist
file = open("cmd.txt", "a")
file.write("\nWelcome")
file.close()

# r+ – Read and Write
# Read and write both
# File must exist

file = open("cmd.txt", "r+")
print(file.read())
file.write("New text")
file.close()

print("5.Rename")
os.rename("cmd.txt", "data1.txt")

print("6.Remove")
os.remove("data1.txt")

print("7.Make Directory")
os.mkdir("MyFolder")