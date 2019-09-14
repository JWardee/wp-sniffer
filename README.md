# WP Sniffer
Will detect information about a WordPress site including
- Core version
- Plugins and their versions
- Theme in use and its version

Additional features include
- Can detect all plugins available on WordPress.org
- List of WordPress.org plugins are parsed into a CSV file for easy processing by other programs 

The tests are enumerative so the results may not always be 100% accurate

## Getting started
1. Install all required package in `requirements.txt` using `pip`
2. Copy `.env.sample` and update any values
3. Run the scan using `./venv/bin/python ./wp_sniffer.py` (WP Sniffer uses Pythons venv system to isolate your development enviroment)
