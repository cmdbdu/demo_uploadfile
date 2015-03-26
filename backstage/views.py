from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from backstage.forms import DocumentForm
from backstage.models import Document

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print form.__dict__
        print repr(form)
        if form.is_valid():
            dc = Document(document = request.FILES['docfile'])
            dc.save()
            return HttpResponseRedirect(reverse('upload'))
    else:
        form = DocumentForm()
    return render_to_response('backstage/index.html',{'form':form},
                            context_instance=RequestContext(request))
