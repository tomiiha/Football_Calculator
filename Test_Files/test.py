team_list = ['Carlisle United','Northampton']
index_list = []
foul_list = []
corner_list = []
cross_list = []
touch_list = []
clearance_list = []
offside_list = []
goal_kick_list = []
throw_in_list = []
long_ball_list = []
removal = team_list[0] + team_list[1]
extra_stats_dict = {"Fouls":foul_list,"Corners":corner_list,"Crosses":cross_list,"Touches":touch_list,"Clearances":clearance_list,"Offsides":offside_list,"Goal Kicks":goal_kick_list,"Throw Ins":throw_in_list,"Long Balls":long_ball_list}
text = '\n\nCarlisle United\xa0Northampton\n21Fouls12\n4Corners2\n10Crosses7\n83Touches101\n\n\nCarlisle United\xa0Northampton\n1Clearances1\n\n\nCarlisle United\xa0Northampton\n10Goal Kicks12\n16Throw Ins18\n15Long Balls17\n\n'
text = text.replace(u'\xa0', u'')
text = text.split('\n')
text = list(filter(None, text))
while removal in text:
    text.remove(removal)

for key in extra_stats_dict:
    for val in text:
        if key in val:
            stat_home = val[:val.find(key)]
            stat_away = val[(val.find(key) + len(key)):]
            extra_stats_dict[key].append(int(stat_home))
            extra_stats_dict[key].append(int(stat_away))

# Not all statistics are in place for all games
# Below to check all lists, and apply 0 to unpopulated statistics 
for y, x in extra_stats_dict.items():
    if len(x) == 0:
        x.append(0)
        x.append(0)

print(foul_list)
print(corner_list)
print(cross_list)
print(touch_list)
print(clearance_list)
print(offside_list)
print(goal_kick_list)
print(throw_in_list)
print(long_ball_list)
