from django.shortcuts import render

import matplotlib.pyplot as plt
import numpy as np

# Create your views here.
def threeplayers(request):
    exp_vals3 = ['33.33','33.33','33.33']
    exp_labels3 = ["one", "two","three"]
    y = np.array([33.3,33.3,33.3])
    plt.pie(y, labels=["one", "two","three"])
    plt.axis('equal')
    plt.savefig("static/test/threeplayers.png")


    return render(request, 'spin/three.html')