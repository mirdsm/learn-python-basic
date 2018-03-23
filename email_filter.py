
import string
import re
null =[]
def fun(s):
    number_filter= list(range(9))
    letter_filter = list(string.ascii_lowercase) or list(string.ascii_lowercase)
    dashscore_filter =['-','_']
    all_filter = number_filter + letter_filter + dashscore_filter
    temp_mails = emails
    for email_acc in temp_mails:
        temp = re.sub('(?!^)(@)', r'', email_acc.split()
        hasil =list(filter(lambda x: x = letter_filter and number_filter and dashscore_filter, temp[0]))
        if hasil == null:
            sec_temp = re.split('(?<!\d)[,.]|[,.](?!\d)', temp[1])
            if
        else:
            del emails[0]













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
