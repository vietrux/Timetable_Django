from tkb.models import Day                
day1 = Day(day_name='Thứ 3', day_subj='vatly')
day3 = Day(day_name='Thứ 3', day_subj='congnghe')
day3 = Day(day_name='Thứ 3', day_subj='qpan')
day4 = Day(day_name='Thứ 3', day_subj='nguvan')
day5 = Day(day_name='Thứ 3', day_subj='nguvan')
day_list = [ day2, day3, day4, day5]
for x in day_list:
    x.save()