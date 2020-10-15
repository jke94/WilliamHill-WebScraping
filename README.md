# WilliamHill-WebScraping
A William Hill scraping to get data from [William Hill football matches on direct web page]('https://sports.williamhill.es/betting/es-es/en-directo/fútbol").

## Installation

### 1. Install the python modules needed for this project.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```cmd
>pip install [module_name]
```
On this project the moduled needed are:
- datetime
- selenium
- logging
- time
- urllib
- urlvalidator
- csv
- FootballMatchEvent (from .\WilliamHill-WebScraping\src)
- coverage
- unittesting

### 2. Download chromedriver.exe, needed for this project.
IMPORTANT: It will be needed to have a [chromedriver.exe](https://chromedriver.chromium.org/downloads) on this path: '.\WilliamHill-WebScraping\tools'

## Usage

```cmd
.\WilliamHill-WebScraping\src>python SeleniumSpyder.py
```
## Data Generated
Automatically after the script execution for each match founded a CSV file will be created in the following repository path:

```cmd
.\WilliamHill-WebScraping\data>
```

## Logs
Automatically after run the script, it will generate a file 'sypderLog.log' with logs on this path:
```cmd
.\WilliamHill-WebScraping\logs>
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)