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