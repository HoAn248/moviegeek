from django.urls import path


from recommender import views

urlpatterns = [
    path(r'^chart/', views.chart, name='chart'),
    path(r'^association_rule/(?P<content_id>\w+)/$',
        views.get_association_rules_for,
        name='get_association_rules_for'),
    path(r'^ar/(?P<user_id>\w+)/$',
        views.recs_using_association_rules,
        name='recs_using_association_rules'),
    path(r'^sim/user/(?P<user_id>\w+)/(?P<sim_method>\w+)/$',
        views.similar_users, name='similar_users'),
    path(r'^cb/item/(?P<content_id>\w+)/$',
        views.similar_content, name='similar_content'),
    path(r'^cb/user/(?P<user_id>\w+)/$',
        views.recs_cb, name='recs_cb'),
    path(r'^cf/user/(?P<user_id>\w+)/$',
        views.recs_cf, name='recs_cb'),
    path(r'^funk/user/(?P<user_id>\w+)/$',
        views.recs_funksvd, name='recs_funksvd'),
    path(r'^fwls/user/(?P<user_id>\w+)/$',
        views.recs_fwls, name='recs_fwls'),
    path(r'^bpr/user/(?P<user_id>\w+)/$',
        views.recs_bpr, name='recs_fwls'),
    path(r'^pop/user/(?P<user_id>\w+)/$',
        views.recs_pop, name='recs_pop')
]
