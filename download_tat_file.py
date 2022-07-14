%cpaste
import copy
import csv
import json
import os

import boto3



# columns = {
#     'air_lane_exists': '',
#     'destination': '',
#     'origin': '',
#     'dto_cutoff': '',
#     'dto_tat': '',
#     'flash_air_cutoff': '',
#     'flash_air_tat': '',
#     'forward_express_cutoff': '',
#     'forward_express_tat': '',
#     'forward_surface_cutoff': '',
#     'forward_surface_tat': '',
#     'heavy_cutoff': '',
#     'heavy_tat': '',
#     'ltl_air_cutoff': '',
#     'ltl_air_tat': '',
#     'ltl_regular_cutoff': '',
#     'ltl_regular_tat': '',
#     'next_b2c_surface_cutoff': '',
#     'next_b2c_surface_tat': '',
#     'return_cutoff': '',
#     'return_tat': '',
#     'rvp_air_cutoff': '',
#     'rvp_air_tat': ''
# }

columns = {
    'origin': '',
    'destination': '',
    'ltl_regular_cutoff': '',
    'ltl_regular_tat': ''
}

tat_name = 'TALBROS B2B'

def download_all_objects_in_folder():
    data_file = open('/tmp/{}.csv'.format(tat_name), 'w')
    writer = csv.DictWriter(data_file, fieldnames=columns.keys())
    writer.writeheader()
    count = 0

    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket('express-production-od-tat')
    objects = my_bucket.objects.filter(Prefix='od-tat-in-templates/{}/'.format(tat_name))

    for obj in objects:
        path, filename = os.path.split(obj.key)
        if not filename:
            continue
        print("{}, {}".format(path, filename))
        filepath = "/tmp/{}".format(filename)
        my_bucket.download_file(obj.key, filepath)
        print("Count: {}".format(count))
        with open(filepath) as json_file:
            data = json.load(json_file)
        try:
            for k, v in data.items():
                od_pair = k.split("_")
                row_dict = copy.deepcopy(columns)
                row_dict["origin"] = od_pair[0]
                row_dict["destination"] = '_'.join(od_pair[1:])
                for column in columns:
                    if column in v:
                        row_dict[column] = v.get(column)
                writer.writerow(row_dict)
        except Exception as err:
            print('Filename: {}, Error: {}'.format(filename, err))

        count += 1
        os.remove(filepath)

    data_file.close()


download_all_objects_in_folder() 
--