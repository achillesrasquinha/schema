<div align="center">
    <img src=".github/logo.png" width="256">
    <h1>schema</h1>
    <h4>metadata, for humans</h4>
</div>

<p align="justify">
    <b>schema</b> helps you create objects, <em>on the fly</em>.
</p>

### Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

#### Installation

To install **schema**, simply use [`pip`](https://pip.pypa.io):

```console
$ pip install frappe-schema
```

#### Usage

<p align="justify">
    <b>schema</b> keeps it simple by fetching you human-readable (and minimal) schemas from data <a href="models">models</a> (provided by <a href="http://schema.org">schema.org</a>) updated <a href="https://en.wikipedia.org/wiki/Daily_build">nightly</a>. This ensures that you optionally recieve up-to-date schemas (<em>on the fly</em>) without having <b>schema</b> reinstalled, and speak in the same language with other users too.
</p>

```python
>>> import schema
>>> thing = schema.Schema('Thing')
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