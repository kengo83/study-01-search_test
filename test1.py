import csv

# CSVファイルを作成⇨書き込む
with open('test.csv', 'w',encoding='utf_8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['たんじろう','ねずこ','ぎゆう','いのすけ','ぜんいつ','れんごく'])
    