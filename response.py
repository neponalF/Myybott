import re

def process_message(message, response_array, response):
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    score = 0
    for word in list_message:
        if word in response_array:
            score += 1

    print(score, response)

    return [score, response]


def get_response(message):
    response_list = [
        process_message(
            message, ['привіт', 'ку', 'хай', 'пр', 'qq'], 'Привіт!!!'),

        process_message(message, ['як', 'справи', 'в',
                        'тебе', 'ти'], 'Все добре'),

        process_message(message, ['пока', 'покеда',
                        'бб', 'bb', 'бувай', 'pp'], 'Бувай')
    ]

    response_scores = []

    for response in response_list:
        response_scores.append(response[0])

    winning_response = max(response_scores) 
    matching_response = response_list[response_scores.index(winning_response)]

    if winning_response == 0:
        bot_response = 'Я тебе не зрозумів'
    else:
        bot_response = matching_response[1]

    print("Bot response: ", bot_response)
    return bot_response

