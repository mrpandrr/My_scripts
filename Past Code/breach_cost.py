a = "To determine the cost of a data breach in your organization, please provide your industry and the number of records breached. \n(A breached record is one that contains personally identifiable information, such as SSN, credit card, CVV, etc)."
b = "When asked for 'Industry', please indicate one of the following: \n\tCommunications\n\tRetail\n\tPharmaceutical\n\tEducation"
print (a)
print (b)

industry = input("Please indicate industry: ")
print ("Here's what was entered",industry)

if(industry=="Communications"):
    records_breached = input("Enter the number of records breached")
    records_breached = int(records_breached)
    cost = 219 * records_breached
    print("Cost of a data breach in",industry, "is ",cost)
elif(industry=="Retail"):
    records_breached = input("Enter the number of records breached")
    records_breached = int(records_breached)
    cost = 120 * records_breached
    print("Cost of a data breach in",industry, "is ",cost)
elif(industry=="Pharmaceutical"):
    records_breached = input("Enter the number of records breached")
    records_breached = int(records_breached)
    cost = 209 * records_breached
    print("Cost of a data breach in",industry, "is  ",cost)
elif(industry=="Education"):
    records_breached = input("Enter the number of records breached")
    records_breached = int(records_breached)
    cost = 259 * records_breached
    print("Cost of a data breach in",industry, "is ",cost)
else:
    print (industry,"is unknown")
    print ( "Please choose from Communications, Retail, Pharmaceutical or”,\
“Education")