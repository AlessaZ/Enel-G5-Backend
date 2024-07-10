from instance import LibreNMSAPI
import os

# Configurar la URL de la API de LibreNMS y el token de API
base_url = "http://34.150.135.224:7080/api/v0"
api_token = os.getenv('API_TOKEN')

# Crear una instancia de LibreNMSAPI
librenms_api = LibreNMSAPI(base_url, api_token)
