import timeit

# Алгоритм Бойєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0: return 0
    last = {}
    for k in range(m):
        last[pattern[k]] = k
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i = i + m - min(k, j + 1)
            k = m - 1
    return -1

# Алгоритму Кнута-Морріса-Пратта
def knuth_morris_pratt(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    j = 0
    computeLPSArray(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def computeLPSArray(pattern, m, lps):
    length = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Алгоритму Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    for i in range(m-1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == m:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1

# Читання файлів
with open('article1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

with open('article2.txt', 'r', encoding='utf-8') as file:
    text2 = file.read()

# Вибір підрядків для тестування
substring_exists1 = 'реалізації відомих алгоритмів' 
substring_not_exists1 = 'some text from anywhere' 

substring_exists2 = 'використано колаборативну фільтрацію' 
substring_not_exists2 = 'some text from anywhere'  

# Вимірювання часу виконання кожного алгоритму
def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1)

# Вимірювання для статті 1
time_boyer_moore_exist1 = measure_time(boyer_moore, text1, substring_exists1)
time_knuth_morris_pratt_exist1 = measure_time(knuth_morris_pratt, text1, substring_exists1)
time_rabin_karp_exist1 = measure_time(rabin_karp, text1, substring_exists1)

time_boyer_moore_not_exist1 = measure_time(boyer_moore, text1, substring_not_exists1)
time_knuth_morris_pratt_not_exist1 = measure_time(knuth_morris_pratt, text1, substring_not_exists1)
time_rabin_karp_not_exist1 = measure_time(rabin_karp, text1, substring_not_exists1)

# Вимірювання для статті 2
time_boyer_moore_exist2 = measure_time(boyer_moore, text2, substring_exists2)
time_knuth_morris_pratt_exist2 = measure_time(knuth_morris_pratt, text2, substring_exists2)
time_rabin_karp_exist2 = measure_time(rabin_karp, text2, substring_exists2)

time_boyer_moore_not_exist2 = measure_time(boyer_moore, text2, substring_not_exists2)
time_knuth_morris_pratt_not_exist2 = measure_time(knuth_morris_pratt, text2, substring_not_exists2)
time_rabin_karp_not_exist2 = measure_time(rabin_karp, text2, substring_not_exists2)

# Результати
print(f"Стаття 1 - підрядок існує в тексті:")
print(f"Boyer-Moore: {time_boyer_moore_exist1}")
print(f"Knuth-Morris-Pratt: {time_knuth_morris_pratt_exist1}")
print(f"Rabin-Karp: {time_rabin_karp_exist1}")

print(f"Стаття 1 - вигаданий підрядок:")
print(f"Boyer-Moore: {time_boyer_moore_not_exist1}")
print(f"Knuth-Morris-Pratt: {time_knuth_morris_pratt_not_exist1}")
print(f"Rabin-Karp: {time_rabin_karp_not_exist1}")

print(f"Стаття 2 - підрядок існує в тексті:")
print(f"Boyer-Moore: {time_boyer_moore_exist2}")
print(f"Knuth-Morris-Pratt: {time_knuth_morris_pratt_exist2}")
print(f"Rabin-Karp: {time_rabin_karp_exist2}")

print(f"Стаття 2 - вигаданий підрядок:")
print(f"Boyer-Moore: {time_boyer_moore_not_exist2}")
print(f"Knuth-Morris-Pratt: {time_knuth_morris_pratt_not_exist2}")
print(f"Rabin-Karp: {time_rabin_karp_not_exist2}")

# Визначення найшвидшого алгоритму для кожного тексту та в цілому
def find_fastest(times):
    return min(times, key=lambda x: x[1])

fastest_exist1 = find_fastest([
    ("Boyer-Moore", time_boyer_moore_exist1),
    ("Knuth-Morris-Pratt", time_knuth_morris_pratt_exist1),
    ("Rabin-Karp", time_rabin_karp_exist1)
])

fastest_not_exist1 = find_fastest([
    ("Boyer-Moore", time_boyer_moore_not_exist1),
    ("Knuth-Morris-Pratt", time_knuth_morris_pratt_not_exist1),
    ("Rabin-Karp", time_rabin_karp_not_exist1)
])

fastest_exist2 = find_fastest([
    ("Boyer-Moore", time_boyer_moore_exist2),
    ("Knuth-Morris-Pratt", time_knuth_morris_pratt_exist2),
    ("Rabin-Karp", time_rabin_karp_exist2)
])

fastest_not_exist2 = find_fastest([
    ("Boyer-Moore", time_boyer_moore_not_exist2),
    ("Knuth-Morris-Pratt", time_knuth_morris_pratt_not_exist2),
    ("Rabin-Karp", time_rabin_karp_not_exist2)
])

print(f"Найшвидший для статті 1 - підрядок існує в тексті: {fastest_exist1}")
print(f"Найшвидший для статті 1 - вигаданий підрядок: {fastest_not_exist1}")
print(f"Найшвидший для статті 2 - підрядок існує в тексті: {fastest_exist2}")
print(f"Найшвидший для статті 2 - вигаданий підрядок: {fastest_not_exist2}")
