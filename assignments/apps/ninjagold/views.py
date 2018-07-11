# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# def index(request):
#     response = "The Index Route is Working!"
#     return HttpResponse(response)


def index(request):
  if 'gold' in session:
    session['gold'] = session['gold']
  else:
    session['gold'] = 0
  if 'append' not in session:
    session['append'] = []

  session['farm'] = random.randrange(10,20)
  session['cave'] = random.randrange(5,10)
  session['house'] = random.randrange(2,5)
  session['casino'] = random.randrange(-50,50)
  return render_template('index.html')

def gold(request):
  if request.form['location'] == 'farm':
    session['gold'] += session['farm']
    session['append'].insert(0, "Gained " + str(session['farm']) + " from the farm. " + str(datetime.datetime.now()))
  if request.form['location'] == 'cave':
    session['gold'] += session['cave']
    session['append'].insert(0, "Gained " + str(session['cave']) + " from the cave. " + str(datetime.datetime.now()))
  if request.form['location'] == 'house':
    session['gold'] += session['house']
    session['append'].insert(0, "Gained " + str(session['house']) + " from the house " + str(datetime.datetime.now()))
  if request.form['location'] == 'casino':
    session['gold'] += session['casino']
    session['append'].insert(0, str(session['casino']) + " from the casino " + str(datetime.datetime.now()))
  return redirect('/')

def reset(request):
  session.clear()
  return redirect('/')