import requests
from patient import create_patient_resource


# Enviar el recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource,resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)
    print("Método:", response.request.method, "| URL final:", response.url, "| Redirecciones:", response.history)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        
        # Devolver el ID del recurso creado
        return response.json()['id']
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None

# Buscar el recurso por ID 
def get_resource_from_hapi_fhir(resource_id, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())

# MÉTODO: Buscar pacientes por número de documento
def search_patient_by_document(document_number, document_system="http://www.renaper.gob.ar/dni"):
    url = "http://hapi.fhir.org/baseR4/Patient"
    params = {"identifier": f"{document_system}|{document_number}"}
    headers = {"Accept": "application/fhir+json", "Cache-Control": "no-cache"}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Error en la búsqueda: {response.status_code}")
        print(response.json())
        return []

    bundle = response.json()
    patients = [entry["resource"] for entry in bundle.get("entry", [])]
    print(f"Se encontraron {len(patients)} paciente(s) con documento {document_number}")
    for p in patients:
        print(f"  ID: {p['id']} - Nombre: {p.get('name')}")
    return patients

