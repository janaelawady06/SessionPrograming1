#learning to code, basics

print("hello world")
print('hello world')
print('And John asked: "how are you?"')
print("7+6")
print(7+6)

print('"'"'")

print("3+4=", 3+4, "and 5*6=", 5*6)
#python puts a space after = after 7 and after = again so sometimes u dont want that:

print("I have $", 100+200, ".")
#i dont want the spaces here so:
print("I have $", 100+200, ".", sep="")
#this fixes it if u put nothing between the quotes

#another issue, each print starts on a new line, u dont always want that

print("1")
print("2")
print("3")
#if i want them on the same line:


print("1 ", end="")
print("2 ", end="")
print("3")
#end can be whatever u want like commas for example:
print("1", end=",")
print("2", end=",")
print("3")

#i could also end with an enter (like a return)

print("1", end=",")
print("2", end="\n\n")
print("3")

#\n means enter
#backslash does alot:

print("\"'")

print(6/2)
#answer here is given 3.0
#if u dont want it:

print(6//2)

print("this was added after first commit")
print("this is after we shared on github")
