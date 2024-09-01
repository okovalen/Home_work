""" Домашнее задание на тему "Форматирование строк". """

#  С использованием %

team1_num = 5
team2_num = 6
print("В команде 'Мастера кода' участников: %s!" % team1_num)
print("В команде 'Волшебники данных' участников: %s!" % team2_num)
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

#  format()

score_1 = 40
team1_time = 1552.512
score_2 = 42
team2_time = 2153.31451

print("Команда 'Волшебники данных' решила задач: {}!".format(score_1))
print("Команда 'Мастера кода' решила задач: {}!".format(score_2))
print("'Волшебники данных' решили задачи за {}!".format(team1_time))
print("'Мастера кода' решили задачи за {}!".format(team2_time))

#  f строка

tasks_total = score_1 + score_2
# tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
# print(tasks_total)

print(f'Количество решённых задач командой "Волшебники данных": {score_1} и командой "Мастера кода": {score_2}.')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = "Победа команды 'Волшебники Данных'!"
else:
    challenge_result = "Ничья!"

print(f'Итоги соревнования: {challenge_result}')

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
