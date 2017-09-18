<div align="center">
    <h1>Schema</h1>
</div>

```python
>>> from schema import Schema
>>> instance = Schema('Thing')
```

```json
{
    "type": "Hospital",
    "prop":
    [
        {
            "name": "availableService",
            "type": ["MedicalProcedure", "MedicalTest", "MedicalTherapy"],
            "desc": "A medical service available from this provider."
        }
    ],
    "from":
    {
        "Place":
        [
            {
                "name": "additionalProperty",
                "type": ["PropertyValue"],
                "desc": "A property-value pair representing an additional characteristics of the entitity..."
            }   
        ]
    },
}