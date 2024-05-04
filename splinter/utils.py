import json
from splinter import models
from datetime import datetime

def save_data(splinter_dict):

    # Pull out the timestamp and remove from dict
    time_stamp = splinter_dict['timestamp']
    # YYYY-MM-DD HH:MM:ss
    updated_timestamp = datetime.strptime(
                                            time_stamp,
                                            "%m/%d/%Y, %H:%M:%S"
                                        )

    del splinter_dict['timestamp']

    for key, value in splinter_dict.items():
    	existing_data = models.SplinterDataPoint.objects.filter(
    																tag_name=key,
    																timestamp=updated_timestamp,
    															)
    	if existing_data.exists():
    		print("Data point already exists in DB")
    	else:
	        TempDataPoint = models.SplinterDataPoint(
	                                                        tag_name=key,
	                                                        tag_value=value,
	                                                        timestamp=updated_timestamp,
	                                                    )
	        TempDataPoint.save()


def read_json_file(filename):
	with open(filename) as f:
	    data = json.load(f)
	return data