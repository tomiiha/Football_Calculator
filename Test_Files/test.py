team_list = ['Carlisle United','Northampton']
index_list = []
foul_list = []
corner_list = []
cross_list = []
touch_list = []
offside_list = []
goal_kick_list = []
throw_in_list = []
long_ball_list = []
removal = team_list[0] + team_list[1]
extra_stats = ["Fouls","Corners","Crosses","Touches","Offsides","Goal Kicks","Throw Ins","Long Balls"]
list_list = [foul_list,corner_list,cross_list,touch_list,offside_list,goal_kick_list,throw_in_list,long_ball_list]
text = '\n\nCarlisle United\xa0Northampton\n21Fouls12\n4Corners2\n10Tomi6\n10Crosses7\n83Touches101\n\n\nCarlisle United\xa0Northampton\n1Clearances1\n\n\nCarlisle United\xa0Northampton\n10Goal Kicks12\n16Throw Ins18\n15Long Balls17\n\n'
text = text.replace(u'\xa0', u'')
text = text.split('\n')
text = list(filter(None, text))
while removal in text:
    text.remove(removal)

text_picker = 0
list_picker = 0
for stat in extra_stats:
    for piece in text:
        if stat in piece:
            stat_gen = piece
            stat_home = piece[:piece.find(stat)]
        else:
            text_picker = text_picker + 1
            list_picker = list_picker + 1

print(foul_list)
print(corner_list)
