black_list = [
    '72.49.34.255', '12.46.37.189',
    '85.42.75.33', '212.23.25.155',
]
white_list = [
    '63.72.182.120', '227.63.41.210',
]
ip_access_lists = {
    'black list': black_list,
    'white list': white_list,
}

def is_access_allowed(ip_address, mode, ip_access_lists):
    match mode:
        case 1:
            if ip_address not in ip_access_lists['black list']:
                return 'ДА'
            else:
                return 'НЕТ'
        case 2:
            if ip_address in ip_access_lists['white list']:
                return 'ДА'
            else:
                return 'НЕТ'

print(
    is_access_allowed(
        '63.42.140.120',
        3,
        ip_access_lists,
    )
)