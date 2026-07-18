inp_dic = {}
out_dic = {}

for _ in range(int(input())):
    id_car, inp_time = input().split(': ')
    inp_dic[id_car] = inp_time

for _ in range(int(input())):
    id_car, out_time = input().split(': ')
    out_dic[id_car] = out_time

for id_car, out_time in out_dic.items():
    t_o_h, t_o_m = out_time.split(':')
    t_i_h, t_i_m = inp_dic[id_car].split(':')
    t_o_h, t_o_m, t_i_h, t_i_m = int(t_o_h), int(t_o_m), int(t_i_h), int(t_i_m)
    if t_o_h < t_i_h:
        t_o_h += 24
    mins = (t_o_h * 60 + t_o_m) - (t_i_h * 60 + t_i_m)
    if mins > 120:
        print(f"{id_car}: {(mins - 120) * 3}₽")
    else:
        print(f'{id_car}: плата не взимается')
