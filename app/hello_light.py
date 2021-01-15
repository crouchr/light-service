import time
import light_sensor


def main():
    try:
        sleep_mins = 1
        sleep_secs = sleep_mins * 60

        sensor = light_sensor.register_light_sensor()

        fp_out = open('../data/lux.tsv', 'w')

        while True:
            lux = light_sensor.get_lux(sensor)
            lux_rec = time.ctime() + '\t' + lux.__str__()
            fp_out.write(lux_rec + '\n')
            fp_out.flush()
            print(lux_rec)
            time.sleep(sleep_secs)

    except Exception as e:
        print(e.__str__())


if __name__ == '__main__':
    main()
