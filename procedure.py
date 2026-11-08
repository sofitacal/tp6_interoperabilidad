from fhir.resources.procedure import Procedure

# Crear el recurso FHIR de Procedure asociado a un paciente
def create_procedure_resource(patient_id, performed_datetime="2026-11-05T10:30:00-03:00"):
    procedure = Procedure(
        # Estado del procedimiento (obligatorio)
        status="completed",

        # Paciente al que se le realizó (obligatorio): referencia al Patient creado antes
        subject={"reference": f"Patient/{patient_id}"},

        # Categoría: procedimiento quirúrgico (SNOMED CT)
        category={
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "387713003",
                "display": "Surgical procedure"
            }]
        },

        # Qué procedimiento se hizo (SNOMED CT)
        code={
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "80146002",
                "display": "Appendectomy"
            }],
            "text": "Apendicectomía"
        },

        # Cuándo se realizó
        performedDateTime=performed_datetime,

        # Quién lo realizó (solo texto, sin referencia a un Practitioner)
        performer=[{"actor": {"display": "Dra. Ana Gómez - Cirugía General"}}],

        # Por qué se hizo: apendicitis aguda
        reasonCode=[{
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "85189001",
                "display": "Acute appendicitis"
            }]
        }],

        # Zona del cuerpo
        bodySite=[{
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "66754008",
                "display": "Appendix structure"
            }]
        }],

        # Resultado
        outcome={
            "coding": [{
                "system": "http://snomed.info/sct",
                "code": "385669000",
                "display": "Successful"
            }]
        },

        # Observaciones
        note=[{"text": "Procedimiento laparoscópico sin complicaciones."}]
    )
    return procedure
