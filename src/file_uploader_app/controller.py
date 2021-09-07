import logging
from django.shortcuts import render
from file_uploader_app.forms import UploadFileForm
from file_uploader_app.spreadsheet_processor import RealEstateSpreadsheetProcessor
from file_uploader_app.data_transformer import CsvDataTransformer

class SpreadsheetProcessorController:
    def __init__(self):
        self.processor = RealEstateSpreadsheetProcessor()
        self.transformer = CsvDataTransformer()
    
    def execute(self, request):
        if request.method == "GET":
            form = UploadFileForm()

            return render(request, "home.html", {"form":form, "message":""})
        
        elif request.method == "POST":
            try:
                form = UploadFileForm(data=request.POST, files=request.FILES)
                if form.is_valid():
                    csv_file = form.cleaned_data['file']
                    if not csv_file.name.endswith('.csv'):
                        return render(request, "home.html", {"form":form, "message":'Error: Please select a .csv file'})
                    list_of_lists = self.transformer.transform_csv_input_to_list_of_lists(csv_file)
                    processed_list_of_dicts = self.processor.process_file(list_of_lists)
                    http_response = self.transformer.transformer_list_of_dicts_to_http_response(processed_list_of_dicts)

                    return http_response
            except Exception as e:
                logging.warn(e)
                return render(request, "home.html", {"form":form, "message":"There was an error processing your file."})