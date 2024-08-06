def total_salary(path):
  with open(path, 'r') as fh:
    total_salary = 0
    salaries = []
    names = []
    lines = fh.readlines()
    for line in lines:
      line = line.strip()
      l = line.split(',')
      names.append(l[0])
      salaries.append(int(l[1]))
      total_salary += int(l[1])

    average_salary = int(total_salary / len(salaries))

    return (total_salary, average_salary)


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")