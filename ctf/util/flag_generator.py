# Flag generator util script

import random
import string

def generate_flag_buffer(base_flag):
    randomSource = string.ascii_letters + string.digits
    flag_buffer = ''.join(random.SystemRandom().choice(randomSource) for i in range(12))
    current_flag = ("flag{%s_%s}" % (base_flag, flag_buffer))
    return current_flag


if __name__ == "__main__":
    base = "h3110_th3re"
    print(generate_flag_buffer(base))