import screen_brightness_control as sbc

def set_low_brightness():
    try:
        sbc.set_brightness(30)
        return "Brightness reduced to 30 percent"
    except Exception as e:
        return "Unable to control brightness"

def set_high_brightness():
    try:
        sbc.set_brightness(80)
        return "Brightness increased"
    except:
        return "Unable to control brightness"