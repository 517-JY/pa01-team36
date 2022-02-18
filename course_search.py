'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''
# import sys
# import sched
# This is for pa01
from schedule import Schedule

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
coursenum (filter by course number, e.g. 21A, 221B, 103A)
lastname (filter by instructor lastname, e.g. hickey)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
            '''Zhiwei's 7a/7b/7e code starts from here'''
        elif command in ['course']:
            course = input("enter course number, for example, COSI 12B,"+
            "make sure there is a space between subject and course code: ")
            schedule = schedule.ZhiweiHu_course(course)
        elif command in ['instructor']:
            sub_command = input("filter by email or lastname?")
            if sub_command == 'email':
                email = input("enter the instructor's email")
                schedule = schedule.email([email])
            elif sub_command == 'lastname':
                lastname = input("enter the instructor's lastname")
                schedule = schedule.lastname([lastname])
        elif command in ['small class', 'smallclass', 'small_class', 'smallClass']:
            schedule = schedule.ZhiweiHu_own_filter_small_class().ZhiweiHu_own_filter_sort()
            '''Zhiwei's 7a/7b/7e code ends here'''
        elif command in ['zhengchu']:
            weekday= input("enter a weekday:")
            schedule=schedule.weekday_zhengchu(weekday)
#         elif command in ['cnum', 'coursenum']:
#             coursenum = input("enter a course number:")
#             schedule = schedule.coursenum([coursenum])
#         elif command in ['e', 'email']:
#             email = input("enter an email:")
#             schedule = schedule.email([email])
#         elif command in ['ln', 'lastname']:
#             lastname = input("enter a lastname:")
#             schedule = schedule.lastname([lastname])
        elif command in ['tt', 'title']:
            title = input("enter a phrash in course titles: ")
            schedule = schedule.title(title)
        elif command in ['p', 'phrase']:
            phrase = input("enter a phrase in course description: ")
            schedule = schedule.phrase(phrase)
        elif command in ['jingnu', 'ja']:
            status = input("enter course status (o for open, c for closed): ")
            if status == 'o':
                schedule = schedule.jingnu_status('open')
            elif status == 'c':
                schedule = schedule.jingnu_status('closed')
        ''' Bohan's slight change of code'''
        elif command in ['bohan']:
            day = input("enter a day ")
            schedule = schedule.bohan_day(day)
        elif command in ['title2']:
            title2 = input("enter a phrase:")
            schedule = schedule.title2(title2)
        elif command in ['description2']:
            description2 = input("enter a phrase:")
            schedule = schedule.description2(description2)
        elif command in ['notday']:
            notday = input("enter a busy day:")
            schedule = schedule.notday(notday)
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()
