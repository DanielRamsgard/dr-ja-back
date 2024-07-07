from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import send_res
import base64

# Create your views here.
@csrf_exempt
def form(request):
    if request.method == "POST":
        # Assuming request.body contains binary data (e.g., a file upload)
        binary_data = request.body

        encoded_data = base64.b64encode(binary_data).decode('utf-8')
        send_res(encoded_data)

        # Return a response (HTTP 200 OK) indicating success
        return HttpResponse("Email sent successfully")

    # Handle other HTTP methods if needed
    return HttpResponse(status=405)  # Method Not Allowed