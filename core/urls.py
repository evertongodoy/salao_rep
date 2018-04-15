from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
    # url (r'^$', 'TaskManager.views.page'), EXEMPLO DE COMO ERA ANTES, O PADRAO DA URL FOI PARA O PATTERNS ACIMA
    url (r'^$', 'principal'),
	url (r'^index/$', 'home'),
)
