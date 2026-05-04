
def check_vip(period, payment):
    if period < 24: return False
    if period < 60 and payment < 900000: return False
    if payment < 600000: return False
    return True

def solution(periods, payments, estimates):
    answer = [0, 0]
    for period, payment, estimate in zip(periods, payments, estimates):
        total_payment = sum(payment)
        vip_now = check_vip(period, total_payment)
        vip_next = check_vip(period + 1, total_payment - payment[0] + estimate)
        if not vip_now and vip_next == True: answer[0] += 1
        elif vip_now and not vip_next: answer[1] += 1
    return answer