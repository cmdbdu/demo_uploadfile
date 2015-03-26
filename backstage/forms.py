# !/usr/bin/env python
# coding:UTF-8
# Created Time:2015-03-24
# Auther dub
from django import forms

class DocumentForm(forms.Form): 
   docfile = forms.FileField(label='select a file') 
