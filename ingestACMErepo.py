import os
import time
import requests

def addRepo(repoPath, acmeRepoFiles):
    for category, urls in acmeRepoFiles.items():
        categoryPath = os.path.join(repoPath, category)
        os.makedirs(categoryPath, exist_ok=True)
        for url in urls:
            # Fetch raw text
            response = requests.get(url)
            if response.status_code == 200:
                filename = url.split("/")[-1]
                with open(os.path.join(categoryPath, filename), "w", encoding="utf-8") as f:
                    f.write(f"Source Code: {url}\n\n")
                    f.write(response.text)
                print(f"Saved Code: {category}/{filename}")
            time.sleep(1) 

if __name__ == "__main__":  
    repoPath = "rawData/implementations/acmeCode" 
    acmeRepoFiles = {
    "Configuration": [
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/acme/init/acme.ini.default",
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/README.md"
    ],
    "Scripts_and_Automation": [
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/acme/init/init.as",
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/acme/init/startup.as"
    ],
    "Resource_Logic": [
        # These define how ACME handles specific oneM2M resources
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/acme/resources/AE.py",
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/acme/resources/CNT.py",
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/acme/resources/CIN.py",
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/acme/resources/SUB.py",
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/acme/resources/GRP.py"
    ],
    "Validation_and_Types": [
        # This is the "Core Logic" for how ACME validates oneM2M attributes
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/acme/services/Validator.py",
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/acme/etc/Types.py"
    ],
    "Examples_and_Testing": [
        # These show the AI how to actually form a request
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/tests/testAE.py",
        "https://raw.githubusercontent.com/ankraft/ACME-oneM2M-CSE/master/tests/testCNT.py"
    ]
    }
    addRepo(repoPath, acmeRepoFiles)