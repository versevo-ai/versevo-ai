if (Get-Command python3 -ErrorAction SilentlyContinue) {
    Write-Host "Python 3 is installed"
} else {
    Write-Host "Python 3 is not installed"
    choco install python3
}

if (Get-Command pip3 -ErrorAction SilentlyContinue) {
    Write-Host "pip3 is installed"
} else {
    Write-Host "pip3 is not installed"
    choco install pip3
}


python3 -m venv venv
. .\venv\Scripts\activate
pip3 install -r .\requirements.txt