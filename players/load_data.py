# python manage.py shell
# from players import load_data
# load_data.read_players_from_file(r'E:\basketball\file\Player Per Game.csv')
# load_data.read_teams_from_file(r'E:\basketball\file\Team Stats Per Game.csv')
# E:\basketball\file\Team Stats Per Game.csv
from .models import *
import csv


def nullNA(val):
    return val if val != 'NA' else None


def read_players_from_file(path):
    cnt = 0
    with open(path, 'r') as cf:
        csvreader = csv.reader(cf)
        header = True
        for row in csvreader:
            if header:
                header = False
                continue
            cnt += 1
            if cnt % 100 == 0:
                print(cnt)
            player = Player(
                seas_id=row[0],
                season=row[1],
                player_id=row[2],
                name=row[3],
                birth_year=row[4] if row[4] != 'NA' else None,
                pos=row[5],
                age=nullNA(row[6]),
                experience=row[7],
                lg=row[8],
                tm=row[9],
                g=nullNA(row[10]),
                gs=nullNA(row[11]),
                mp_per_game=nullNA(row[12]),
                fg_per_game=nullNA(row[13]),
                fga_per_game=nullNA(row[14]),
                fg_percent=nullNA(row[15]),
                x3p_per_game=nullNA(row[16]),
                x3pa_per_game=nullNA(row[17]),
                x3p_percent=nullNA(row[18]),
                x2p_per_game=nullNA(row[19]),
                x2pa_per_game=nullNA(row[20]),
                x2p_percent=nullNA(row[21]),
                e_fg_percent=nullNA(row[22]),
                ft_per_game=nullNA(row[23]),
                fta_per_game=nullNA(row[24]),
                ft_percent=nullNA(row[25]),
                orb_per_game=nullNA(row[26]),
                drb_per_game=nullNA(row[27]),
                trb_per_game=nullNA(row[28]),
                ast_per_game=nullNA(row[29]),
                stl_per_game=nullNA(row[30]),
                blk_per_game=nullNA(row[31]),
                tov_per_game=nullNA(row[32]),
                pf_per_game=nullNA(row[33]),
                pts_per_game=nullNA(row[34])
            )
            player.save()


def read_teams_from_file(path):
    cnt = 0
    with open(path, 'r') as cf:
        csvreader = csv.reader(cf)
        header = True
        for row in csvreader:
            if header:
                header = False
                continue
            cnt += 1
            if cnt % 100 == 0:
                print(cnt)
            team = Team(
                season=row[0],
                lg=row[1],
                name=row[2],
                abbreviation=row[3],
                playoffs=row[4] == 'TRUE',
                g=nullNA(row[5]),
                mp_per_game=nullNA(row[6]),
                fg_per_game=nullNA(row[7]),
                fga_per_game=nullNA(row[8]),
                fg_percent=nullNA(row[9]),
                x3p_per_game=nullNA(row[10]),
                x3pa_per_game=nullNA(row[11]),
                x3p_percent=nullNA(row[12]),
                x2p_per_game=nullNA(row[13]),
                x2pa_per_game=nullNA(row[14]),
                x2p_percent=nullNA(row[15]),
                ft_per_game=nullNA(row[16]),
                fta_per_game=nullNA(row[17]),
                ft_percent=nullNA(row[18]),
                orb_per_game=nullNA(row[19]),
                drb_per_game=nullNA(row[20]),
                trb_per_game=nullNA(row[21]),
                ast_per_game=nullNA(row[22]),
                stl_per_game=nullNA(row[23]),
                blk_per_game=nullNA(row[24]),
                tov_per_game=nullNA(row[25]),
                pf_per_game=nullNA(row[26]),
                pts_per_game=nullNA(row[27])
            )
            team.save()


def read_game_from_file(ml, path):
    cnt = 0
    with open(path, 'r') as cf:
        csvreader = csv.reader(cf)
        header = True
        for row in csvreader:
            if header:
                header = False
                continue
            cnt += 1
            if cnt % 100 == 0:
                print(cnt)
            game = Game(
                visit_team=row[0],
                visit_win=row[1],
                home_team=row[2],
                home_win=row[3],
                pred_model=ml
            )
            game.save()


def read_games():
    games = Game.objects.all()
    for game in games:
        game.delete()
    read_game_from_file('DT', r'E:\basketball\file\predict\prediction of 2020-2021_DT.csv')
    read_game_from_file('LogisticRegression', r'E:\basketball\file\predict\prediction of 2020-2021_LogisticRegression.csv')
    read_game_from_file('RND', r'E:\basketball\file\predict\prediction of 2020-2021_RND.csv')

names = []

def read_labels_from_file(path):
    global names
    with open(path, 'r') as cf:
        csvreader = csv.reader(cf)
        header = True
        for row in csvreader:
            if header:
                header = False
                continue
            print(row[0], names[int(row[0])]['id'], names[int(row[0]) + 1]['id'])
            player = Player.objects.filter(pk__gte=names[int(row[0])]['id'], pk__lt=names[int(row[0]) + 1]['id'])
            for p in player:
                p.label = row[3]
                p.save()


def read_players_label():
    info_path = r'E:\basketball\file\Player Per Game.csv'
    cnt = 0
    pre = -1
    global names
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
    read_labels_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\中锋\空间策应中锋(Spatial Center)\data_spatial_center.csv')
    read_labels_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\前锋\全能前锋(Almighty_Forwards)\data_Almighty_Fowards.csv')
    read_labels_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\前锋\内线锋位摇摆人(Inside Forward Swingman)\data_Inside_Forward_Swingman.csv')
    read_labels_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\前锋\外线锋位摇摆人(Outside Forward Swingman)\data_Outside_Forward_Swingman.csv')
    read_labels_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\后卫\3D后卫(3D Guards)\data_3DGuards.csv')
    read_labels_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\后卫\三分型后卫(3P Shooter Guards)\data_3Pshooter.csv')
    read_labels_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\后卫\终结性后卫(Terminated Guards)\data_terminated_gurads(2P, 2P%).csv')


def load_label_from_file(path, pos):
    with open(path, 'r') as cf:
        csvreader = csv.reader(cf)
        header = True
        for row in csvreader:
            if header:
                header = False
                continue
            label = Label(v0=row[1], v1=row[2], label=row[3], name=row[4], pos=pos)
            label.save()
    

def load_label():
    load_label_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\中锋\空间策应中锋(Spatial Center)\data_spatial_center.csv', 'Spatial Center')
    load_label_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\前锋\全能前锋(Almighty_Forwards)\data_Almighty_Fowards.csv', 'Almighty_Forwards')
    load_label_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\前锋\内线锋位摇摆人(Inside Forward Swingman)\data_Inside_Forward_Swingman.csv', 'Inside Forward Swingman')
    load_label_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\前锋\外线锋位摇摆人(Outside Forward Swingman)\data_Outside_Forward_Swingman.csv', 'Outside Forward Swingman')
    load_label_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\后卫\3D后卫(3D Guards)\data_3DGuards.csv', '3D Guards')
    load_label_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\后卫\三分型后卫(3P Shooter Guards)\data_3Pshooter.csv', '3P Shooter Guards')
    load_label_from_file(r'E:\basketball\file\divide\2D聚类结果(2D Clustering Result)\后卫\终结性后卫(Terminated Guards)\data_terminated_gurads(2P, 2P%).csv', 'Terminated Guards')