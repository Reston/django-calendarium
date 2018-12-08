"""URLs for the ``calendarium`` app."""
from django.urls import path, re_path

from . import views

app_name = "calendarium"

urlpatterns = [
    # event views
    path(
        'event/create/',
        views.EventCreateView.as_view(),
        name='calendar_event_create'),

    path(
        'event/<int:pk>/',
        views.EventDetailView.as_view(),
        name='calendar_event_detail'),

    path(
        'event/<int:pk>/update/',
        views.EventUpdateView.as_view(),
        name='calendar_event_update'),

    path(
        'event/<int:pk>/delete/',
        views.EventDeleteView.as_view(),
        name='calendar_event_delete'),

    # occurrence views
    re_path(
        r'^event/(?P<pk>\d+)/date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
        views.OccurrenceDetailView.as_view(),
        name='calendar_occurrence_detail'),

    re_path(
        r'^event/(?P<pk>\d+)/date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/update/$',  # noqa: E501
        views.OccurrenceUpdateView.as_view(),
        name='calendar_occurrence_update'),

    re_path(
        r'^event/(?P<pk>\d+)/date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/delete/$',  # noqa: E501
        views.OccurrenceDeleteView.as_view(),
        name='calendar_occurrence_delete'),

    # calendar views
    re_path(
        r'^(?P<year>\d+)/(?P<month>\d+)/$',
        views.MonthView.as_view(),
        name='calendar_month'),

    re_path(
        r'^(?P<year>\d+)/week/(?P<week>\d+)/$',
        views.WeekView.as_view(),
        name='calendar_week'),

    re_path(
        r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
        views.DayView.as_view(),
        name='calendar_day'),

    path(
        'get-events/',
        views.UpcomingEventsAjaxView.as_view(),
        name='calendar_upcoming_events'),

    path(
        '',
        views.CalendariumRedirectView.as_view(),
        name='calendar_current_month'),

]
