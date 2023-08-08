from contact.views import ContactCreateView


urlpatterns = [
    path('', ContactCreateView.as_view(), name='contacts'),
]