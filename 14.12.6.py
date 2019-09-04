
from urllib import urlopen

  
def find_city(html):    
    " Finds city within the provided HTML script using html_find function"

    return html_find(html, delimiter1= '<title>', delimiter2= ' zip code</title>')
    
    

def find_population(html):    
    " Finds population within the provided HTML script using html_find function "
    
    return html_find(html, delimiter1= 'Total population</dt><dd>', delimiter2= '<span class="trend')


def html_find(html, delimiter1, delimiter2):
    """ Takes a list of the lines of code within a HTML script
        Searches for data indirectly by finding index of delimeter1 and delimeter2  """

    for line in html:
        if delimiter1 in line and delimiter2 in line:
            return line[line.find(delimiter1) + len(delimiter1) : line.find(delimiter2)]
            
        
def run():    
    " Runs loop which prompts user for a zipcode and prints the zipcode's city and population "
    
    while True:
        
        inpt = raw_input('\n\nWhat is the zipcode would you like to search? ')
        conn = urlopen('http://www.uszip.com/zip/' + inpt)
        html = conn.read().split('\n')
        conn.close()
        
        print '\nThe provided zip code belongs to %s, which has a population of %s.'%(find_city(html), find_population(html))
        if 'y' in raw_input('\nContinue program? ').lower(): continue 
        else: break
    
    
if __name__ == '__main__':

    run()
