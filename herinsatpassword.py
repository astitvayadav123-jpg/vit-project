print("""WELCOME TO MATHS QUIZ, THE AIM OF THE QUIZ IS TO PROVIDE GOOD PRACTICE OF 
ADDITION,SUBTRACTION,MUTLIPLICATION,INTEGRATION AND DIFFERTION,YOU CAN CHOOSE 
ANYONE TOPIC TO STUDY""")
name=str(input("ENTER YOUR NAME:"))#taking input from user 

print("CHOOSE YOUR TOPIC FOR QUIZ:")
print("""1.CHOOSE 1 FOR ADDITION
2.CHOOSE 2 FOR SUBTRACTION                  
3.CHOOSE 3 FOR MUTLIPLICATION
4.CHOOSE 4 FOR DIVISON
5.CHOOSE 5 FOR DIIFERNTION
6.CHOOSE 6 FOR INTEGRATION
PRESS ENTER TO MAKE CHOICE""")  #selecting topic 
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
     ] #question bank of additon 
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
]#subtraction bank of additon 
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
   
]#question bank of multiplication
division = [
    ["""Q) Divide 10 by 2.

  a. 4

  b. 5

  c. 6

  d. 8""", "b"],

    ["""Q) What is the division of 12 by 3?

  a. 3

  b. 4

  c. 5

  d. 6""", "b"],

    ["""Q) What will be the answer of 15 / 3?

  a. 4

  b. 5

  c. 6

  d. 7""", "b"],

    ["""Q) Divide 16 by 4.

  a. 2

  b. 3

  c. 4

  d. 5""", "c"],

    ["""Q) What is 18 divided by 2?

  a. 7

  b. 8

  c. 9

  d. 10""", "c"],

    ["""Q) What will be the result of 20 / 4?

  a. 4

  b. 5

  c. 6

  d. 8""", "b"],

    ["""Q) Divide 21 by 3.

  a. 6

  b. 7

  c. 8

  d. 9""", "b"],

    ["""Q) What is the answer of 24 / 6?

  a. 3

  b. 4

  c. 5

  d. 6""", "b"],

    ["""Q) What will you get when you divide 25 by 5?

  a. 3

  b. 4

  c. 5

  d. 6""", "c"],

    ["""Q) Divide 27 by 3.

  a. 7

  b. 8

  c. 9

  d. 10""", "c"],

    ["""Q) What is the division of 28 by 4?

  a. 5

  b. 6

  c. 7

  d. 8""", "c"],

    ["""Q) What will be the answer of 30 / 5?

  a. 4

  b. 5

  c. 6

  d. 7""", "c"],

    ["""Q) Divide 32 by 4.

  a. 6

  b. 7

  c. 8

  d. 9""", "c"],

    ["""Q) What is 35 divided by 5?

  a. 5

  b. 6

  c. 7

  d. 8""", "c"],

    ["""Q) Find the answer of 36 / 6.

  a. 4

  b. 5

  c. 6

  d. 7""", "c"],

    ["""Q) Divide 40 by 5.

  a. 6

  b. 7

  c. 8

  d. 9""", "c"],

    ["""Q) What is the result of 42 / 6?

  a. 6

  b. 7

  c. 8

  d. 9""", "b"],

    ["""Q) What will be the answer when 45 is divided by 5?

  a. 7

  b. 8

  c. 9

  d. 10""", "c"],

    ["""Q) Divide 48 by 6.

  a. 6

  b. 7

  c. 8

  d. 9""", "c"],

    ["""Q) What is 49 divided by 7?

  a. 5

  b. 6

  c. 7

  d. 8""", "c"],

    ["""Q) What will you get from 50 / 5?

  a. 8

  b. 9

  c. 10

  d. 11""", "c"],

    ["""Q) Divide 54 by 6.

  a. 7

  b. 8

  c. 9

  d. 10""", "c"],

    ["""Q) What is the answer of 56 / 7?

  a. 6

  b. 7

  c. 8

  d. 9""", "c"],

    ["""Q) What will be the result of 60 divided by 6?

  a. 8

  b. 9

  c. 10

  d. 12""", "c"],

    ["""Q) Divide 63 by 7.

  a. 7

  b. 8

  c. 9

  d. 10""", "c"],

    ["""Q) What is 64 / 8?

  a. 6

  b. 7

  c. 8

  d. 9""", "c"],

    ["""Q) Find the answer of 70 divided by 7.

  a. 8

  b. 9

  c. 10

  d. 11""", "c"],

    ["""Q) What is the division of 72 by 8?

  a. 7

  b. 8

  c. 9

  d. 10""", "c"],

    ["""Q) Divide 75 by 5.

  a. 13

  b. 14

  c. 15

  d. 16""", "c"],

    ["""Q) What will be the answer of 80 / 8?

  a. 8

  b. 9

  c. 10

  d. 12""", "c"],

    ["""Q) What is 81 divided by 9?

  a. 7

  b. 8

  c. 9

  d. 10""", "c"],

    ["""Q) Divide 84 by 7.

  a. 10

  b. 11

  c. 12

  d. 13""", "c"],

    ["""Q) What is the result of 90 / 9?

  a. 8

  b. 9

  c. 10

  d. 11""", "c"],

    ["""Q) What will you get when 96 is divided by 8?

  a. 10

  b. 11

  c. 12

  d. 13""", "c"],

    ["""Q) Divide 100 by 10.

  a. 8

  b. 9

  c. 10

  d. 12""", "c"],

    ["""Q) What is 18 / 3?

  a. 5

  b. 6

  c. 7

  d. 8""", "b"],

    ["""Q) Find the answer of 20 divided by 5.

  a. 3

  b. 4

  c. 5

  d. 6""", "b"],

    ["""Q) What will be the result of 24 / 4?

  a. 4

  b. 5

  c. 6

  d. 8""", "c"],

    ["""Q) Divide 27 by 9.

  a. 2

  b. 3

  c. 4

  d. 5""", "b"],

    ["""Q) What is 30 divided by 6?

  a. 4

  b. 5

  c. 6

  d. 7""", "b"],

    ["""Q) What is the answer of 36 / 4?

  a. 7

  b. 8

  c. 9

  d. 10""", "c"],

    ["""Q) Divide 40 by 8.

  a. 4

  b. 5

  c. 6

  d. 7""", "b"],

    ["""Q) What will you get when 42 is divided by 7?

  a. 5

  b. 6

  c. 7

  d. 8""", "b"],

    ["""Q) Find the answer of 45 / 9.

  a. 4

  b. 5

  c. 6

  d. 7""", "b"],

    ["""Q) What is 48 divided by 8?

  a. 5

  b. 6

  c. 7

  d. 8""", "b"],

    ["""Q) Divide 54 by 9.

  a. 5

  b. 6

  c. 7

  d. 8""", "b"],

    ["""Q) What will be the answer of 56 / 8?

  a. 5

  b. 6

  c. 7

  d. 8""", "c"],

    ["""Q) What is the result of 63 divided by 9?

  a. 6

  b. 7

  c. 8

  d. 9""", "b"],

    ["""Q) Divide 64 by 8.

  a. 6

  b. 7

  c. 8

  d. 9""", "c"],

    ["""Q) What is 70 / 10?

  a. 5

  b. 6

  c. 7

  d. 8""", "c"],

    ["""Q) Find the answer of 72 divided by 9.

  a. 6

  b. 7

  c. 8

  d. 9""", "c"],

    ["""Q) What will you get from 80 / 10?

  a. 6

  b. 7

  c. 8

  d. 9""", "c"],

    ["""Q) Divide 84 by 12.

  a. 6

  b. 7

  c. 8

  d. 9""", "b"],

    ["""Q) What is the answer of 90 / 10?

  a. 7

  b. 8

  c. 9

  d. 10""", "c"],

    ["""Q) What will be the result of 96 divided by 12?

  a. 6

  b. 7

  c. 8

  d. 9""", "c"],

    ["""Q) Divide 100 by 5.

  a. 15

  b. 20

  c. 25

  d. 30""", "b"],

    ["""Q) What is 108 / 12?

  a. 7

  b. 8

  c. 9

  d. 10""", "c"],

    ["""Q) Find the answer of 120 divided by 10.

  a. 10

  b. 11

  c. 12

  d. 13""", "c"],

    ["""Q) What will you get when 144 is divided by 12?

  a. 10

  b. 11

  c. 12

  d. 14""", "c"],

    ["""Q) Divide 150 by 10.

  a. 10

  b. 15

  c. 20

  d. 25""", "b"],

    ["""Q) What is the result of 200 / 10?

  a. 10

  b. 15

  c. 20

  d. 25""", "c"]
]#question bank of divison
differntion=[
   ["""Q)  What is the derivative of y = x⁵?

a. 5x⁴

b. x⁴

c. 4x⁵

d. 5x
""","a"],
[""""Q) Find dy/dx if y = 3x⁴ − 5x² + 7x − 9.

a. 12x⁴ − 10x² + 7

b. 3x³ − 5x + 7

c. 12x³ − 10x + 7

d. 12x³ − 5x + 7""","c"],
[""""Q) The derivative of √x is:

a. 1/√x

b. 1/(2√x)

c. √x/2

d. 2√x""","b"],
[""""Q) What is the derivative of 1/x³?

a. 3/x²

b. 1/x⁴

c. −3/x²

d. −3/x⁴""","d"],
[""""Q) Find the derivative of y = 2x⁷ + 4x³ − 6x + 10.

a. 14x⁶ + 12x² − 6

b. 14x⁷ + 12x³ − 6

c. 2x⁶ + 4x² − 6

d. 14x⁶ + 4x² − 6""","a"],
[""""Q) What is d/dx(sin x)?

a. −sin x

b. sin x

c. −cos x

d. cos x""","d"],
[""""Q) Find dy/dx if y = x² sin x.

a. 2x cos x + x² sin x

b. x² cos x

c. 2x sin x + x² cos x

d. 2x sin x""","c"],
[""""Q) What is the derivative of tan x + x³?

a. tan²x + 3x²

b. sec²x + 3x²

c. sec x + 3x

d. cos²x + 3x²""","b"],
[""""Q) Find the derivative of y = sin(x²).

a. cos(x²)

b. 2x sin(x²)

c. cos(2x)

d. 2x cos(x²)""","d"],
[""""Q) Find dy/dx if y = cos(3x + 2).

a. 3cos(3x + 2)

b. −sin(3x + 2)

c. 3sin(3x + 2)

d. −3sin(3x + 2)""","d"],
[""""Q) Differentiate y = x²eˣ.

a. 2xeˣ

b. eˣ(x² − 2x)

c. eˣ(x² + 2x)

d. x²eˣ""","c"],
[ """Q) Find the derivative of y = (x² + 1)(x³ − 2x).

a. 5x⁴ − 6x² − 2

b. 5x⁴ − 3x² − 2

c. 3x⁴ − 2x²

d. 5x⁴ − 2x² + 1
""", "b"],
[""""Q) Find dy/dx if y = (x² + 1)/(x + 1).

a. (x² − 1)/(x + 1)²

b. (2x + 1)/(x + 1)

c. (x² + 2x − 1)/(x + 1)²

d. (x² + 1)/(x + 1)²""","c"],
[""""Q) Find the derivative of y = x³ ln x.

a. 3x³ ln x + x²

b. 3x² ln x + x²

c. 3x² ln x

d. x² ln x + 3x""","b"],
[""""Q) Differentiate y = sin x/x.

a. (x sin x − cos x)/x²

b. cos x/x

c. (sin x − x cos x)/x

d. (x cos x − sin x)/x²""","d",],
[""""Q) Find dy/dx if y = (3x² + 5)⁴.

a. 4(3x² + 5)³

b. 12x(3x² + 5)⁴

c. 24x(3x² + 5)³

d. 24x(3x² + 5)⁴""","c"],
[""""Q) Find the derivative of y = √(1 + x²).

a. x/√(1 + x²)

b. 2x/√(1 + x²)

c. 1/√(1 + x²)

d. √(1 + x²)/x""","a"],
[""""Q) Find dy/dx if y = e^(x² + 3x).

a. 2xe^(x² + 3x)

b. (2x + 3)e^(x² + 3x)

c. e^(2x + 3)

d. (x² + 3)e^(x² + 3x)""","b"],
[""""Q) Find the second derivative of y = x⁴ − 3x³ + 2x² − 5x + 1.

a. 12x³ − 18x² + 4 

b. 4x³ − 9x² + 4x − 5

c. 12x² − 9x + 4

d. 12x² − 18x + 4""","d"],
[""""Q) If y = x³ − 6x² + 9x + 2, which are the critical points?

a. x = 2 and x = 3

b. x = 1 and x = 3

c. x = 1 and x = 2

d. x = 0 and x = 3""","a"]
]#question bank of differnation
integration = [

    ["""Q) What is ∫ x⁵ dx?

a. x⁶/6 + C

b. 5x⁴ + C

c. x⁵/5 + C

d. 6x⁶ + C
""", "a"],

    ["""Q) What is ∫ 3x² dx?

a. 3x³ + C

b. x³ + C

c. 6x + C

d. x² + C
""", "b"],

    ["""Q) What is ∫ 1/x dx?

a. 1/x² + C

b. x + C

c. ln|x| + C

d. −1/x² + C
""", "c"],

    ["""Q) What is ∫ √x dx?

a. (2/3)x^(3/2) + C

b. (1/2)x^(1/2) + C

c. x²/2 + C

d. 2x^(3/2) + C
""", "a"],

    ["""Q) What is ∫ (4x³ − 2x + 5) dx?

a. 12x² − 2 + C

b. x⁴ − x² + 5x + C

c. 4x⁴ − x² + 5x + C

d. x⁴ − 2x² + 5x + C
""", "b"],

    ["""Q) What is ∫ sin x dx?

a. cos x + C

b. −sin x + C

c. −cos x + C

d. sin x + C
""", "c"],

    ["""Q) What is ∫ cos x dx?

a. sin x + C

b. −sin x + C

c. cos x + C

d. −cos x + C
""", "a"],

    ["""Q) What is ∫ sec²x dx?

a. tan²x + C

b. sec x + C

c. cot x + C

d. tan x + C
""", "d"],

    ["""Q) What is ∫ eˣ dx?

a. xeˣ + C

b. eˣ + C

c. eˣ/x + C

d. ln(eˣ) + C
""", "b"],

    ["""Q) What is ∫ 2e^(2x) dx?

a. e^(2x) + C

b. 2e^(2x) + C

c. 4e^(2x) + C

d. e^(2x)/2 + C
""", "a"],

    ["""Q) What is ∫ (2x + 1)⁵ dx?

a. 5(2x + 1)⁴ + C

b. (2x + 1)⁶/6 + C

c. (2x + 1)⁶/12 + C

d. (2x + 1)⁵/5 + C
""", "c"],

    ["""Q) What is ∫ x cos(x²) dx?

a. sin(x²) + C

b. (1/2)sin(x²) + C

c. cos(x²) + C

d. x² sin(x²) + C
""", "b"],

    ["""Q) What is ∫ 1/(1 + x²) dx?

a. tan⁻¹x + C

b. sin⁻¹x + C

c. ln(1 + x²) + C

d. 1/(1 + x²) + C
""", "a"],

    ["""Q) What is ∫ 1/√(1 − x²) dx?

a. tan⁻¹x + C

b. cos⁻¹x + C

c. sin⁻¹x + C

d. √(1 − x²) + C
""", "c"],

    ["""Q) Using integration by parts, what is ∫ x eˣ dx?

a. xeˣ + C

b. eˣ(x − 1) + C

c. eˣ(x + 1) + C

d. x²eˣ/2 + C
""", "b"],

    ["""Q) What is ∫ ln x dx?

a. x ln x − x + C

b. ln(x²)/2 + C

c. x ln x + x + C

d. 1/x + C
""", "a"],

    ["""Q) What is ∫ 1/(x + 3) dx?

a. 1/(x + 3)² + C

b. ln|x| + 3 + C

c. ln|x + 3| + C

d. x + 3 + C
""", "c"],

    ["""Q) What is ∫ (3x²)/(x³ + 1) dx?

a. ln|x³ + 1| + C

b. 3ln|x³ + 1| + C

c. 1/(x³ + 1) + C

d. x³/(x³ + 1) + C
""", "a"],

    ["""Q) What is ∫ x/(x² + 4) dx?

a. ln|x² + 4| + C

b. (1/2)ln|x² + 4| + C

c. 1/(x² + 4) + C

d. tan⁻¹(x/2) + C
""", "b"],

    ["""Q) What is ∫₀¹ x² dx?

a. 1/2

b. 1/4

c. 2/3

d. 1/3
""", "d"]

]#question bank of integration

 



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
          random.shuffle(division)
      
          correct = 0
          incorrect = 0
          total_questions = 0
      
          print("QUIZ")
          print("The quiz will end after 3 incorrect answers.\n")
      
          for  div in division:
      
            # Stop if 3 answers are incorrect
            if incorrect == 3:
              break
         
            print(div[0])
      
            answer = input("Your answer: ")
      
            total_questions += 1
      
            if answer.lower() ==div[1].lower():
              print("Correct!\n")
              correct += 1
            else:
              print("Incorrect!")
              print("Correct answer:", div[1])
              print()
              incorrect += 1
elif choice==5:
            random.shuffle(differntion)
        
            correct = 0
            incorrect = 0
            total_questions = 0
        
            print("QUIZ")
            print("The quiz will end after 3 incorrect answers.\n")
        
            for  diff in differntion:
        
              # Stop if 3 answers are incorrect
              if incorrect == 3:
                break
           
              print(diff[0])
        
              answer = input("Your answer: ")
        
              total_questions += 1
        
              if answer.lower() ==diff[1].lower():
                print("Correct!\n")
                correct += 1
              else:
                print("Incorrect!")
                print("Correct answer:", diff[1])
                print()
                incorrect += 1
else :
                 random.shuffle(integration)
             
                 correct = 0
                 incorrect = 0
                 total_questions = 0
             
                 print("QUIZ")
                 print("The quiz will end after 3 incorrect answers.\n")
             
                 for  ind in integration:
             
                   # Stop if 3 answers are incorrect
                   if incorrect == 3:
                     break
                
                   print(ind[0])
             
                   answer = input("Your answer: ")
             
                   total_questions += 1
             
                   if answer.lower() ==ind[1].lower():
                     print("Correct!\n")
                     correct += 1
                   else:
                     print("Incorrect!")
                     print("Correct answer:", ind[1])
                     print()
                     incorrect += 1
#displaying result
print("NAME:",name)
print("QUIZ RESULT")
print("Total questions attempted:", total_questions)
print("Correct answers:", correct)
print("Incorrect answers:", incorrect)


