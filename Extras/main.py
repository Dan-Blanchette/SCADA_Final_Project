from pymodbus.client import ModbusTcpClient
import time
import json
import requests
from datetime import datetime


class plc_tag():
    def __init__(self, name, modbus_address, value):
        self.name = name
        self.modbus_address = modbus_address
        self.value = value


def connect_to_brx_plc():
    client = ModbusTcpClient('192.168.1.1', port="502") # type: ignore
    status = client.connect()
    # print(status)
    return client


def read_coils(client, coil_number, number_of_coils=1):
    # Address the offset coil
    coil_number = coil_number - 1
    result = client.read_coils(coil_number, number_of_coils)
    result_list = result.bits[0:number_of_coils]
    return result_list


def write_modbus_coil(client, coil_number, value):
    coil_number = coil_number - 1
    result = client.write_coils(coil_number, value)


def close_connection_to_click(client):
    client.close()


def pulse_stepper(client, motor_pulse_control):

    write_modbus_coil(client, motor_pulse_control.modbus_address, True)
    time.sleep(0.01)
    write_modbus_coil(client, motor_pulse_control.modbus_address, False)
    time.sleep(0.01)


def change_motor_direction(client, motor_direction_feedback, motor_direction_control):

    motor_direction = read_coils(client, motor_direction_feedback.modbus_address, 1)
    print("Changing motor direction")
    motor_direction = motor_direction[0]
    write_modbus_coil(client, motor_direction_control.modbus_address, not motor_direction)


def write_to_json_file(file_name, data_dict):
    with open(file_name, "w") as file:
        json.dump(data_dict, file)


def create_data_structure_for_cache(*args):
    # Creating tag dictionary
    # IE: {'In hand': True, "In auto": False}

    result_dict = {}
    # Iterate through unknown number of objects
    for argument in args:
        result_dict[argument.name] = argument.value

    # Append a timestamp 
    now = datetime.now()
    result_dict["timestamp"] = now.strftime("%m/%d/%Y, %H:%M:%S")

    # Result dict = {"In Hand": True, ...., "timestamp": "04/24/2024, 3:37:15"}
    return result_dict


def send_data_to_webserver(data_dict, session):
    # Convert from python dict to JSON string
    # to be able to send to our django web server
    json_string = json.dumps(data_dict)

    # This is the site you are trying to send to
    site_url = 'http://localhost:8000/receive-stepper-data/'
    site_url2 = 'http://localhost:8000/receive-splinter-data/'

    # These are some headers for your browser, I wouldn't worry about these
    headers = {'User-Agent': 'Mozilla/5.0'}

    # This is sending the data to the webserver
    r = session.post(site_url, data=json_string, headers=headers)
    r2 = session.post(site_url2, data=json_string, headers=headers)

    # This is the webservers response, which if it is working
    # should be a response code of 200
    print(r.status_code)
    print(r2.status_code)



def main():
    tag_dict = {}
    
    # Create a session with our webserver to speed things up
    session = requests.Session()

    # Create our click PLC connection object
    brx_plc_connection = connect_to_brx_plc()
    
    # in_auto = plc_tag("In Auto", 41, None)
    retro_1 = plc_tag("Retro_1", 5, None)
    e_stop = plc_tag("E_Stop", 9, None)
    start_stop = plc_tag("Start_Stop", 31, None)
    reject_motor = plc_tag("Reject Motor", 32, None)
    led_lights = plc_tag("LED Lights", 33, None)
    hall_effect = plc_tag("Hall Effect", 8, None)
    machine_vision = plc_tag("Machine Vision", 37, None) 
    # Create our objects for each PLC tag
    # in_auto = plc_tag("In Auto", 16385, None)
    # in_hand = plc_tag("In Hand", 16386, None)
    # e_stop = plc_tag("E-Stop", 16387, None)
    # motor_pulse_feedback = plc_tag("Motor Pulse Feedback", 16388, None)
    # motor_direction_feedback = plc_tag("Motor Direction Feedback", 16389, None)
    # motor_pulse_control = plc_tag("Motor Pulse Control", 16390, None)
    # motor_direction_control = plc_tag("Motor Direction Control", 16391, None)

    # Use this for changing stepper motor direction
    # count = 0

    while True:
        retro_data = read_coils(brx_plc_connection, retro_1.modbus_address)
        retro_1.value = retro_data[0]

        e_stop_data = read_coils(brx_plc_connection, e_stop.modbus_address)
        e_stop.value = e_stop_data[0]

        start_stop_data = read_coils(brx_plc_connection, start_stop.modbus_address)
        start_stop.value = start_stop_data[0]   
        
        reject_motor_data = read_coils(brx_plc_connection, reject_motor.modbus_address)
        reject_motor.value = reject_motor_data[0]

        led_lights_data = read_coils(brx_plc_connection, led_lights.modbus_address)
        led_lights.value = led_lights_data[0]

        hall_effect_data = read_coils(brx_plc_connection, hall_effect.modbus_address)
        hall_effect.value = hall_effect_data[0]
        
        machine_vision_data = read_coils(brx_plc_connection, machine_vision.modbus_address)
        machine_vision.value = machine_vision_data[0]

        # print(retro_1.value, e_stop.value, start_stop.value, reject_motor.value, 
        #        led_lights.value, hall_effect.value, machine_vision.value
        #       )

    # Run forever
    # while True:
    #     # Read the selector switch and E-Stop coils
    #     data = read_coils(click_plc_connection, in_auto.modbus_address, 7)
    #     in_auto.value = data[0]
    #     in_hand.value = data[1]
    #     e_stop.value = data[2]
    #     motor_pulse_feedback.value = data[3]
    #     motor_direction_feedback.value = data[4]
    #     motor_pulse_control.value = data[5]
    #     motor_direction_control.value = data[6]

    #     # Pulse the stepper motor
    #     if in_auto.value is True and e_stop.value is False:
    #         pulse_stepper(click_plc_connection, motor_pulse_control)
    #         count += 1
    #         if count == 200:
    #             count = 0
    #             change_motor_direction(click_plc_connection, motor_direction_feedback, motor_direction_control)

    #     if in_hand.value is True and e_stop.value is False:
    #         print("In hand")

    #     # setup tag dictionary with unlimited arguments
        tag_dict = create_data_structure_for_cache(
                                            retro_1,
                                            e_stop,
                                            start_stop,
                                            reject_motor,
                                            led_lights,
                                            hall_effect,
                                            machine_vision
                                        )
        send_data_to_webserver(tag_dict, session)

    # close_connection_to_click(click_plc_connection)


if __name__ == '__main__':
    main()
