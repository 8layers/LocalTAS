import LocalTAS

from Maltego import *


def phrase2Custom(request):
    TRX    = MaltegoTransform()
    entity = TRX.addEntity("8layers.CustomEntity", request.Value)
    return TRX.returnOutput()

__config__ = {
    "prefix": "8layers",
    "author": "8layers",
    "transforms": {
        "Custom": {
            'desc': "Custom Transform",
            'display': "Example Transform",
            'input': ['maltego.Phrase'],
            'call': phrase2Custom,
        },
    },
    'entities': {
        'CustomEntity' : {
            'category' : 'Testing',
            'icon': 'Person',
            'desc': 'Test entity',
            'parent': 'maltego.Person',
            'set' : 'Testing',
            'properties': {
                'value': {
                    'sample'  : 'Custom Entity'
                },
            }

        }
    },
    'transformsets': {
        'Testing': 'Transform for testing purpose'
    },
    'machines': {
        'Test': {
            'favorite' : True,
            'desc': 'Beschreibung',
            'instructions': 'start { run("8layers.Phrase2Custom") }'
        }
    }
}

if __name__ == "__main__":
    LocalTAS.run(__config__)
