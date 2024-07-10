from librenms.devices import get_device
from librenms.ports import get_ports_by_device, get_port_info
from librenms.switching import get_links_by_device, get_vlans_by_device
from concurrent.futures import ThreadPoolExecutor
from functools import partial

def get_ports_info(idLnms):
    ports = get_ports_by_device(idLnms)
    neighbours = get_links_by_device(idLnms)
    
    # Crear un diccionario para búsqueda rápida de enlaces por local_port_id
    links_by_port_id = {}
    for neighbour in neighbours:
        local_port_id = neighbour['local_port_id']
        if local_port_id not in links_by_port_id:
            links_by_port_id[local_port_id] = []
        links_by_port_id[local_port_id].append(neighbour)
    
    # Función para obtener información de puerto con vecino
    def get_port_info_with_neighbour(port):
        port_id = port['port_id']
        if port_id in links_by_port_id:
            port['neighbours'] = links_by_port_id[port_id]
        else:
            port['neighbours'] = None  # o cualquier manejo deseado si no hay vecino
        
        port_info = get_port_info(port_id)
        port.update(port_info)  # Actualizar el diccionario del puerto con la información obtenida
        
        return port
    
    # Obtener datos de los puertos utilizando threads
    with ThreadPoolExecutor(max_workers=10) as executor:
        portsData = list(executor.map(get_port_info_with_neighbour, ports))
    
    return portsData

class DeviceService:
    @staticmethod
    def get_device_info(idLnms):
        # Inicializa una respuesta vacía
        response = {}

        with ThreadPoolExecutor(max_workers=4) as executor:
            # Futuros para cada llamada API
            futures = {
                'device': executor.submit(get_device, idLnms),
                'ports': executor.submit(get_ports_info, idLnms),
                'vlans': executor.submit(get_vlans_by_device, idLnms)
            }
            
            # Esperar a que se completen todas las llamadas
            results = {name: future.result() for name, future in futures.items()}
        
        # Verificar y actualizar la respuesta con los resultados
        if not results['device']:
            raise Exception("API did not send device")
        response.update(results['device'])
        
        response['ports'] = results['ports']
        response['vlans'] = results['vlans']
        
        return response

        