from util.modbusReader import ModbusReader
from util.RedisIO import REDISIO
import util.config as config
import time
def main():
    modbus_reader = ModbusReader()
    redis_io = REDISIO(config.redis_ip, config.redis_password)
    
    while True:
        respond = modbus_reader.readHoldingReg(10000,5)
        value = {
            'timestamp':int(time.time()),
            'name': 'example_device_1',
            'rawData': respond
        }
        redis_io.pushDataToRedis('example_device_1', value)
        time.sleep(5)
if __name__ == '__main__':
    main()    
