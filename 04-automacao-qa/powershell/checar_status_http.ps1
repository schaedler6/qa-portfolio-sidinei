# Checagem simples de status HTTP para URLs do portfólio

$Urls = @(
    "https://sid.dev.br",
    "https://github.com/schaedler6",
    "https://github.com/schaedler6/qa-portfolio-sidinei",
    "https://www.linkedin.com/in/sidschaedler/"
)

$Resultados = foreach ($Url in $Urls) {
    try {
        $Resposta = Invoke-WebRequest -Uri $Url -Method Head -TimeoutSec 10 -ErrorAction Stop

        [PSCustomObject]@{
            URL = $Url
            StatusCode = $Resposta.StatusCode
            Resultado = "OK"
            Erro = ""
        }
    }
    catch {
        [PSCustomObject]@{
            URL = $Url
            StatusCode = "N/A"
            Resultado = "FALHA"
            Erro = $_.Exception.Message
        }
    }
}

$Resultados | Format-Table -AutoSize

$Saida = "..\relatorios\status-http.csv"
New-Item -ItemType Directory -Force -Path "..\relatorios" | Out-Null
$Resultados | Export-Csv -Path $Saida -NoTypeInformation -Encoding UTF8

Write-Host "Relatório salvo em: $Saida" -ForegroundColor Green
