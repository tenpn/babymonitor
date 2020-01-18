"""
Messing around with sensehat.
"""
from time import sleep
import math
from sense_hat import SenseHat

C_PER_BLOCK = 1.5
MIN_TEMP = 15.5
MAX_TEMP = MIN_TEMP + C_PER_BLOCK*8
MIN_GOOD_TEMP = 20
MAX_GOOD_TEMP = MIN_GOOD_TEMP + C_PER_BLOCK*2

def alpha(min_val, max_val, val):
    """Return 0-1 where 0 val==min_val and 1 val==max_val. Does not clamp."""
    return (val-min_val)/(max_val-min_val)

def get_col_for_temp(temp):
    """Returns a suitable (r,g,b) color for this C temp."""
    if temp >= MAX_GOOD_TEMP:
        hot_alpha = alpha(MAX_GOOD_TEMP, MAX_TEMP, temp)
        return (math.floor(hot_alpha*255), math.floor((1-hot_alpha)*255), 0)
    elif temp >= MIN_GOOD_TEMP:
        return (0, 255, 0)
    else:
        good_alpha = alpha(MIN_TEMP, MIN_GOOD_TEMP, temp)
        return (0, math.floor(good_alpha*255), math.floor((1-good_alpha)*255))

def draw_temp_scale_in_col(x, sense):
    """Draws the scale on the right"""
    for y in range(8):
        gague_temp = MIN_TEMP+y*C_PER_BLOCK
        gague_col = (255, 0, 0) if gague_temp >= MAX_GOOD_TEMP \
            else (0, 255, 0) if gague_temp >= MIN_GOOD_TEMP \
                 else (0, 0, 255)
        sense.set_pixel(x, 7-y, gague_col)
    
def draw_temp_in_col(x, new_temp, sense):
    """Draws the temp gauge."""
    clean_temp = max(MIN_TEMP, min(MAX_TEMP, new_temp))
    col = get_col_for_temp(clean_temp)
    fill_to_y = math.floor(alpha(MIN_TEMP, MAX_TEMP, clean_temp)*8)
    # 00 is top left
    for y in range(8):
        p_col = col if y <= fill_to_y else (0, 0, 0)
        sense.set_pixel(x, 7-y, p_col)

def main():
    """loops the hat"""
    sense = SenseHat()
    sense.low_light = True
    c_hist = []

    while True:
        sense.clear()
        draw_temp_scale_in_col(7, sense)
        current_temp = sense.get_temperature()
        print(current_temp)
        c_hist.append(current_temp)
        if len(c_hist) > 7:
            c_hist.pop(0)
        for i in range(min(len(c_hist), 7)):
            current_c_hist = c_hist[-(i+1)]
            draw_temp_in_col(6-i, current_c_hist, sense)

        sleep(5)

if __name__ == "__main__":
    main()
