from django.http import request
from django.shortcuts import redirect, render
import numpy as np
import os
from django.conf import settings

def create_chart(num, label_name):
    
    characters_to_remove = "'[]"
    new_string = label_name

    for character in characters_to_remove:
        new_string = new_string.replace(character, "")

    if num == 2:
        import matplotlib.pyplot as plt

        plt.pie(['50','50'], labels=  new_string.split(','))
        plt.axis('equal')
        plt.savefig("static/test/twoplayers.png")
        plt.cla()
        plt.clf()
        plt.close()

    if num == 3:
        import matplotlib.pyplot as plt
        plt.pie(['33.3','33.3', '33.3'], labels=new_string.split(','))
        plt.axis('equal')
        plt.savefig("static/test/threeplayers.png")
        plt.cla()
        plt.clf()
        plt.close()

    if num == 4:
        import matplotlib.pyplot as plt
        plt.pie(['25','25', '25', '25'], labels=new_string.split(','))
        plt.axis('equal')
        plt.savefig("static/test/fourplayers.png")
        plt.cla()
        plt.clf()
        plt.close()

    if num == 5:
        import matplotlib.pyplot as plt
        plt.pie(['20','20', '20', '20', '20'], labels=new_string.split(','))
        plt.axis('equal')
        plt.savefig("static/test/fiveplayers.png")
        plt.cla()
        plt.clf()
        plt.close()

    if num == 6:
        import matplotlib.pyplot as plt
        plt.pie(['16.6','16.6', '16.6','16.6','16.6','16.6'], labels=new_string.split(','))
        plt.axis('equal')
        plt.savefig("static/test/sixplayers.png")
        plt.cla()
        plt.clf()
        plt.close()



# Create your views here.
def spin(request):
    """ GETS THE USERS FOR MAKING THE SPIN"""

    if request.method == "POST":
        print(request.POST)
        no_of_players = request.POST.get('no_of_players')
        return redirect('spin:getnames',no_of_players)

    else:

        context = {
            'title' : 'SPIN HOME'
        }

        return render(request, 'spin/spinhome.html' , context)

def getnames(request, pk):

    if request.method == "POST":
        print(request.POST)
        no_of_names = request.POST.get('number_of_names')
        print(' post la varadhuu idhu dhaa           ',request.POST.get('number_of_names'))
        if no_of_names == '1':
            getplayer1 = request.POST.get('name_of_player11')
            ls = []
            ls.append(getplayer1)
            return redirect('spin:twoplayers',ls)
        elif no_of_names == '2':
            print('entering 2222')
            getplayer1 = request.POST.get('name_of_player21')
            getplayer2 = request.POST.get('name_of_player22')

            ls = []
            ls.append(getplayer1)
            ls.append(getplayer2)
            return redirect('spin:twoplayers',ls)

        elif no_of_names == '3':
            getplayer1 = request.POST.get('name_of_player31')
            getplayer2 = request.POST.get('name_of_player32')
            getplayer3 = request.POST.get('name_of_player33')

            ls = []
            ls.append(getplayer1)
            ls.append(getplayer2)
            ls.append(getplayer3)

            return redirect('spin:threeplayers',ls)


        elif no_of_names == '4':
            getplayer1 = request.POST.get('name_of_player41')
            getplayer2 = request.POST.get('name_of_player42')
            getplayer3 = request.POST.get('name_of_player43')
            getplayer4 = request.POST.get('name_of_player44')

            ls = []
            ls.append(getplayer1)
            ls.append(getplayer2)
            ls.append(getplayer3)
            ls.append(getplayer4)
            
            
            return redirect('spin:fourplayers',ls)

        elif no_of_names == '5':
            getplayer1 = request.POST.get('name_of_player51')
            getplayer2 = request.POST.get('name_of_player52')
            getplayer3 = request.POST.get('name_of_player53')
            getplayer4 = request.POST.get('name_of_player54')
            getplayer5 = request.POST.get('name_of_player55')

            ls = []
            ls.append(getplayer1)
            ls.append(getplayer2)
            ls.append(getplayer3)
            ls.append(getplayer4)
            ls.append(getplayer5)
            
            
            return redirect('spin:fiveplayers',ls)

        elif no_of_names == '6':
            print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
            getplayer1 = request.POST.get('name_of_player61')
            getplayer2 = request.POST.get('name_of_player62')
            getplayer3 = request.POST.get('name_of_player63')
            getplayer4 = request.POST.get('name_of_player64')
            getplayer5 = request.POST.get('name_of_player65')
            getplayer6 = request.POST.get('name_of_player66')

            ls = []
            ls.append(getplayer1)
            ls.append(getplayer2)
            ls.append(getplayer3)
            ls.append(getplayer4)
            ls.append(getplayer5)
            ls.append(getplayer6)
            
            
            return redirect('spin:sixplayers',ls)
        
        

    print('getting names' , pk)
    context = {
        'pk' : pk
    }
    return render(request, 'spin/spin_getnames.html', context)

def twoplayers(request,ls):
    print('entering game 2', ls , type(ls))
    create_chart(2, ls)
    return render(request, 'spin/two.html')

def threeplayers(request,ls):
    print('entering game 3')
    create_chart(3, ls)
    return render(request, 'spin/three.html')

def fourplayers(request, ls):
    print('entering game 4')
    create_chart(4, ls)
    return render(request, 'spin/four.html')

def fiveplayers(request, ls):
    print('entering game 5')
    create_chart(5, ls)
    return render(request, 'spin/five.html')

def sixplayers(request, ls):
    print('entering game 6')
    create_chart(6, ls)
    return render(request, 'spin/six.html')
