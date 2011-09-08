#from django.template import Context, loader

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
from django.template import RequestContext
from polls.models import Choice, Poll
#from django.http import HttpResponse

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	#t = loader.get_template('polls/index.html')
	#c = Context({
	#	'latest_poll_list': latest_poll_list,
	#})
	#output = ', '.join([p.question for p in latest_poll_list])
	#return HttpResponse(t.render(c))
	return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('polls/detail.html', {'poll':p},
				context_instance=RequestContext(request))

def results(request, poll_id):
        p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('polls/results.html', {'poll' : p})

def vote(request, poll_id):
        p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render_to_response('polls/detail.html', {'poll': p,'error_message': "You didn't select a choice.",}, context_instance=RequestContext(request))
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))

