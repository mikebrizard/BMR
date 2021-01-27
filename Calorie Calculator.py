print("Welcome to the Calorie Calculator where you will find out your BMR and get a breakdown of your daily recommended calorie intake spread across the 3 micronutrients: Protein, Carbs and Fat")
name = input("OK lets get started. What is your name?:")
yourweight = input(f"Ok {name}, how much do you weigh in pounds?")
yourage = input("How old are you in years?")
yourheight = input("How tall are you in inches?")
yourgender = int(input("What is your gender: M or F?"))


weight = int(yourweight)
age = int(yourage)
height = int(yourheight)

mbmr= 66
mbmrbw = weight * 6.3
mbmrht = height * 12.9
mbmrage = age * 6.8

fbmr = 655
fbmrbw = weight * 4.3
fbmrht = height * 4.7
fbmrage = age * 4.7

yourbmrm = (mbmr) + (mbmrbw) + (mbmrht) -(mbmrage)
yourbmrf = (fbmr) + (fbmrbw) + (fbmrht) - (fbmrage)

proteiningrams = weight 
carbsingrams = int(weight * .6)

proteincalories = proteiningrams * 4
carbscalories = carbsingrams * 4

fatscaloriesm = int((yourbmrm) - (proteincalories) - (carbscalories))
fatscaloriesf = int((yourbmrf) - (proteincalories) - (carbscalories))

fatsingramsm = fatscaloriesm // 9

if yourgender <= 1:
  print(f"Your BMR is {yourbmrm}")
  print(f"""Protein Intake: {proteiningrams} grams
Protein Calories: {proteincalories} calories
Carb Intake: {carbsingrams} grams 
Carbs Calories: {carbscalories} calories
Fats Intake {fatscaloriesm} calories 
Fats Grams {fatscaloriesm // 9} grams of fats""")

 
else:
  print(f"Ok {name}, your BMR is {yourbmrf}") 
  print(f"""  Protein intake: {proteiningrams} grams 
  Protein Calories: {proteincalories} calories
  Carb intake: {carbsingrams} grams 
  Carb Calories: {carbscalories} calories
  Fats intake: {fatscaloriesf} calories 
  Fats Calories: {fatscaloriesf // 9} grams""")
