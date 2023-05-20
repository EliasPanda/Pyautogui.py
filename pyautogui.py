#instale a biblioteca pyautogui antes de fazer o programa
 #pip install pyautogui (copie e cole no seu teminal do VS ou CMD)

import pyautogui as bot 

bot.press('win') # press() ele pressiona a tecla, nesse caso mandei pressionar a tecla do windows 
bot.sleep(2) #aqui é o tempo que vc irá da para executar a proxima ação
bot.write('opera')# write() é uma função para escrever algo, nesse caso ele escreve na pesquisa do menu inicar
bot.sleep(2)#aqui é o tempo que vc irá da para executar a proxima ação
bot.press('enter')# aqui ele preciona o ENTER
bot.sleep(2) #aqui você da um tempo de pesquisa, nesse caso eu dei 1s
bot.write('https://web.whatsapp.com') #aqui você passará o endereço desejado, no nosso caso é do whats.
bot.sleep(2)#aqui é o tempo que vc irá da para executar a proxima ação
bot.press('enter')
bot.sleep(8)#poderá precisar de um tempo maior ou menor, vai depender do seu pc e sua intert.
bot.click(x=205, y=186) #aqui vc vai pegar as posições da sua tela
#(deixarei um QRcode com o codigo pra pegar as posições, da caixa de pesquisa do whhats )
bot.write('Desenvolvimento de garotos de programas')#aqui é o que será digitado na caixa de pesquisa do whats
bot.press('enter')#aqui faz a função do enter e vai direto para o contado
bot.sleep(2)#aqui é o tempo que vc irá da para executar a proxima ação
bot.write('hahaha')#aqui é a menssagem a ser enviada
bot.sleep(2)#aqui é o tempo que vc irá da para executar a proxima ação
bot.press('enter')#aqui envia a menssagem

#by: ~Elias, ~Thomas, ~Victor, ~alice, ~Allan, ~Thiago, ~Felipe


