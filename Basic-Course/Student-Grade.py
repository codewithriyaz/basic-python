# Start Code Here
maths = 95
science = 95
english = 95
social = 95
language = 90
total = maths+science+english+social+language
average = total/5
print("Your Total Score is "+str(total))
print("Your Average Score is "+str(average))
if average > 90:
  print("Your Grade is A+")
elif average < 90 and average > 80:
  print("Your Grade is A")
elif average < 80 and average > 70:
  print("Your Grade is B+")
elif average < 70 and average > 60:
  print("Your Grade is B")
elif average < 60 and average > 50:
  print("Your Grade is C+")
elif average < 50 and average > 40:
  print("Your Grade is C")
else:
  print("Sorry ! You are Failed.")
