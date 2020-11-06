connect = open("simple.txt","r")


cats = [ ]
for line in connect:
    line = line.strip()

    if "cost" in line and "data breach" in line:

        start = line.find("in") +3

        end = line.find("is")
        print(start)
        category = line[start:end]
        print (category)
        cats.append(category)
for item in cats:

    print ("Category:", item)

connect.close()

print

print ("Done!")
