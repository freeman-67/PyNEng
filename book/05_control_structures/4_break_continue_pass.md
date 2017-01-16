## break, continue, pass
В Python есть несколько операторов, которые позволяют менять поведение циклов по умолчанию.

### Оператор break
__Оператор break__ позволяет досрочно прервать цикл:
* break прерывает текущий цикл и продолжает выполнение следующих выражений
* если используется несколько вложенных циклов, break прерывает внутренний цикл и продолжает выполнять выражения следующие за блоком
* break может использоваться в циклах for и while


Пример с циклом for:
```python
In [1]: for num in range(10):
   ...:     if num < 7:
   ...:         print num
   ...:     else:
   ...:         break
   ...:     
0
1
2
3
4
5
6
```

Пример с циклом while:
```python
In [2]: i = 0
In [3]: while i < 10:
   ...:     if i == 5:
   ...:         break
   ...:     else:
   ...:         print i
   ...:         i += 1
   ...:         
0
1
2
3
4
```

Ещё пример:
```python
# -*- coding: utf-8 -*-

username = raw_input('Введите имя пользователя: ' )
password = raw_input('Введите пароль: ' )

while True:
    if len(password) < 8:
        print 'Пароль слишком короткий\n'
        password = raw_input('Введите пароль еще раз: ' )
    elif username in password:
        print 'Пароль содержит имя пользователя\n'
        password = raw_input('Введите пароль еще раз: ' )
    else:
        print 'Пароль для пользователя %s установлен' % username
        break
```

### Оператор continue
Оператор continue возвращает управление в начало цикла. То есть, continue позволяет "перепрыгнуть" оставшиеся выражения в цикле и вернуться в начало цикла.

Пример с циклом for:
```python
In [4]: for num in range(5):
   ...:     if num == 3:
   ...:         continue
   ...:     else:
   ...:         print num
   ...:         
0
1
2
4
```

Пример с циклом while:
```python
In [5]: i = 0
In [6]: while i < 6:
   ....:     i += 1
   ....:     if i == 3:
   ....:         print "Пропускаем 3"
   ....:         continue
   ....:         print "Это никто не увидит"
   ....:     else:
   ....:         print "Текущее значение: ", i
   ....:         
Текущее значение:  1
Текущее значение:  2
Пропускаем 3
Текущее значение:  4
Текущее значение:  5
Текущее значение:  6
```

### Оператор pass
Оператор pass ничего не делает. Фактически это такая заглушка для объектов.

Например, Вы придумали как будет выглядеть скрипт, но, прежде чем писать его, Вы решили прописать структуру скрипта.

В таких случаях pass очень помогает. Его можно ставить в циклах, функциях, классах. И это не будет влиять на исполнение кода.

Пример использования pass:
```python
In [6]: for num in range(5):
   ....:     if num < 3:
   ....:         pass
   ....:     else:
   ....:         print num
   ....:         
3
4
```
