math = int(input("Enter Math Marks: "))
Science = int(input("Enter Science Marks: "))
Geography = int(input("Enter Geography Marks: "))

totalPercentage = (100*(math + Science + Geography))/300

if(totalPercentage >= 40 and math > 32 and Science > 32 and Geography > 32):
    print("PASS", totalPercentage)

else:
    print("FAIL", totalPercentage)