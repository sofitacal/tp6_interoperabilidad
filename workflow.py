from patient import create_patient_resource
from procedure import create_procedure_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, search_patient_by_document

if __name__ == "__main__":
    dni = "44345123"

    # 3b: buscar si ya existe un paciente con ese DNI
    existentes = search_patient_by_document(dni)

    if existentes:
        patient_id = existentes[0]["id"]
        print(f"El paciente ya existía, se usa el ID {patient_id}")
    else:
        # 3a: crear el paciente con DNI
        patient = create_patient_resource(
            family_name="Rodrigo", given_name="Olivia",
            birth_date="2002-05-10", gender="female",
            document_number=dni
        )
        patient_id = send_resource_to_hapi_fhir(patient, "Patient")

    if patient_id:
        # 3a: leer el paciente
        get_resource_from_hapi_fhir(patient_id, "Patient")

        # 3c: crear un Procedure asociado al paciente y leerlo
        procedure = create_procedure_resource(patient_id)
        procedure_id = send_resource_to_hapi_fhir(procedure, "Procedure")

        if procedure_id:
            get_resource_from_hapi_fhir(procedure_id, "Procedure")
