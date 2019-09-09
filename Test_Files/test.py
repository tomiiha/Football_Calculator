team_list = ['Carlisle United','Northampton']
index_list = []
removal = team_list[0] + team_list[1]
extra_stats = ["Fouls","Corners","Crosses","Touches","Clearances","Offsides","Goal Kicks","Throw Ins","Long Balls"]
text = '\n\nCarlisle United\xa0Northampton\n21Fouls12\n4Corners2\n10Crosses7\n83Touches101\n\n\nCarlisle United\xa0Northampton\n1Clearances1\n\n\nCarlisle United\xa0Northampton\n10Goal Kicks12\n16Throw Ins18\n15Long Balls17\n\n'
text = text.replace(u'\xa0', u'')
text = text.split('\n')
text = list(filter(None, text))
while removal in text:
    text.remove(removal)
