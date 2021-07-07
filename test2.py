import csv

# CSVファイルを読み込む
def search():
    with open('test.csv', 'r',encoding='utf_8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            source = row
            print(source)
    word = input('鬼滅の登場人物の名前を入力して下さい：')
    if word in source:
        print(word + 'はsourceの中に存在します')
    else:
        print(word + 'はsourceの中に存在しません')
        add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        if add_flg=="1":
            source.append(word)
        with open('test.csv', 'w', newline='',encoding='utf_8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(source)
            print(source)
    
search()



        

           
            


