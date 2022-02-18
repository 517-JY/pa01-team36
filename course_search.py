'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

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
        elif command in ['cnum', 'coursenum']:
            coursenum = input("enter a course number:")
            schedule = schedule.coursenum([coursenum])
        elif command in ['e', 'email']:
            email = input("enter an email:")
            schedule = schedule.email([email])
        elif command in ['ln', 'lastname']:
            lastname = input("enter a lastname:")
            schedule = schedule.lastname([lastname])
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
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''print_course prints a brief description of the course '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()
