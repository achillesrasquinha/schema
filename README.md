<div align="center">
    <img src=".github/logo.png" width="200">
    <h1>Schema</h1>
</div>

### Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

#### Installation

#### Usage
```python
>>> from schema import Schema
>>> instance = Schema('Thing')
```

JSON Schema
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
```

#### License
This repository has been released under the [MIT License](LICENSE)