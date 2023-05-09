# Ejecicio de práctica
# Preguntar que de un numero hasta que sea uno entre el 1 y el 10
$ValidNums = ""
do
{
    $ValidNums += 1..10
    $num = Read-Host "Introduce un numero"
    $b = $ValidNums.Contains($num)
    if (!$b)
    {
        Write-Host "Numero incorrecto"
    }
}
until($b)