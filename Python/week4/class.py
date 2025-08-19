file = open("./Python/week4/js.pdf","w")
file.write("JsMammie1, JsMammie2, JsMammie3 \n")

#Reading content from a file
#new . after the working folder and writing file with specific path

'''file= open("./Python/week4/js.pdf","r")
content = file.read()
'''


#appending new line with a
file=open("./Python/week4/js.pdf", "a")
file.write("O my God, I never though")
file= open("./Python/week4/js.pdf","r")
content = file.read()
cont=file.readlines()
print(content)
