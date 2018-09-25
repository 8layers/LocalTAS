# LocalTAS

LocalTAS is designed to create Maltego configuration files and launch local transforms easily. Additionally it is able to create the TRX.wsgi for the TDS. The following configurations are supported:
* Transforms
* Icons
* Entities
* Transform Sets
* Machines


### Prerequisites

LocalTAS requires 
* [Python3](https://www.python.org/downloads/)
* [python-resize-image](https://github.com/charlesthk/python-resize-image) (for icons)

Patervas [Python TRX Library](https://docs.paterva.com/en/developer-portal/transform_libraries/) has been updated to Python3 and is included in this repository.

## Usage
Create a Python file that contains your transforms. Add the following lines.

```
import LocalTAS
...
__config__ = {...}
if __name__ == __main__:
    LocalTAS.run(__config__)
```

Create the configuration files (config.mtz and TRX.wsgi) via

```
$ python3 LocalTAS.py yourTransformFile.py
```

Test your transform with

```
$ python3 yourTransformFile.py -t TransformName -i maltego.Entity EntityValue "parameterName=parameterValue"
```
### Configuration
Key | Type | Description | Optional | Default
---|---|---|---|---
desc | string | The prefix will be used to genereate the unique id of transforms and entites. | yes  | rndString(6)
author | string | In in case of transforms Maltego asks for an author. | yes | String(0)
transforms | dict | Transform configuration | yes | - 
icons | dict | Icon configuration | yes | - 
entities | dict | Entity configuration | yes | - 
transformsets | dict | Transform sets | yes | - 
machines | dict | Machine configuration | yes | - 

#### Transform Configuration
All transforms are defined in a dict. The key value defines the transform name. 
```
__config__['entities'] = {
    'TransformName': {..}
}
```
The following settings are available:

Key | Type | Description | Optional | Default
---|---|---|---|---
desc | string | Description of the transform | yes  | String(0)
display | string | Display name at context menu | yes | Transform ID
set | string | Name of the transform set that this transform should be within | yes | -
input | list of string | Name the entities that the trasform should be available for | no | - 
call | calllable | Reference to the actual transform | no | - 

In case you need the transform id:
```
transfomID = __config__['prefix'] + '.' entityName + '2' + TransformName
# Example result: 8layers.Domain2IP
```

#### Icon Configuration
The configuraion for icons is straight forward
```
__config__['icons'] = {
    'IconFolder': {
        'IconName' : 'path/to/icon.png',
    }
}
```

#### Entity Configuration
The entity configuration is the most complex one. Every entity has properties which should to be defined separately. First we start with the entities. All entities are defined in a dict. The key value defines the entity name. 
```
__config__['entities'] = {
    'EntityName': {..}
}
```
The following settings are available:

Key | Type | Description | Optional | Default
---|---|---|---|---
icon | string | IconName | no | -
category | string | Choose or create a category this entity belongs to | no | - 
desc | string | Description of the entity | yes  | String(0)
parent | string | Entity ID of the parent entity | yes | -
displayValue | string | ID of the property that should be displayed at the graph | yes | -
editValue | string | ID of the property that should be edited on dbl-click | yes | -
properties | dict | Define special properties for your entity | yes | -

In case you need the entity id:
```
entityID = __config__['prefix'] + '.' entityName
# Example result: 8layers.BtcCluster
```

##### Property Configuration
```
__config__['entities']['EntityName']['properties'] = {
    'PropertyName': {..}
}
```
The following settings are available:

Key | Type | Description | Optional | Default
---|---|---|---|---
default | string | The Default value of the property | yes | -
sample | string | The value of the property when dragged from the palette | yes | String(0)
desc | string | Description for this property | yes | String(0)
type | string | The data type of this property | yes  | string
display | string | Value that sould be shown in the property view | yes | PropertyName
nullable | bool | property can be null | yes | True
hidden | bool | hide the property | yes | False
readonly | bool | disallow to edit the value| yes | False

In case you need the property id:
```
propertyID = 'properties.' + PropertyName
# Example result: properties.cryptocurrencyaddress
```

#### Transform Set Configuration
The configuraion for transform sets quiet simple
```
__config__['transformsets'] = {
    'TransformSetName' : 'description of your transform set',
}
```

#### Machine Configuration
All machines are defined in a dict. The key value defines the machine name. 
```
__config__['machines'] = {
    'MachineName': {..}
}
```
The following settings are available:

Key | Type | Description | Optional | Default
---|---|---|---|---
instructions | string | Insert your machine instructions here ("start{...}") | no | -
Default | string | Description of your machine | yes | String(0)
favorite | bool | Mark the machine as favorite | yes | False
enabled | bool | Enable or Disable your machine | yes | True

In case you need the machine id:
```
machineID = __config__['prefix'] + "." + MachineName
# Example result: 8layers.DNS
```

