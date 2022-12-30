## cidrCalc.py
- Small utility script that takes in a CIDR block as an argument and returns the first and last IP of the range. Can optionally iterate through the range to print every IP.

## genVipARecords.py
- Helpful for creating/appending raw DNS A records to zone files to be imported into DNS systems.
###### Arguments:
- CDN PoP
- IP Version (v4 / v6)
- CIDR Block of VIP space
###### Output:
- Raw DNS A records

## genVipPTRRecords.py
- Helpful for creating/appending raw DNS PTR records to zone files to be imported into DNS systems.
- Slightly redacted for privacy reasons
###### Arguments:
- CDN PoP
- IP Version (v4 / v6)
- CIDR Block of VIP space
###### Output:
- Raw DNS PTR records
