import gspread
from oauth2client.service_account import ServiceAccountCredentials

#escopo
scope = ['https://spreadsheets.google.com/feeds']

#autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)

#planilha_id
wks = gc.open_by_key('1b-GkDhhxJIwWcA6tk3z4eX58f-f1w2TA2f2XrI4XB1w')

#define qual pagina será a pesquisa
dt_atualizacao = wks.get_worksheet(9)
confirmados = wks.get_worksheet(13)
descartados = wks.get_worksheet(1)
obitos = wks.get_worksheet(15)
altas_medicas = wks.get_worksheet(12)

#faz o get por linha e coluna
print('data: ', dt_atualizacao.cell(2, 1).value)
print('confirmados: ', confirmados.cell(2, 3).value)
print('descartados: ', descartados.cell(2, 3).value)
print('obitos: ', obitos.cell(2, 3).value)
print('altas_medicas: ', altas_medicas.cell(2, 3).value)
