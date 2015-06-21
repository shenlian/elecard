from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$','home.views.login'),
    url(r'^edit/(?P<wechatid>\w+)$','home.views.edit'),
    url(r'^finish/(?P<card_id>.{36})$','home.views.finish'),
    url(r'^login$','home.views.login'),
    url(r'^cardstyle/(?P<card_id>.{36})$','home.views.cardstyle'),
    url(r'^cardedit/(?P<card_id>.{36})$','home.views.cardedit'),
    url(r'^cardedit_after/(?P<card_id>.{36})$','home.views.cardedit_after'),
    url(r'^makeOrder/(?P<card_id>.{36})$','home.views.makeOrder'),
    url(r'^shipaddress/(?P<card_id>.{36})$','home.views.shipaddress'),
    url(r'^enteraddress/(?P<wechatid>\w+)$','home.views.enteraddress'),
    url(r'^confirmaddress/(?P<wechatid>\w+)/','home.views.confirmaddress'),
    url(r'^shipway$','home.views.shipway'),
    url(r'^micro/electronic_edit$','home.views.electronic_edit'),
    url(r'^micro/card_holder$','home.views.card_holder'),
    url(r'^micro/electronic_finish$','home.views.electronic_finish'),
    # url(r'^vedioshare/', include('vedioshare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^normal/', include('normal.urls')),
    # url(r'^registration/',include('registration.urls'),),
    url(dajaxice_config.dajaxice_url,include('dajaxice.urls')),
	# url(r'^replay/(?P<pid>.{36})$','normal.views.replay',name = "replay"),
)
# for develop to serve user-upload content in MEDIA_ROOT
if settings.DEBUG:
	 urlpatterns += patterns('',
			 url(r'^media/(?P<path>.*)$',
				 'django.views.static.serve',
				 {'document_root': settings.MEDIA_ROOT}),
				 )



