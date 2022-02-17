'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''
import sys
import sched
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
        elif command in ['coursenum','subject']:
            if command == 'coursenum':
                coursenum = input("enter the course number:")
                schedule = schedule.ZhiweiHu_coursenum([coursenum])
            else:
                subject = input("enter the course subject")
                schedule = schedule.subject([subject])
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

