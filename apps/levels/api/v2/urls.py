# Django Core Libraries
from django.conf.urls import url

# Own´s Libraries
from .viewsets import (
    AssesmentCreateView,
    LevelsView,
    ChildrenLevelsView,
)


levels_v2_urls = [
    url(r'^assesment/', AssesmentCreateView.as_view(), name='create-assesment'),
    url(r'^create/', LevelsView.as_view(), name='levels-v2'),
    url(r'^children/', ChildrenLevelsView.as_view(), name='children-levels-v2'),
]
