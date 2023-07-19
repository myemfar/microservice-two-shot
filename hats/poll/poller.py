import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hats_project.settings")
django.setup()

# Import models from hats_rest, here.
from hats_rest.models import LocationVO


def poll():
    while True:
        print('hats poller changed')
        try:
            url = "http://wardrobe-api:8000/api/locations/"
            response = requests.get(url)
            content = json.loads(response.content)
            for location in content["locations"]:
                LocationVO.objects.update_or_create(
                    import_href=location["href"],
                    defaults={"closet_name": location["closet_name"]},
                )
            # Write your polling logic, here
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(20)


if __name__ == "__main__":
    poll()
