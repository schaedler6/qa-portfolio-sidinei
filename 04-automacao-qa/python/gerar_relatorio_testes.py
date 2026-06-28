from datetime import datetime
from pathlib import Path

CASOS = [
    {
        "id": "CT-001",
        "cenario": "Carregar página inicial",
        "status": "Pendente"
    },
    {
        "id": "CT-002",
        "cenario": "Validar hero profissional",
        "status": "Pendente"
    },
    {
        "id": "CT-003",
        "cenario": "Validar seção Portfólio QA",
        "status": "Pendente"
    },
    {
        "id": "CT-004",
        "cenario": "Validar links externos",
        "status": "Pendente"
    }
]

def gerar_relatorio() -> str:
    linhas = [
        "# Relatório Automatizado de Testes",
        "",
        f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "| ID | Cenário | Status |",
        "|---|---|---|"
    ]

    for caso in CASOS:
        linhas.append(f"| {caso['id']} | {caso['cenario']} | {caso['status']} |")

    linhas.extend([
        "",
        "## Observação",
        "",
        "Relatório gerado automaticamente como exemplo de automação para QA."
    ])

    return "\n".join(linhas)

def main() -> None:
    saida = Path("../relatorios/relatorio-automatizado-testes.md")
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(gerar_relatorio(), encoding="utf-8")
    print(f"Relatório gerado em: {saida}")

if __name__ == "__main__":
    main()
