# anagram optimal program

def anagram2(s1,s2):

        s1 = s1.replace(' ','').lower()
        s2 = s2.replace(' ','').lower()

        #return sorted(s1) == sorted(s2)
        if (sorted(s1) == sorted(s2)):
            print(True)
        else:
            print(False)







anagram2('public relations', 'crap built on lies')

anagram2('god','dog')

anagram2('aa','bb')
