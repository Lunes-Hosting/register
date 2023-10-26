import os.path

import requests
import config
import json 

#code that deals with the subdomain.json file

def setup() -> int:
    if os.path.exists("subdomains.json"):
        return 0
    else:
        dict = {}
        for x in config.cloudflare_domain:
            dict[x] = {}
        
        # Writing to sample.json
        with open("subdomain.json", "w") as outfile:
            json.dump(dict, outfile, indent=4)
        return 0


def retrieve_j() -> dict:
    try:
        response = requests.get(config.github_subdomain_json)
        content = json.loads(response.content)
        return content
    except:
        return None



def check(domain_target: str) -> str:
    library = retrieve_j
    if library != None:

        domain = domain_target.split(".")
        if domain != 3:
            return "Bad Input"
        
        subdomain = domain[0]
        content = library[domain[1]+"."+domain[2]][subdomain[0]]
        if content == None:
            return "No one owns it"
        else:
            return "The user " + content["owner"] + " owns it."

    return None