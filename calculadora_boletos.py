from datetime import datetime, timedelta

def calcular_parcelas():
    print("=== Calculadora de Parcelas ===\n")

    # Entrada dos dados
    data_inicial_str = input("Data inicial (dd/mm/aaaa): ")
    intervalo_primeira = int(input("Intervalo da primeira parcela (dias): "))
    qtd_parcelas = int(input("Quantidade de parcelas: "))
    intervalo_entre = int(input("Intervalo entre parcelas (dias): "))
    valor_total = float(input("Valor total (R$): ").replace(",", "."))

    # Conversão da data
    data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y")

    # Cálculo do valor por parcela
    valor_parcela = round(valor_total / qtd_parcelas, 2)

    print("\nDatas e Valores das Parcelas:")

    for i in range(qtd_parcelas):
        if i == 0:
            data_parcela = data_inicial + timedelta(days=intervalo_primeira)
        else:
            data_parcela += timedelta(days=intervalo_entre)

        print(f"Parcela {i + 1}: {data_parcela.strftime('%d/%m/%Y')} - R$ {valor_parcela:.2f}")

if __name__ == "__main__":
    calcular_parcelas()