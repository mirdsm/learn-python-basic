list_time = [(1,2),(2,4),(3,5),(6,7),(8,10)]

list_meeting_time = [(0, 1),(0,1), (3, 5), (4, 8), (10, 12), (9, 10)]



class first_try():
    def __init__(self):
        slot_time =[]
        for i in range(0,13):
            i = i + 0.5
            slot_time.append(i)
        return slot_time
         #return slot_time
         #print slot_time
    def to_deret(self):
        schedule = []
        for item in list_meeting_time:
            #temp=[]
            for i in range(item[0],item[1]+1):
                i = i + 0.5
                schedule.append(i)
        return schedule

class second_try(first_try):
    def deletion(self):
        for number_schedule in schedule:
            for number_schedule_2 in slot_time:
                if number_schedule == number_schedule:
                    pass
                else:
                    print number_schedule


secod_step =second_try()
first_step = first_try()
secod_step.deletion()
#first_step.to_deret()
