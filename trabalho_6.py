#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#
#~# Maria Eduarda Nascimento Andrade ~#
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

def main():
    days = int(input())

    stocks = []
    for _ in range(days): # cria uma lista que armazena os valores diários 
        stocks.append(float(input()))

    range_buy_sell = int(input()) # tempo máximo entre compra e venda
    wallet = float(input())
     
    max_profit = -1 # não existe lucro máximo negativo, o maior seria 0 no pior dos casos
    for idx in range(len(stocks) - range_buy_sell + 1): # iteração limitada pelo máximo de dias
        max_idx = idx + range_buy_sell + 1
        limited_stocks = stocks[idx:max_idx] # vai iterar em fatias que vai do seu index atual, até o máximo
        profit, buy_value, sell_value, purchased_stocks, buy_idx, sell_idx = get_max_profit(limited_stocks, wallet) # variáveis que recebem o retorno da função
        
        buy_idx += idx + 1 # dia da compra
        sell_idx += idx + 1 # dia da venda
        if profit > max_profit:
            max_profit = profit # atualiza max profit
            result = profit, buy_value, sell_value, purchased_stocks, buy_idx, sell_idx  # result armazena as variáveis
    
    
    print(f"Dia da compra: {result[4]}")
    print(f"Valor de compra: R$ {result[1]:.2f}")
    print(f"Dia da venda: {result[5]}")
    print(f"Valor de venda: R$ {result[2]:.2f}")
    print(f"Quantidade de acoes compradas: {int(result[3])}")
    print(f"Lucro: R$ {result[0]:.2f}")
    

def get_max_profit(stocks, money):
    
    max_profit = -1
    for idx_buy in range(len(stocks)): # armazena o index da compra enquanto itera
        for idx_sell in range(idx_buy, len(stocks)): # armazena o index da venda enquanto itera
            buy_value = stocks[idx_buy] 
            sell_value = stocks[idx_sell] 
            profit_by_stock = sell_value - buy_value
            purchased_stocks = money // buy_value
            profit = purchased_stocks * profit_by_stock
            if profit > max_profit:
                max_profit = profit
                result = (profit, buy_value, sell_value, purchased_stocks, idx_buy, idx_sell)
                
    return result

main()