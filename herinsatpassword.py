print("""WELCOME TO MATHS QUIZ, THE AIM OF THE QUIZ IS TO PROVIDE GOOD PRACTICE OF 
ADDITION,SUBTRACTION,MUTLIPLICATION,INTEGRATION AND DIFFERTION,YOU CAN CHOOSE 
ANYONE TOPIC TO STUDY""")
name=str(input("ENTER YOUR NAME:"))

print("CHOOSE YOUR TOPIC FOR QUIZ:")
print("""1.CHOOSE 1 FOR ADDITION
2.CHOOSE 2 FOR SUBTRACTION
3.CHOOSE 3 FOR MUTLIPLICATION
4.CHOOSE 4 FOR DIVISON
5.CHOOSE 5 FOR DIFFERNTION 
6.CHOOSE 6 FOR INTEGRATION
PRESS ENTER TO MAKE CHOICE""")
choice=int(input("ENTER YOUR CHOICE:"))
import random
additions = [
    ["""Q) 1 + 3 =

     a. 2

     b. 4

     c. 5

     d. 6""","b"],
     ["""Q) 3 + 2 =

     a. 4

     b. 5

     c. 6

     d. 7""","b"],
     ["""Q) 4 + 4 =

     a. 6

     b. 7

     c. 8

     d. 10""","c"],
     ["""Q) 3 + 5 =

     a. 2

     b. 7

     c. 8

     d. 9""","c"],
     ["""Q) 7 + 2

     a. 5

     b. 6

     c. 8

     d. 9""","d"],
     ["""Q) 10 + 2 =

     a. 8

     b. 9

     c. 11

     d. 12""","d"],
     ["""Q) 7 + 6 =

     a. 12

     b. 13

     c. 14

     d. 15""","b"],
     ["""Q) 5 + 4 =

     a. 9

     b. 8

     c. 7

     d. 6""","a"],
     ["""Q) 2 + 2 =

     a. 0

     b. 3

     c. 4

     d. 5""","c"],
     ["""Q) 9 + 3 =

     a. 10

     b. 11

     c. 12

     d. 13""","c"],
     ["""Q) 8 + 3 =

     a. 10

     b. 11

     c. 12

     d. 13""","b"],
     ["""Q) 9 + 9 =

     a. 15

     b. 16

     c. 17

     d. 18""","d"],
     ["""Q) 8 + 7 =

     a. 13

     b. 14

     c. 15

     d. 16""","c"],
     ["""Q) 8 + 8 =

     a. 14

     b. 15

     c. 16

     d. 17""","c"],
     ["""Q) 7 + 10 =

     a. 0

     b. 7

     c. 16

     d. 17""","d"],
     ["""Q) 6 + 9 =

     a. 13

     b. 14

     c. 15

     d. 16""","c"],
     ["""Q) 6 + 6 =

     a. 11

     b. 12

     c. 13

     d. 14""","b"],
     ["""Q) 6 + 2 =

     a. 4

     b. 7

     c. 8

     d. 9""","c"],
     ["""Q) 3 + 8 + 13 =

     a. 22

     b. 23

     c. 24

     d. 25""","c"],
     ["""Q) 4 + 4 + 0 + 4 + 5 =

     a. 15

     b. 16

     c. 17

     d. 18""","c"]
     ]
subtraction=[
  ["""Q) 10-5=

  a.5

  b.6

  c.7

  d.8
  ""","a"
  ],
  ["""Q) 16-5=

  a.14

  b.13

  c.12

  d.11""","d"],
  ["""Q) 20-12=

  a.6

  b.7

  c.8

  d.9""","c"],
  ["""Q) 11-7=

  a.1

  b.2

  c.3

  d.4""","d"],
  ["""Q) 17-9=

  a.8

  b.9

  c.10

  d.11""","a"],
  ["""Q) 19-12=

  a.4

  b.5

  c.6

  d.7""","d"],
  ["""Q) 11-7=

  a.1

  b.2

  c.3

  d.4""","d"],
  ["""Q) 16-12=

  a.1

  b.2

  c.3

  d.4""","d"],
  ["""Q) 45-24=

  a.18

  b.19

  c.20

  d.21""","d"],
  ["""Q) 78-46=

  a.31

  b.32

  c.33

  d.34""","b"],
  ["""Q) 100-74=

  a.26

  b.27

  c.28

  d.29""","a"],
  ["""Q) 36-23=

  a.12

  b.13

  c.14

  d.15""","b"],
  ["""Q) 47-26=

  a.34

  b.21

  c.36

  d.32""","b"],
  ["""Q) 54-36=

  a.81

  b.18

  c.23

  d.28""","b"],
  ["""Q) 89-34=

  a.34

  b.54

  c.64

  d.55""","d"],
  ["""Q) 67-34=

  a.45

  b.40

  c.33

  d.44""","c"],
  ["""Q) 126-90=

  a.36

  b.46

  c.26

  d.56""","a"],
  ["""Q) 459-247=

  a.213

  b.312

  c.212

  d.214""","c"],
  ["""Q) 567-543=

  a.24

  b.34

  c.54

  d.64""","a"],
  ["""Q) 890-678=

  a.344

  b.345

  c.212

  d.456""","c"]
]
multiplication=[
  ["""Q) 5 x 5 =

   a.24

   b.25

   c.34

   d.23
  ""","b"],
  ["""Q) 6 x 7=

  a.48

  b.42

  c.49

  d.56""","b"],
  ["""Q) 4 x 5=

  a.25

  b.30

  c.20
  d.15

  ""","c"],
  ["""Q) 8 x 9=

  a.72

  b.64

  c.63

  d.80""","a"],
  ["""Q) 9 x 7=

  a.72

  b.64

  c.63

  d.80
  ""","c"],
  ["""Q) 7 x 7 =

  a.49

  b.45

  c.63

  d.70""","a"],
  ["""Q) 12 x 8 =

  a.108

  b.72

  c.120

  d.96""","d"],
  ["""Q) 13 x 6 =

  a.72

  b.78

  c.144

  d.90""","b"],
  ["""Q) 14 x 8 =
  
  a.112
  b.122
  c.132
  d.92""","a"],
  ["""Q) 45 x 3 = 
  a.125
  b.135
  c.95
  d.90""","b"],
  ["""Q) 8 x 4=
  a.32
  b.24
  c.36 
  d.34""","a"],
  ["""Q) 23 x 4 =
  a.72
  b.62
  c.78
  d.92""","d"],
  ["""Q) 56 x 2 =
  a.112
  b.212
  c.211
  d.121""","a"],
  ["""Q) 34 x 4 =
  a.136
  b.146
  c.236
  d.246""","a"],
  ["""Q) 42 x 2 =
  a.84
  b.86
  c.88
  d.92""","a"],
  ["""Q) 84 x 3 =
  a.262 
  b.252
  c.242
  d.232""","b"],
  ["""Q) 47 x 2 =
  a.92 
  b.84
  c.94
  d.82""","c"],
  ["""Q) 34 x 5 =
  a.135
  b.170
  c.175
  d.180""","b"],
  ["""Q) 22 x 5 =
  a.110
  b.120
  c.111
  d.101""","a"],
  ["""Q) 80 x 2 =
  a.150
  b.160
  c.120
  d.130""","b"]
   
]
divison=[
   
]

    # Randomize questions


if choice==1:
    

    
     

    # Randomize questions
    random.shuffle(additions)

    correct = 0
    incorrect = 0
    total_questions = 0

    print("QUIZ")
    print("The quiz will end after 3 incorrect answers.\n")

    for   addition in additions:

      # Stop if 3 answers are incorrect
      if incorrect == 3:
        break
   
      print(addition[0])

      answer = input("Your answer: ")

      total_questions += 1

      if answer.lower() == addition[1].lower():
        print("Correct!\n")
        correct += 1
      else:
        print("Incorrect!")
        print("Correct answer:", addition[1])
        print()
        incorrect += 1
elif choice==2:
      random.shuffle(subtraction)
  
      correct = 0
      incorrect = 0
      total_questions = 0
  
      print("QUIZ")
      print("The quiz will end after 3 incorrect answers.\n")
  
      for   subs in subtraction:
  
        # Stop if 3 answers are incorrect
        if incorrect == 3:
          break
     
        print(subs[0])
  
        answer = input("Your answer: ")
  
        total_questions += 1
  
        if answer.lower() == subs[1].lower():
          print("Correct!\n")
          correct += 1
        else:
          print("Incorrect!")
          print("Correct answer:", subs[1])
          print()
          incorrect += 1
elif choice==3:
        random.shuffle(multiplication)
    
        correct = 0
        incorrect = 0
        total_questions = 0
    
        print("QUIZ")
        print("The quiz will end after 3 incorrect answers.\n")
    
        for  mult in multiplication:
    
          # Stop if 3 answers are incorrect
          if incorrect == 3:
            break
       
          print(mult[0])
    
          answer = input("Your answer: ")
    
          total_questions += 1
    
          if answer.lower() == mult[1].lower():
            print("Correct!\n")
            correct += 1
          else:
            print("Incorrect!")
            print("Correct answer:", mult[1])
            print()
            incorrect += 1
elif choice==4:
  pass
elif choice==5:
  pass
else :
  pass


print("QUIZ RESULT")
print("Total questions attempted:", total_questions)
print("Correct answers:", correct)
print("Incorrect answers:", incorrect)


