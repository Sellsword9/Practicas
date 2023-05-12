clear
$usuario = Read-Host("Introduce el nombre de un usuario")
if ((Get-LocalUser).name.contains($usuario)) {
    Write-Host("Usuario ya existente")
}else
{
    $contra = Read-Host("Introduce la contraseña para el nuevo usuario")
    $sec = ConvertTo-SecureString $contra -AsPlainText -Force
    New-LocalUser -Password $sec -Name $usuario -Verbose
}