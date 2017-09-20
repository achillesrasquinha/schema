<div align="center">
    <img src=".github/logo.png" width="256">
    <h1>schema</h1>
    <h4>metadata, for humans</h4>
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

#### JSON Schemas
##### Tree
```json
{
    "name": "Thing",
    "desc": "The most generic type of item.",
    "type": "core",
    "children":
    [
        {
            "name": "Action",
            "children":
            [
                
            ]
        }
    ]
}
```

##### Type
```json
{
    "name": "Hospital",
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