# ----- Bucles
# do while -- while -- do until -- for -- foreach 
# $true 
$opciones = "si Si SI sí Sí SÍ sÍ"
# do {
#    $resp = Read-Host "¿Desea salir?"
#    $bol = $opciones.indexOf($resp) -lt 0
#    if ($bol)
#    {
#        Write-Host "Has pulsado una opcion incorrecta"
#    }
# } while ($bol)
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