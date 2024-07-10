import requests
from librenms.connection import librenms_api

# Función para obtener información de los dispositivos
def get_ports_by_device(dispositivo_id):
    response = librenms_api.get(f'/ports/search/device_id/{dispositivo_id}')
    if isinstance(response, requests.Response):
        if response.status_code == 200:
            devices = response.json()
            return devices['ports']
        else:
            print(f'Error: {response.status_code}')
            return None
    elif isinstance(response, dict):  # Handling if librenms_api.get() returns a dict
        return response.get('ports', None)
    else:
        print('Unexpected response type')
        return None
    
def get_port_info(port_id):
    response = librenms_api.get(f'/ports/{port_id}')
    if isinstance(response, requests.Response):
            if response.status_code == 200:
                ports_data = response.json()
                if 'port' in ports_data:
                    return ports_data['port'][0]
                else:
                    print('No ports key found in the response.')
                    return None
            else:
                print(f'Error: {response.status_code}')
                return None
    elif isinstance(response, dict):  # Handling if librenms_api.get() returns a dict
        if 'port' in response:
            return response['port'][0]
        else:
            print('No ports key found in the response.')
            return None
    else:
        print('Unexpected response type')
        return None
