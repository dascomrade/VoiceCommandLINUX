def replaceLetter(input):
 outpt = []
 inputlow = input.lower()
 numbers = [0,1,2,3,4,5,6,7,8,9]
 outpt.append("\n")

 for letter in inputlow:
    if (letter == "a"):
        outpt.append("Alpha")
    elif(letter == "b"):
        outpt.append("Bravo")
    elif(letter == "c"):
        outpt.append("Charlie")
    elif(letter == "d"):
        outpt.append("Delta")
    elif(letter == "e"):
        outpt.append("Echo")
    elif(letter == "f"):
        outpt.append("Foxtrot")
    elif(letter == "g"):
        outpt.append("Golf")
    elif(letter == "h"):
        outpt.append("Hotel")
    elif(letter == "i"):
        outpt.append("India")
    elif(letter == "j"):
        outpt.append("Juliet")
    elif(letter == "k"):
        outpt.append("Kilo")
    elif(letter == "l"):
        outpt.append("Lima")
    elif(letter == "m"):
        outpt.append("Mike")
    elif(letter == "n"):
        outpt.append("November")
    elif(letter == "o"):
        outpt.append("Oscar")
    elif(letter == "p"):
        outpt.append("Papa")    
    elif(letter == "q"):
        outpt.append("Quebec")
    elif(letter == "r"):
        outpt.append("Romeo")
    elif(letter == "s"):
        outpt.append("Sierra")
    elif(letter == "t"):
        outpt.append("Tango")
    elif(letter == "u"):
        outpt.append("Uniform")
    elif(letter == "v"):
        outpt.append("Victor")
    elif(letter == "w"):
        outpt.append("Whiskey")
    elif(letter == "x"):
        outpt.append("X-Ray")
    elif(letter == "y"):
        outpt.append("Yankee")
    elif(letter == "z"):
        outpt.append("Zulu")
    elif(letter == " "):
       outpt.append("\n ")
    else:
        outpt.append(letter)

 #for numbers in input:
  # outpt.append(numbers)

 combined = " ".join(outpt)
 return combined
inp = input("")
output = replaceLetter(inp)
print(output)
