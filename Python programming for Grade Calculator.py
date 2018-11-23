# Python program - Calculate Grade of Student

print("Grade Calculator Designed by Apexontop");
print("Enter 'x' for exit.");
print("Enter marks obtained in 5 subjects: ");
mark1 = input();
if mark1 == 'x':
    exit();
else:
    mark1 = int(mark1);
    mark2 = int(input());
    mark3 = int(input());
    mark4 = int(input());
    mark5 = int(input());
    sum = mark1 + mark2 + mark3 + mark4 + mark5;
    average = sum/5;
    if(average>=70 and average<=100):
        print("Your Grade is A");
    elif(average>=60 and average<=69):
        print("Your Grade is B");
    elif(average>=50 and average<=59):
        print("Your Grade is C");
    elif(average>=45 and average<=49):
         print("Your Grade is D");
    elif(average>=40 and average<=44):
        print("Your Grade is E");
    elif(average>=0 and average<=39):
        print("Your Grade is F");
    else:
        print("Strage Grade...!!");
            
