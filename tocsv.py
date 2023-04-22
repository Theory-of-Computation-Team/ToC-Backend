import csv
from getTemple import getTem


def write_temple_to_csv(province):
    lit = getTem(province)
    with open('list_temple.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for name in lit:
            writer.writerow([province, name])


if __name__ == '__main__':
    provinces = ['PrachinBuri', 'prayao', 'pattani', 'Ayutthaya']
    with open('list_temple.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Province', 'Temple'])
    for province in provinces:
        write_temple_to_csv(province)
