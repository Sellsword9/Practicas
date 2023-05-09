# ----- Bucles
# do while -- while -- do until -- for -- foreach 
clear
$n = 0
while ($n -lt 10) {
    $n++
    Write-Host $n
}
Read-Host "Pulsa intro para continuar"
clear
foreach ($vari in 1..99)
{
    $r = [math]::Sqrt($vari)
    Write-Host [$r]
}
Read-Host "Pulsa intro para continuar"
#Otro foreach
Clear-Host
$ruta = "C:\Windows"
$pregunta = Read-Host "Introduce el fichero a buscar"


foreach ($fich in Get-ChildItem $ruta)
{
    if ($fich.Name.IndexOf($pregunta) -ge 0)
    {
        Write-Host $fich.Name
    }
}