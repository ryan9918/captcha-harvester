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
  - The most important step is to know how to edit your hosts file. You can find out how to do this with a simple google search. You will need to add an entry to your hosts file like so `127.0.0.1 harvester.DOMAIN-HERE` - replacing DOMAIN-HERE with the domain you are harvesting for e.g. supremenewyork.com or adidas.com or sneakersnstuff.com
  - Open config.json in an editor such as atom or sublime and make the necessary changes to the file. Making sure the domain is entered without the `www` and the sitekey is correct and the latest one available
  - cd into the directory of the repository
  - `python main.py` to run the script
  
  To request tokens from the server, you must send a GET request to `http://harvester.DOMAIN-HERE:5000/api/token`. The token that is set to expire next will be returned in json format.
  If there is a valid token available:
  ```javascript
  {"success": true, "error": null, "result": "TOKEN-HERE"}
  ```
  Or if there are no tokens available:
   ```javascript
  {"success": false, "error": "ERROR-HERE", "result": null}
  ```
  Note: An alternative to this is to use the built-in python function `sendToken` from your own script which will only return when there is a token available. Using requests is generally much cleaner and therefore a better option.
  
## FAQ
  - The captcha solving page will not load... *attempt to reload it manually and check you edited your hosts file correctly*
