FROM mcr.microsoft.com/powershell

WORKDIR /app

SHELL ["pwsh", "-Command"]

RUN Install-Module -Name Pode -Force

ADD ["webapp.ps1", "/app/"]

CMD ["pwsh", "-File", "webapp.ps1"]