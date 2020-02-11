from django.shortcuts import render, redirect
import random #importing the random library in Python so we can use it


#########INDEX RENDER FUNCTION#########
def index(request):

    #Get a random number using the random library and save it in a variable
    randomNumber = random.randrange(0,101)
    dude = "Hey Man"
    #Create a object that saves random number variable in a key so it can
    #be passed to jinja engine in template
    context = {
        'rand_num': randomNumber,
        'string_dude': dude
    }

    #Add a int value 1 to the request.session object with key 'view_count'
    #so that it is set to 1 every time the page is visited for the first
    #time or session is cleared
    if 'view_count' not in request.session:
        request.session['view_count'] = 1
    
    #If 'view_count' is already a key present in the request.session object
    #then add 1
    elif 'view_count' in request.session:
        request.session['view_count'] += 1


    #Render page and pass context object to jinja
    return render(request, 'index.html', context)
###########################################


#########GENERATE NEW NUMBER FUNCTION#########
def generate(request):
    return redirect('/')
    #Redirect to the root url path and subsequently to the index views function
    #all over again
#############################################


#########CLEAR SESSION FUNCTION#########

    #Clear all information stored in the request.session object
def reset(request):
    request.session.clear()

    #Redirect to the root url path and subsequently to the index views function
    #all over again
    return redirect('/')
########################################

