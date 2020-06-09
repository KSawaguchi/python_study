from termcolor import colored

print(colored("""######################################################\n
こんにちは！私はRobotaです。あなたの名前は何ですか？\n
######################################################""", 'green'))

while True:
    name = input('')
    if name != '':
        break