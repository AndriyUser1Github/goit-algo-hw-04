
from pathlib import Path

path = Path(input("Введіть рядок-адресу потрібного файлу: "))

def get_cats_info(path):
    """
    функція читає файл та повертає список зі 
    словників з інформацією про кожного кота
    """

    lst_dcts_cats = []
    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.readlines()
        for line in lines:
            line = "".join(line.split("\n"))
            line = line.split(",")
            lst_dcts_cats.append({"id": line[0], "name": line[1], "age": line[2]})
        return lst_dcts_cats
    
cat_info = get_cats_info(path)
print(cat_info)






