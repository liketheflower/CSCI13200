# reference code for part C 1 problem
import collections
def favorite_car_color(car_colors):
    cnt = collections.Counter(car_colors)
    color_cnt = list(cnt.items())
    max_color = max(color_cnt, key = lambda x:x[1])
    return max_color[0]
car_colors = ['white', 'grey', 'white', 'grey', 'black', 'silver', 'green', 'black', 'white']
favorite_color = favorite_car_color(car_colors)
print("Alex's neighbors' favoriate car color is: ", favorite_color)
