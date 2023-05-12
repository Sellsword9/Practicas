clear
function copiar($path1, $path2)
{
    #Función que copia los ficheros exe de un diretorio a otro

    if (Test-Path -Path $directorio)
        {
            Copy-Item -Path $path1\*.exe $path2
        }

}
function contar($path1)
{
   (Get-ChildItem -Path $path1 -File).Length
}

$directorio = Read-Host "Introduzca directorio de destino"