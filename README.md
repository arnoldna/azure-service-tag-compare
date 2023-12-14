# azure-service-tag-compare

Compares the AzureCloud service tag CIDR against all other service tags.

## Setup

Assumes Python is already installed.

Open a command prompt and navigate to the folder with the `requirements.txt` file.

Execute the following command to install the required Python modules:

``` python
pip install -r requirements.
```

Download the required service tag file from Microsoft and save it to same folder as the `requirements.txt` file.
Azure US Government = <https://www.microsoft.com/en-us/download/details.aspx?id=57063>
Azure Commercial (Public Cloud) = <https://https://www.microsoft.com/en-us/download/details.aspx?id=56519>

Execute the following command to execute the script:

```python
python.exe serviceTagCompare.py
```

If there are any missing CIDRs the Azure Service Tag and missing IP Address are displayed.