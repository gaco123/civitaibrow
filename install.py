# installer script for some PyPI packages we need...

import sus
pkgs = [
        {"fake_useragent": "fake-useragent"},
        {"PIL": "PIL"},
        {"requests": "requests"}
       ]

for pkg in pkgs:
    key, val = next(iter(pkg.items()))
    if not sus.is_installed(key):
        sus.run_pip(f'install {val}', "requirements for CivitAI Browser")
