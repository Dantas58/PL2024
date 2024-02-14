
# id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado

def csv_parser(file_path):
    dic = {}
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        lines.pop(0)  
        for line in lines:
            values = line.split(',')
            dic[values[0]] = tuple(values[1:])
    return dic

def order_modalidades(dic):
    modalidades = []
    for id in dic:
        if dic[id][7] not in modalidades:
            modalidades.append(dic[id][7])
    modalidades.sort()
    return modalidades

def athlete_percentage(dic):

    yes = 0;
    no = 0;
    for id in dic:
        if dic[id][11] == 'true':
            yes += 1
        else:
            no += 1
    return (yes/(yes+no))*100

def age_groups(dic):

    age_groups = {i: 0 for i in range(0, 56, 5)}

    for id in dic:
        age = int(dic[id][4])

        for i in range(0, 56, 5):
            if i <= age < i + 5:
                age_groups[i] += 1

    return age_groups


def print_age_groups(dic):

    groups = age_groups(dic)
    for age, count in sorted(groups.items()):
        print(f'Age {age}-{age+4}: {count}')


infos = csv_parser('emd.csv')
print(order_modalidades(infos))
valid_athletes = athlete_percentage(infos)
print(f"Valid Athletes: {valid_athletes}%")
print(f"Invalid Athletes: {100 - valid_athletes}%")
print_age_groups(infos)
