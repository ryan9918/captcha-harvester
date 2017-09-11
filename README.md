# Manual Captcha Harvester

## Description
This simple script allows the user to manually harvest captchas and request them from the local server when needed. The token management is handled entirely by the server.

## Requirements
  - Python 3+
  The following modules must also be installed and can be with pip e.g. `pip install colorama`
  - `colorama`
  - `termcolor`
  - `flask`
  
## Instructions
  - The most important step is to know how to edit your hosts file. You can find out how to do this with a simple google search. You will need to add an entry to your hosts file like so `127.0.0.1 cartchefs.DOMAIN-HERE` - replacing DOMAIN-HERE with the domain you are harvesting for e.g. supremenewyork.com or adidas.com or sneakersnstuff.com
  - Open config.json in an editor such as atom or sublime and make the necessary changes to the file. Making sure the domain is entered without the `www` and the sitekey is correct and the latest one available
  - cd into the directory of the repository
  - `python main.py` to run the script
  
  To request tokens from the server, you must send a GET request to `http://cartchefs.DOMAIN-HERE:5000/token`. The token that is set to expire next will be returned in text format. It is advised to only request tokens from the server right when you are about to use them.
  The alternative is to call the `sendToken` function from your own script
  
## FAQ
  - The captcha solving page will not load... *attempt to reload it manually and check you edited your hosts file correctly*
  - Can you help me... *yeah I probably could but I likely won't so try work out your own issues xox*
