def get_cats_info(path):
  with open(path, 'r') as fh:
    infos = []
    lines = fh.readlines()
    for line in lines:
      line = line.strip()
      l = line.split(',')
      infos.append({"id":l[0], "name":l[1], "age":l[2]})

    return infos

cats_info = get_cats_info("cats_file.txt")
print(cats_info)