

list_meeting_time = [(0, 1),(0,1), (3, 5), (4, 8), (10, 12), (9, 10)]
slot_time =[]
schedule = []
class first_try():
    def __init__(self):

        for i in range(0,13):
            slot_time.append(i)
            i = i + 0.5
            slot_time.append(i)
        print "slot\n",slot_time

         #return slot_time
         #print slot_time
    def to_deret(self):

        #schedule = self.schedule
        for item in list_meeting_time:
            #temp=[]
            for i in range(item[0],item[1]+1):
                schedule.append(i)
                i = i + 0.5
                schedule.append(i)
        print "sche\n",schedule
        print '-'*6


    def deletion(self):
        r =0
        for number_schedule in slot_time:
            i = 0

            for number_schedule_2 in schedule:

                if number_schedule == number_schedule_2:
                    del slot_time[r]
                else:
                    i = i + 1
                    #print i
                    if i == 33:
                        r= r + 1
                        print r
                    else:
                        pass


                #print i

        print "--", slot_time


first_step = first_try()
first_step.to_deret()
first_step.deletion()
