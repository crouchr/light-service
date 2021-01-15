# sample program for how to use the functions
# use the rest api

import time
import call_rest_api

listen_port = 9503
endpoint_base = 'http://192.168.1.180:' + listen_port.__str__() # mrdell


def main():
    try:
        sleep_mins = 1
        sleep_secs = sleep_mins * 60

        query = {}
        query['app_name'] = 'hello_light_use_rest_api'

        status_code, response_dict = call_rest_api.call_rest_api(endpoint_base + '/status', query)

        fp_out = open('../data/lux.tsv', 'w')

        while True:

            status_code, response_dict = call_rest_api.call_rest_api(endpoint_base + '/get_lux', query)
            lux = response_dict['lux']
            lux_rec = time.ctime() + '\t' + lux.__str__()
            fp_out.write(lux_rec + '\n')
            fp_out.flush()
            print(lux_rec)
            time.sleep(sleep_secs)

    except Exception as e:
        print(e.__str__())


if __name__ == '__main__':
    main()
