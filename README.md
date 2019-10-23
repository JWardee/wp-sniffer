# WP Sniffer
Will detect information about a WordPress site including
- Core version
- Plugins and their versions
- Theme in use and its version

## Additional features include
- Can detect all plugins available on WordPress.org
- List of WordPress.org plugins are parsed into a CSV file for easy processing by other programs 
- Comes with `JSON` and `XML` formatters
- Write your own formatters so you can fully control the output

The tests are enumerative so the results may not always be 100% accurate

## Getting started
1. Install all required packages in `requirements.txt` using `pip`
2. Copy `.env.sample`, name it `.env` and update any values
3. Run the scan using `./wp_sniffer/wp_sniffer` on screen instructions will guide you from there

## Running a scan programatically
1. Import the scan manager `from wp_sniffer.scan_manager import ScanManager`
2. Call the `run_all` method passing the url to scan - eg `ScanManager().run_all('http://my-wordpress-site.com')`

## Forking the repo and building
1. Fork the repo as normal and make any changes you'd like
2. To build run: `python3 setup.py bdist_wheel` **NOTE: Your `.env` file is also built into the package not `.env.sample`**
3. In your other python project you can install your fork by calling `pip install LOCATION_OF_YOUR_setup.py_FILE_HERE --no-cache-dir`

## Creating your own formatter
1. Copy and paste one of the default formatters (either `json.py` or `xml.py`) found in the `output_formatters` directory
2. Make sure the file contains a `format_output` with one argument. The results argument will be a `list` of `dictionaries`. Whatever you return becomes the outputted result
3. Update the `OUTPUT_FORMATTER` variable in `.env` to the name of your new formatter file