import requests
from connection import librenms_api

# Función para obtener información de los dispositivos
def get_devices():
    response = librenms_api.get('/devices')
    if isinstance(response, requests.Response):
        if response.status_code == 200:
            devices = response.json()
            return devices['devices']
        else:
            print(f'Error: {response.status_code}')
            return None
    elif isinstance(response, dict):  # Handling if librenms_api.get() returns a dict
        return response.get('devices', None)
    else:
        print('Unexpected response type')
        return None

# Función para obtener todos los datos de un dispositivo por su ID
def get_device(dispositivo_id):
    response = librenms_api.get(f'/devices/{dispositivo_id}')
    if isinstance(response, requests.Response):
            if response.status_code == 200:
                device_data = response.json()
                if 'devices' in device_data:
                    return device_data['devices'][0]
                else:
                    print('No devices key found in the response.')
                    return None
            else:
                print(f'Error: {response.status_code}')
                return None
    elif isinstance(response, dict):  # Handling if librenms_api.get() returns a dict
        if 'devices' in response:
            return response['devices'][0]
        else:
            print('No devices key found in the response.')
            return None
    else:
        print('Unexpected response type')
        return None




