# Extracting Colors from an Image using Cologram

import colorgram as cg

def extract_colors(image_path):
    extract_colors = cg.extract(image_path, 30)
    rgb_colors = []
    for color in extract_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        rgb_colors.append((r, g, b))
    
    rgb_colors = remove_white_colors(rgb_colors)

    return rgb_colors   

def remove_white_colors(color_list):
    filtered_colors = [color for color in color_list if not (color[0] > 200 and color[1] > 200 and color[2] > 200)]
    return filtered_colors