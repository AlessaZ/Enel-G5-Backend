from librenms.devices import get_device
from librenms.ports import get_ports_by_device, get_port_info
from librenms.switching import get_links_by_device, get_vlans_by_device
from concurrent.futures import ThreadPoolExecutor

def get_ports_info(idLnms):
    ports = get_ports_by_device(idLnms)
    portsIDs = [port['port_id'] for port in ports]
    
    # Obtener datos de los puertos utilizando threads
    with ThreadPoolExecutor(max_workers=10) as executor:
        portsData = list(executor.map(get_port_info, portsIDs))
    
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
                'neighbours': executor.submit(get_links_by_device, idLnms),
                'vlans': executor.submit(get_vlans_by_device, idLnms)
            }
            
            # Esperar a que se completen todas las llamadas
            results = {name: future.result() for name, future in futures.items()}
        
        # Verificar y actualizar la respuesta con los resultados
        if not results['device']:
            raise Exception("API did not send device")
        response.update(results['device'])
        
        response['ports'] = results['ports']
        response['neighbours'] = results['neighbours']
        response['vlans'] = results['vlans']
        
        return response

        