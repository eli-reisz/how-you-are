name = input("what is your name? ").lower()
print(f"Hi {name}, your in for a ride!!!")
ready = input("are you ready[yes/no]? ").lower

if ready == "yes":
  print("alright then lets go!!")
  
elif ready == "no":
  exit()

score = 0

age = int(input("how old are you? "))

school = input("are you in school? ").lower()
if age <= 18 and school == "yes":
  score += 1

elif age <= 18 and school == "no":
  score -= 1
  
elif age > 18 and school == "yes":
  score += 2
  
elif age > 18 and school == "no":
  graduated = input("did you graduate high school? ").lower()
  
  if graduated == "yes":
    score += 1
  elif graduated == "no":
    score -= 1

job = input("do you have a job? ").lower()
if school == "yes" and job == "yes":
  score += 2
   
elif school == "no" and job == "yes":
  score += 1
  
elif school == "no" and job == "no":
  score -= 1
 
else:
  score + 0

religious = input("are you religious? ").lower()

if religious == "yes":
  score += 1
    
elif religious == "no":
  score -= 1

if age >= 18:
  married = input("are you married? ").lower()
  
  if married == "yes" and score >= 3:
    score += 1
  
  elif married == "yes" and score < 3:
    score -= 1

else:
  married = "no"
    
if married == "no":
  girlfreind = input("do you have a girlfreind? ").lower()
  if girlfreind == "yes" and age >= 18:
    score += 1
  elif girlfreind == "yes" and age < 18:
    score -= 1
  elif girlfreind == "no":
    score += 1
    

if score >= 4:
  print("Your happy!!!")
  
elif score < 4 and score > 0:
  print("your not stabl")
  
elif score <= 0:
  print("your dipresed")