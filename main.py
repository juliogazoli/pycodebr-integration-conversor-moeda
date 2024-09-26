from clients.callmebot_service import CallMeBot
from clients.conversor_service import CoinConversorService


conversor_service = CoinConversorService()
conversion = conversor_service.converter('BTC', 'BRL')

wpp_service = CallMeBot()
wpp_service.send_messaage(message=f'Cotação do Bitcoin: R$ {conversion}')
