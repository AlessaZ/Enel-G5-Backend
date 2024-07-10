from connection import librenms_api

# Función para obtener información de los dispositivos
def get_ports_by_device(dispositivo_id):
    response = librenms_api.get(f'/ports/search/?device_id\={dispositivo_id}')
    if response.status_code == 200:
        dispositivos = response.json()
        return dispositivos['ports']
    else:
        print(f'Error: {response.status_code}')
        return None
    
def get_port_info(port_id):
    response = librenms_api.get(f'/ports/{port_id}')
    if response.status_code == 200:
        dispositivos = response.json()
        return dispositivos['ports']
    else:
        print(f'Error: {response.status_code}')
        return None
    

# Llamar a la función y mostrar la información de los dispositivos
dispositivo = get_port_info(1)

print(f"ID: {dispositivo['device_id']}")