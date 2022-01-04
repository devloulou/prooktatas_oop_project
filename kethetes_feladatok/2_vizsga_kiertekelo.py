# Egyetemi féléves értékelő: írjatok egy olyan programot - függvények segíségével - ,
# amely az alábbi tanulók féléves jegyét meghatározza.
# Az értékelésnél a következő szabályokat kell betartani:

## a beadando a jegy 10%-át adja
## a vizsga a jegy 70%-át
## a labor gyakorlat pedig a jegy 20%-át

# Az eredmények a következők szerint kell meghatározni
# 90 - 100 => 5
# 80 - 89 => 4
# 70 - 79 => 3
# 60 - 69 => 2
# 0  - 59 => 1

# példa az elvárt eredményre:
#
#
kriszta = { "tanulo":"Kriszta",
         "beadando" : [70, 60, 30, 10],
         "vizsga" : [70, 75],
         "labor" : [68.20, 77.20]
       }
# (ez egy lekalkulált eredmény)
# Kriszta
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# Kriszta átlag pontszáma: 69.54
# Kriszta tanuló eredménye: 2

# 2. feladat: az osztály átlag eredményeit is határozzátok meg:
# példa outputra:
#
# Osztály átlag pontszáma 72.79
# Osztály eredménye 3


karcsi = { "tanulo":"Horváth Károly",
         "beadando" : [80, 50, 40, 20],
         "vizsga" : [75, 75],
         "labor" : [78.20, 77.20]
       }


jani = { "tanulo":"Potter János",
          "beadando" : [82, 56, 44, 30],
          "vizsga" : [80, 80],
          "labor" : [67.90, 78.72]
        }


denes = { "tanulo" : "Neumann Dénes",
          "beadando" : [77, 82, 23, 39],
          "vizsga" : [78, 77],
          "labor" : [80, 80]
        }


emese = { "tanulo" : "Morvai Emese",
         "beadando" : [67, 55, 77, 21],
         "vizsga" : [40, 50],
         "labor" : [69, 44.56]
       }


tomi = { "tanulo" : "Kiss Tamás",
        "beadando" : [29, 89, 60, 56],
        "vizsga" : [65, 56],
        "labor" : [50, 40.6]
      }

students = [karcsi, jani, denes, emese, tomi]

def generate_student_points(student):
	## a beadando a jegy 10%-át adja
	## a vizsga a jegy 70%-át
	## a labor gyakorlat pedig a jegy 20%-át

	beadando_avg = sum(student['beadando'])/len(student['beadando'])
	vizsga_avg = sum(student['vizsga'])/len(student['vizsga'])
	labor_avg = sum(student['labor'])/len(student['labor'])

	return beadando_avg*0.1+vizsga_avg*0.7+labor_avg*0.2

def generate_grade(point):
	# 90 - 100 => 5
	# 80 - 89 => 4
	# 70 - 79 => 3
	# 60 - 69 => 2
	# 0  - 59 => 1

	if point >= 0 and point <60:
		return 1
	if point >= 60 and point <70:
		return 2
	if point >= 70 and point <80:
		return 3
	if point >= 80 and point <90:
		return 4
	if point >= 90:
		return 5



print(generate_student_points(kriszta))
print(generate_grade(generate_student_points(kriszta)))

# Kriszta
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# Kriszta átlag pontszáma: 69.54
# Kriszta tanuló eredménye: 2


# Osztály átlag pontszáma 72.79
# Osztály eredménye 3

def generate_grades():
	import math
	points = []
	grades = []
	for student in students:
		point = generate_student_points(student)
		grade = generate_grade(point)

		print(student['tanulo'])
		print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
		print(f"{student['tanulo']} átlag pontszáma: {point}")
		print(f"{student['tanulo']} tanuló eredménye: {grade}")

		points.append(point)
		grades.append(grade)
	
	print()
	print(points)
	print(grades)
	
	print(f"Osztály átlag pontszáma: {sum(points)/len(points)}")
	print(f"Osztály átlag pontszáma: {sum(grades)/len(grades)}")
	print(f"Osztály átlag pontszáma: {int((sum(grades)/len(grades)))}")

generate_grades()