from distest.main.models import META_Data
import datetime

class METAmiddleware(object):
    def process_request(self, request):
        b=META_Data(ip = request.META.get('REMOTE_ADDR','none'), username=request.META.get('USERNAME','none'), date=datetime.datetime.now())
        b.save()
