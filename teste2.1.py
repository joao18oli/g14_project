# Marta's test


import datetime

# =========================
# BASE DE DADOS
# =========================
db = 'Airport airlines - original (com dados do csv).db'

# =========================
# ESCOLHER CLASSE
# =========================

# # -------- Airport --------
# from classes.airport import Airport
# test_class = Airport
# ob = (0, "1990-01-01", "Aeroporto Francisco Sá Carneiro")

# -------- Airline --------
# from classes.airline import Airline
# test_class = Airline
# ob = (0, "TAP", "Premium")

# -------- Terminal --------
# from classes.terminal import Terminal
# from classes.airport import Airport
# Airport.read('data/' + db)  
# test_class = Terminal
# ob = (0, "Terminal A", 1)

# -------- Voo --------
from classes.voo import Voo
from classes.airport import Airport
from classes.airline import Airline
Airport.read('data/' + db)
Airline.read('data/' + db)
test_class = Voo
ob = (0, 1, 1, "2026-01-01", 150)

# =========================

# Ler dados
test_class.read('data/' + db)

op = ''

while op != 'q':
    print('\nChoose option')
    print('---------------')
    print('l - list')
    print('b - beginning')
    print('n - next')
    print('p - previous')
    print('e - end')
    print('---------------')
    print('i - insert')
    print('m - modify')
    print('r - remove')
    print('---------------')
    print('s - sort')
    print('f - find')
    print('---------------')
    print('q - quit')
    print('---------------')

    p = test_class.current()
    print(f'\nCurrent: {p}')

    op = input('? ')

    # =====================
    # NAVEGAÇÃO
    # =====================
    if op == 'b':
        test_class.first()

    elif op == 'n':
        test_class.nextrec()

    elif op == 'p':
        test_class.previous()

    elif op == 'e':
        test_class.last()

    # =====================
    # INSERT
    # =====================
    elif op == 'i':

        if len(test_class.lst) == 0:
            p = test_class(*ob)

        fields = list(p.__dict__.keys())

        print('leave blank = auto id')
        id = input(f'{fields[0][1:]} = ')
        id = int(id) if id else 0

        values = [id]

        for att in fields[1:]:
            atype = type(getattr(p, att))
            val = input(f'{att[1:]} = ')

            if atype == int:
                values.append(int(val))
            else:
                values.append(val)

        # criar objeto 
        obj = test_class(*values)

        test_class.insert(obj.id)

    # =====================
    # MODIFY
    # =====================
    elif op == 'm':
        fields = list(p.__dict__.keys())

        id = input(f'{fields[0][1:]} = ')
        if id:
            id = int(id)
            obj = test_class.current(id)

            if obj:
                print('leave blank = keep value')

                for att in fields[1:]:
                    val = input(f'{att[1:]} = ')
                    if val != "":
                        atype = type(getattr(obj, att))

                        if atype == int:
                            setattr(obj, att, int(val))
                        else:
                            setattr(obj, att, val)

                test_class.update(id)

    # =====================
    # REMOVE
    # =====================
    elif op == 'r':
        id = int(input('id = '))

        if id in test_class.lst:
            print(test_class.obj[id])
            if input('Confirm delete (y/n)? ').lower() == 'y':
                test_class.remove(id)

    # =====================
    # LIST
    # =====================
    elif op == 'l':
        for code in test_class.lst:
            print(test_class.obj[code])

    # =====================
    # SORT
    # =====================
    elif op == 's':
        attrib = input('attribute (sem _): ')
        key = '_' + attrib

        if key in p.__dict__:
            reverse = input('reverse? (y/n): ').lower() == 'y'
            current_id = p.id

            test_class.sort(key, reverse)

            for code in test_class.lst:
                print(test_class.obj[code])

            test_class.current(current_id)

    # =====================
    # FIND
    # =====================
    elif op == 'f':
        attrib = input('attribute (sem _): ')
        key = '_' + attrib

        if key in p.__dict__:
            atype = type(getattr(p, key))
            value = input('value: ')

            if atype == int:
                value = int(value)

            results = test_class.find(value, key)

            if results:
                test_class.current(results[0].id)
                for obj in results:
                    print(obj)