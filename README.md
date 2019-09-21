# WP Sniffer
Will detect information about a WordPress site including
- Core version
- Plugins and their versions
- Theme in use and its version

### Additional features include
- Can detect all plugins available on WordPress.org
- List of WordPress.org plugins are parsed into a CSV file for easy processing by other programs 
- Comes with `JSON` and `XML` formatters
- Write your own formatters so you can fully control the output

The tests are enumerative so the results may not always be 100% accurate

## Getting started
1. Install all required package in `requirements.txt` using `pip`
2. WP Sniffer uses Pythons venv system to isolate your development environment. Run the scan using `./venv/bin/python ./wp_sniffer.py`

## Creating your own formatter
1. Copy and paste one of the default formatters (either `json.py` or `xml.py`) found in the `output_formatters` directory
2. Make sure the file contains a `format_output` with one argument. The results argument will be a `list` of `dictionaries`. Whatever you return becomes the outputted result
3. Update the `OUTPUT_FORMATTER` variable in `.env` to the name of your new formatter file