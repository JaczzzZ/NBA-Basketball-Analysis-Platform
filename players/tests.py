import csv


def read_players_label():
    info_path = r'E:\basketball\file\Player Per Game.csv'
    cnt = 0
    pre = -1
    names = []
    with open(info_path, 'r') as cf:
        csvreader = csv.reader(cf)
        header = True
        for row in csvreader:
            if header:
                header = False
                continue
            if pre != int(row[2]):
                pre = int(row[2])
                names.append({
                    'id': cnt + 1,
                    'name': row[3]
                })
            cnt += 1
    names.append({
        'id': 50000
    })
    path = r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\中锋\空间策应中锋(Spatial Center)\data_spatial_center.csv'
    with open(info_path, 'r') as cf:
        csvreader = csv.reader(cf)
        header = True
        for row in csvreader:
            if header:
                header = False
                continue
            print(row[3], names[int(row[0])]['id'], names[int(row[0]) + 1]['id'])
            player = player.objects.filter(pk__gte=names[int(row[0])]['id'], pk__lt=names[int(row[0]) + 1]['id'])
            for p in player:
                p.label = row[3]
                p.save()


read_players_label()
