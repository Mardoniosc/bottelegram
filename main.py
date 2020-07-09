# coding=utf-8
import os
import telebot
import urllib
import json

bot = telebot.TeleBot(os.environ['SPACE_BOT_TOKEN'])

@bot.message_handler(commands=['start', 'help'])
def send_start_message(message):
  bot.reply_to(message, 'Olá '+ message.from_user.first_name 
                        +", eu sou o Donio "
                        "\nAbaixo a lista de comandos que eu respondo"
                        "\n/people para saber quais "
                        "pessoas estão no espaço nesse momento."
                        "\n/olá, /oi, /oii, /eae para um comprimento amigavel"
                        "\n/frase para um frase aleátoria"
                        "\n/start ou /help para mostrar os comandos novamente"
                        "\n\n /info para informações sobre bot e seu desenvolvedor"
                        )

@bot.message_handler(commands=['info'])
def send_people(message):
  bot.reply_to(message, 'Olá meu nome é Donio\n'
                        'Fui criado por Mardonio S Costa com BotFather'
                        '\nUltima atualização: 09/07/2020'
                        '\nCodigo fonte disponivel no github: https://github.com/Mardoniosc/bottelegram'
                        '\nPara mais informações pode entrar em contato com @Mardoniosc no telegram'
                        )

@bot.message_handler(commands=['people'])
def send_people(message):
  bot.reply_to(message, get_reply_message())

def get_reply_message():
  n_people, people = get_people()
  message = "Existem " \
            + str(n_people) + \
            " pessoas no espaço neste momento, são elas: \n\n"
  for person in people:
    message += person["name"] + \
                " na espaçonave " + person["craft"] + "\n\n"
  return message

@bot.message_handler(commands=['frase'])
def send_frase(message):
  frase = get_frase_random()
  bot.reply_to(message, frase)

def get_people():
  req = "http://api.open-notify.org/astros.json"
  response = urllib.request.urlopen(req)
  obj = json.loads(response.read())
  return obj["number"], obj["people"]

@bot.message_handler(commands=['oi', 'olá', 'oii', 'eae'])
def send_cumprimento(message):
    bot.reply_to(message, get_cumprimento_message(message))

def get_cumprimento_message(msg):
    return 'Olá '+ msg.from_user.first_name +  ', Legal poder falar com você'

def get_frase_random():
  req = "https://allugofrases.herokuapp.com/frases/random"
  response = urllib.request.urlopen(req)
  obj = json.loads(response.read())
  mensagem = obj['frase'] + "\nLivro: " + obj['livro'] \
              + "\nAuthor: " + obj['autor']

  return mensagem

bot.polling()