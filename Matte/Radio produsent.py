    #a)

    def f(måneder):
        total = 580
        for i in range(måneder):
            total += 580+(30*(i-1))
            print(f'Måned {i+1}: {580+(30*(i))} radioer')
        return total

    def e(måneder):
        radioer = 580+(30*(måneder-1))

    print(f'Det ble totalt produsert {f(12)} radioer i 2021.')
    print(f'I Desember 2026 ble det produsert {e(72)} radioer.')

    8940
    7210