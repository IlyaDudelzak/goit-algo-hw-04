def total_salary(path):
  try:
    with open(path, 'r') as fh:
      total_salary = 0
      salaries = []
      names = []
      lines = fh.readlines()
      for line in lines:
        line = line.strip()
        l = line.split(',')
        names.append(l[0])
        salaries.append(float(l[1]))
        total_salary += float(l[1])

      average_salary = total_salary / len(salaries)

      return (total_salary, average_salary)

  except FileNotFoundError:
    print("Файл не найден")
    return (0, 0)

  except ValueError:
    print("Файл поврежден")
    return (0, 0)

  except ZeroDivisionError:
    print("Файл не содержит зарплат")
    return (0, 0)

total, average = total_salary("salary_file.txt")
if(total != 0 and average != 0):
  print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")