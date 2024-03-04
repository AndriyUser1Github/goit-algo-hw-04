
from pathlib import Path

path = Path(input("Введіть рядок-адресу потрібного файлу: "))

def total_salary(path):
    """
    функція читає файл, обчислює та 
    повертає загальну суму заробітної платні 
    та середню заробітню платню всіх робітників
    """

    lst_sum = []
    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.readlines()
        for line in lines:
            line = "".join(line.split("\n"))
            line = line.split(",")
            lst_sum.append(int(line[1]))
    
    total = sum(lst_sum)
    averange = total / len(lst_sum)
    tpl_sum = (total, averange)
    return tpl_sum

total, averange = total_salary(path)   
print(f"Загальна сума заробітної платні: {total}\nСередня заробітня платня: {averange}")
