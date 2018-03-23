


import re
def fun(s):
    #emails = False
    temp_mails = emails
    for word in temp_mails:
        temp = re.sub('(?!^)(@)', r'', word.split()
        if map(lambda x:x.isalpha(), temp[0]) or map(lambda x:x.list(range(10)), temp[0]) or map(lambda x:x.list(["-","_"], temp[0]) == True:
            if map(lambda x:x.isalpha(), temp[1]) or map(lambda x:x.list(range(10)), temp[0]) == True:
                sec_temp = re.split('(?<!\d)[,.]|[,.](?!\d)', temp[1])
                if len(sec_temp[1]) <= 3:
                    None
                else:
                    emails = del emails[0]
            else:
                emails = del emails[0]
        else:
            emails = del emails[0]



def filter_mail(emails):
    return filter(fun, emails)

if __name__ == "__main__":
    n = int(raw_input())
    emails= []
    for _ in range(n):
        emails.append(raw_input())
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
