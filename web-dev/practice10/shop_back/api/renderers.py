from rest_framework.renderers import JSONRenderer

class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type = None, renderer_context = None):
        response = renderer_context.get("response")
        statusCode = response.status_code if response else 200
        
        responseStructure = {
            "data" : data,
            "success" : statusCode < 400
        }
        
        return super().render(responseStructure, accepted_media_type, renderer_context)