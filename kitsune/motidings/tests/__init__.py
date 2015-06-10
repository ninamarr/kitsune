from factory.django import DjangoModelFactory
from tidings.models import Watch


class WatchFactory(DjangoModelFactory):
    class Meta:
        model = Watch

    event_type = 'fooevent'
    is_active = True
