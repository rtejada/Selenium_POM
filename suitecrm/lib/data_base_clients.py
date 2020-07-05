import csv
file = open('pruebas-realizados-coronavirus.csv')
content = csv.reader(file, delimiter=';')
tests_list = list(content)
file.close()