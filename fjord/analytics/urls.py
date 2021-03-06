from django.conf.urls import patterns, url

from fjord.analytics.analyzer_views import (
    ProductsUpdateView,
    SurveyCreateView
)


urlpatterns = patterns(
    'fjord.analytics.views',

    # This covers / and /dashboard
    url(r'^(?:dashboard/?)?$', 'dashboard', name='dashboard'),

    # This covers product dashboards
    url(r'^dashboard/(?P<productslug>[^/]+)/?$',
        'product_dashboard_router', name='product_dashboard'),

    # Show a specific response
    url(r'^dashboard/response/(?P<responseid>\d+)/?$',
        'response_view', name='response_view'),

    # Translate a specific response
    url(r'^dashboard/translate/(?P<responseid>\d+)/?$',
        'spot_translate', name='spot_translate'),
)

# These are analyzer-group only views.
urlpatterns += patterns(
    'fjord.analytics.analyzer_views',

    # Analytics dashboard
    url(r'^analytics/?$', 'analytics_dashboard',
        name='analytics_dashboard'),
    url(r'^analytics/occurrences/?$', 'analytics_occurrences',
        name='analytics_occurrences'),
    url(r'^analytics/products/?$', ProductsUpdateView.as_view(),
        name='addproducts'),
    url(r'^analytics/search/?$', 'analytics_search',
        name='analytics_search'),
    url(r'^analytics/hourly/?$', 'analytics_hourly_histogram',
        name='analytics_hourly_histogram'),
    url(r'^analytics/duplicates/?$', 'analytics_duplicates',
        name='analytics_duplicates'),
    url(r'^analytics/hbdata(?:/(?P<answerid>\d+))?/?$', 'hb_data',
        name='hb_data'),
    url(r'^analytics/hberrorlog(?:/(?P<errorid>\d+))?/?$', 'hb_errorlog',
        name='hb_errorlog'),
    url(r'^analytics/hbsurveys/?$', SurveyCreateView.as_view(), name='hb_surveys'),
)
