from file_uploader_app.controller import SpreadsheetProcessorController

# Create your views here.

def home(request):
    controller = SpreadsheetProcessorController()
    return controller.execute(request)