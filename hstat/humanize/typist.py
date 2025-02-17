from random import randint
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

import time

_EST_LOOP_OVRHEAD: int = 39

_MIN_KEY_DELAY_MS: int = 52 - _EST_LOOP_OVRHEAD
_MAX_KEY_DELAY_MS: int = 76 - _EST_LOOP_OVRHEAD
_KEY_INPUT_ACCURACY_PCNT: int = 89


def humanize_send(input_element: WebElement, *values: str):
    """Simulates human typing inaccuracy and consistency for a Selenium webdriver

    Args:
        input_element (WebElement): Selenium WebElement that accepts inputs
        values (str): The string to be input

    Example:
        form_input = driver.find_element(By.ID,"First-Name")\n
        humanize_send(form_input,"Nattah-Boht")
    """
    for value in values:
        keystroke = 0

        errors = 0
        fixed = 0

        max_errors = max(int(0.3*len(value)),1)
        start_time = time.time()
        while keystroke < len(value):
            delay_ms = randint(_MIN_KEY_DELAY_MS,_MAX_KEY_DELAY_MS)
            key_attmpt = value[keystroke]

            # Roll to send correct char
            # If there are errors to correct, roll to fix them
            if errors < max_errors:
                roll = randint(0,100)
            else:
                roll = -1

            accurate_keystroke = roll <= _KEY_INPUT_ACCURACY_PCNT


            # TODO implement deletion errors

            if accurate_keystroke and errors == fixed:              # no errors >> good keystroke
                input_element.send_keys(key_attmpt)
                keystroke += 1
            elif accurate_keystroke and errors > fixed:             # errors >> good keystroke
                input_element.send_keys(Keys.BACK_SPACE)
                fixed += 1
            elif not accurate_keystroke and errors > fixed:         # errors >> bad keystroke
                input_element.send_keys(key_attmpt)
                errors += 1
            else:                                                   # no errors >> bad keystroke
                input_element.send_keys(chr(ord(key_attmpt)+1)) 
                errors += 1
            
            time.sleep(delay_ms/1000)
    final = time.time()-start_time
    # print(f"Loop time ran {final} for a total of {final/len(values[0])} per iteration")
    return

__all__ = ["humanize_send"]