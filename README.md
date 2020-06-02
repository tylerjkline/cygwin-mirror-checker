# Cygwin Mirror Checker

This will fetch, scan, analyze the response times of all Cygwin mirror servers, ranks them by speed (how fast servers responded, quickest first response)), and reports the state/area that server is in.

![Usage of cygwin mirror checker](https://github.com/tylerjkline/cygwin-mirror-checker/raw/Staging/Cygwin.gif)

The reason I did this is that it's been 4 years since the last time someone posted this script, so until now, it hasn't been updated, and given great looks... 

Just a great script that was outdated and needed a nice polishing, couldn't find anyone else who did it, so I did.
## Dependencies

Python version 3.0 or higher, the PyPI Request package, and that's it.

```bash
sudo apt-get update && sudo apt-get install python3 && sudo apt-get install python3-pip && python3 -m pip install request
```
## Installation
```bash
$ git clone https://github.com/tylerjkline/cygwin-mirror-checker
$ cd cygwin-mirror-checker
```

## Usage
Cygwin-mirrors.py takes no arguments and can only be run as shown here:

```bash
$ python3 cygwin-mirrors.py
```

## Contributing
Pull requests are welcome, please leave recommendations on improvements or problems in their appropriate sections and I'll do my best to fix them.

## License
[This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.](https://creativecommons.org/licenses/by-nc/4.0/)
