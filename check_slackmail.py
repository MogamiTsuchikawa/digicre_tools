import os,sys,csv
with open(sys.argv[1],'r',encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        tmp = row[1].split('@')
        if tmp[1] != 'shibaura-it.ac.jp' and row[2] == 'メンバー':
            print(row[1])