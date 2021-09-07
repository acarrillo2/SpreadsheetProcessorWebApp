from io import StringIO
import csv
from django.http import HttpResponse

class CsvDataTransformer:
    def transform_csv_input_to_list_of_lists(self, csv_file):
        data_string = csv_file.read().decode("utf-8")
        string_io = StringIO(data_string)
        list_of_lists = list(csv.reader(string_io, skipinitialspace=True))

        return list_of_lists[1:]
    
    def transformer_list_of_dicts_to_http_response(self, list_of_dicts):
        columns = []
        for key in list_of_dicts[0].keys():
            columns.append(key)
        response = HttpResponse(
            content_type="text/csv",
            headers={'Content-Disposition': 'attachment; filename="output.csv"'},
        )
        writer = csv.DictWriter(response, fieldnames=columns)
        writer.writeheader()
        writer.writerows(list_of_dicts)

        return response