# ABOUT : The program deals with the working of files system
#       : Different methods to deal with files
#       * open("file_name", "mode of operation")

# open file and link the file object to variable
file_ref = open("../datasets/olympic.txt", "r")

# print(file_ref)

# closes the file object
# have to close after every use
file_ref.close()