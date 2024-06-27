def check_comments(comment, swear_words):
    words = comment.split()  # Разбиваем комментарий на отдельные слова
    
    for word in words:
        if word.lower() in swear_words:  # Проверяем каждое слово на наличие матерных слов
            return True  # Если найдено матерное слово, возвращаем True
    
    return False  # Если матерных слов не найдено, возвращаем False

# Список матерных слов, которые будем проверять
swear_words = {"bad", "rude", "vulgar", "offensive"}

# Пример использования функции
comment1 = "This is a clean comment"
comment2 = "This is a rude comment with bad language"
comment3 = "Another clean comment without any offensive words"

if check_comments(comment1, swear_words):
    print("Comment 1 contains swear words. Block the comment.")
else:
    print("Comment 1 is clean. Allow the comment.")

if check_comments(comment2, swear_words):
    print("Comment 2 contains swear words. Block the comment.")
else:
    print("Comment 2 is clean. Allow the comment.")

if check_comments(comment3, swear_words):
    print("Comment 3 contains swear words. Block the comment.")
else:
    print("Comment 3 is clean. Allow the comment.")
