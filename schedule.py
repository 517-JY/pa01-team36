'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        stripped = [name.strip().lower() for name in names]
        print('\n** Requested lastname: ', stripped, '\n')
        return Schedule([course for course in self.courses if course['instructor'][1].lower() in stripped])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        stripped = [email.strip().lower() for email in emails]
        print('\n** Requested Email: ', stripped, '\n')
        return Schedule([course for course in self.courses if course['instructor'][2] in stripped])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        print('** Email jingnuan@brandeis.edu if you have questions about this command :)')
        upper_case = [s.upper() for s in subjects]
        print('\n** Requested Key Words: ', upper_case, '\n')
        return Schedule([course for course in self.courses if course['subject'] in upper_case])

    def sort(self,field):
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        else:
            print("can't sort by "+str(field)+" yet")
            return self
        
    def coursenum(self, coursenums):
        ''' coursenum filters the courses by course number '''
        upper_coursenum = [c.upper() for c in coursenums]
        print('\n** Requested Course Numbers: ', upper_coursenum, '\n')
        return Schedule([course for course in self.courses if course['coursenum'] in upper_coursenum])
    
    def title(self, title):
        ''' title filters the courses by phrase in title '''
        key_words = title.split()
        print('\n** Requested title: ',key_words, '\n')
        return Schedule([course for course in self.courses for word in key_words if word in course['name'].lower()])
    
    def phrase(self, phrase):
        ''' phrase filters the courses by phrase in the description '''
        print('\n** Requested phrase: ', phrase.strip().lower(), '\n')
        return Schedule([course for course in self.courses if phrase.lower() in course['description'].lower()])
    
    def jingnu_status(self, status):
        ''' jingnu_status filters the courses by course status '''
        print('\n** Requested status: ', status.strip().lower(), '\n')
        return Schedule([course for course in self.courses if course['status_text'].lower() == status])

 
    