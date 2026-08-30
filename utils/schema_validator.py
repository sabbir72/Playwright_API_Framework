import json

from jsonschema import validate

def validate_schema(response_body, schema_path):
    with open(schema_path, 
              "r",
              encoding="utf-8"
              )as file:
        schema=json.load(file)

    validate(
        instance=response_body, schema=schema
    )
