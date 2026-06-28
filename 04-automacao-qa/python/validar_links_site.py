import urllib.request
import urllib.error
from datetime import datetime

URLS = [
    "https://sid.dev.br",
    "https://github.com/schaedler6",
    "https://github.com/schaedler6/qa-portfolio-sidinei",
    "https://www.linkedin.com/in/sidschaedler/"
]

def verificar_url(url: str) -> dict:
    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "QA-Portfolio-Sidinei/1.0"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            return {
                "url": url,
                "status": response.status,
                "ok": 200 <= response.status < 400,
                "erro": ""
            }

    except urllib.error.HTTPError as erro:
        return {
            "url": url,
            "status": erro.code,
            "ok": False,
            "erro": str(erro)
        }

    except Exception as erro:
        return {
            "url": url,
            "status": "N/A",
            "ok": False,
            "erro": str(erro)
        }

def main() -> None:
    print("# Relatório de Validação de Links")
    print()
    print(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print("| URL | Status | Resultado | Erro |")
    print("|---|---:|---|---|")

    for url in URLS:
        resultado = verificar_url(url)
        status_texto = "OK" if resultado["ok"] else "FALHA"
        print(
            f"| {resultado['url']} | {resultado['status']} | "
            f"{status_texto} | {resultado['erro']} |"
        )

if __name__ == "__main__":
    main()
