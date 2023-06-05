Clear-Host
# Pedir numero y un nombre generico
do
{
[int64]$numero = Read-Host "Introduce un numero mayor que 1 y menor que 50"
if ($numero -lt 1 -or $numero -ge 50)
{
    Write-Host "Error: Introduce un numero entre 1 y 50"
}
}while($numero -lt 1 -or $numero -ge 50)

$nombre = read-host "Introduzca un nombre generico para la creacion de users"

foreach ($user in 1..$numero)
{
    Write-Host $nombre$user
}

# Dominios

(Get-ADDomain).name
New-ADOrganizationalUnit -Name "OU_Cadiz" -Path "OU=OU_PROINSA, DC=primerodaw, DC=local"
Remove-ADOrganizationalUnit -Identity "OU=OU_Cadiz, OU=OU_PROINSA,DC=primerodaw,DC=local" # -Confirm $true

