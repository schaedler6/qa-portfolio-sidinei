# Criar estrutura padronizada para evidências de QA

$Data = Get-Date -Format "yyyy-MM-dd"
$Base = "..\relatorios\evidencias\$Data"

$Pastas = @(
    "prints",
    "videos",
    "logs",
    "relatorios",
    "bugs"
)

foreach ($Pasta in $Pastas) {
    $Caminho = Join-Path $Base $Pasta
    New-Item -ItemType Directory -Force -Path $Caminho | Out-Null
}

$Readme = Join-Path $Base "README.md"

@"
# Evidências de QA — $Data

## Estrutura

- prints/
- videos/
- logs/
- relatorios/
- bugs/

## Uso

Salvar aqui evidências coletadas durante execução de testes manuais, testes de API, validações visuais e automações.
"@ | Set-Content -Path $Readme -Encoding UTF8

Write-Host "Estrutura de evidências criada em:" -ForegroundColor Green
Write-Host $Base
