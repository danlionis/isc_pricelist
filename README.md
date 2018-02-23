# Pricelist Generator

## General

Tables are in `.csv` format

Headers are **not** allowed inside any table.

The names of *region, country* and *operator* in the output tables are taken from the `marketshare` table. That's why they are not required in the pricelist table.

## Pricelist

mnc values can be seperated by a `comma` ( , ) if there is more than one mnc number for an operator

### Schema

|Column |Values   |type     |required|
|-      |-        |-        |:-:      |
|A      |region   |text     |   
|B      |country  |text     |
|C      |operator |text     |
|D      |mcc      |number   |X        |
|E      |mnc      |number (comma seperated)   |X        |
|F      |price    |number   |X        |

### Example

|A (region)|B (country)|C (operator)|D (mcc)|E (mnc)|F (price)|
|-|-|-|-|-|-|
|Europe|Germany|Telefonica O2 Germany|262|07,08,11|0,0630|
|Europe|Germany|Telekom Germany|262|01|0,0580|
|Europe|Germany|Vodafone D2|262|02,04,09|0,0580|


## Marketshare Table

mnc values can **not** be seperated by a comma.

### Schema

|Column |Values     |type     |required|
|-      |-          |-        |:-:      |
|A      |region     |text     |X        |
|B      |country    |text     |X        |
|C      |operator   |text     |X        |
|D      |mcc        |number   |X        |
|E      |mnc        |number   |X        |
|F      |marketshare|percentage|X        |

### Example

|A (region)|B (country)|C (operator)|D (mcc)|E (mnc)|F (marketshare)|
|-|-|-|-|-|-|
|Europe|Germany|Telekom (Deutsche Telekom)|262|01|31,826%|
|Europe|Germany|Vodafone|262|02|34,090%|
|Europe|Germany|O2 (Telefónica)|262|07|34,084%|


## Usage

1. Open the .exe file
2. Select a pricelist table
3. Select a marketshare table
4. Select an output directory
5. Select a percentage which will be added to the salesprice
6. Click on generate
7. If any errors occured they will show in the console
