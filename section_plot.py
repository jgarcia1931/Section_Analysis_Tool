import matplotlib.pyplot as plt, mpld3
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import pandas as pd
import json

def initializeAnalysis(shapes):

    def section_properties(test, mirror=False, xbar_init=0, ybar_init=0):
        columns = ["el", "base", "height", "Area", "xbar", "Ax", "Ax^2", "Ioy"]
        data_y = pd.DataFrame(columns=columns)

        # Y moment
        for i in range(len(test)):
            basey = test[i][1]
            heighty = test[i][2]
            areay = basey * heighty
            xbar = test[i][0][0] + basey / 2
            Ax = areay * xbar
            Ax_sq = Ax * xbar
            Ioy = (heighty * basey**3) / 12

            data_y.at[i, "el"] = i + 1
            data_y.at[i, "base"] = basey
            data_y.at[i, "height"] = heighty
            data_y.at[i, "Area"] = areay
            data_y.at[i, "xbar"] = xbar
            data_y.at[i, "Ax"] = Ax
            data_y.at[i, "Ax^2"] = Ax_sq
            data_y.at[i, "Ioy"] = Ioy

        # Sum all columns
        sums_y = data_y.sum(axis=0)
        xbar_cg = sums_y["Ax"] / sums_y["Area"]
        Ioy_all = sums_y["Ioy"] + sums_y["Ax^2"] - xbar_cg * sums_y["Ax"]

        columns = ["el", "base", "height", "Area", "ybar", "Ay", "Ay^2", "Iox"]
        data_x = pd.DataFrame(columns=columns)

        # X moment
        for i in range(len(test)):
            basex = test[i][1]
            heightx = test[i][2]
            if(abs(ybar_init - (test[i][0][1] + heightx)) < 0.01 or ybar_init > test[i][0][1] + heightx):
                continue
            areax = basex * heightx
            if(mirror==True):
                ybarx = (test[i][0][1] + heightx / 2) - ybar_init
                Ay_x = areax * ybarx
                Ay_sqx = Ay_x * ybarx
            else:
                ybarx = test[i][0][1] + heightx / 2
                Ay_x = areax * ybarx
                Ay_sqx = Ay_x * ybarx
            Iox = (basex * heightx**3) / 12

            data_x.at[i, "el"] = i + 1
            data_x.at[i, "base"] = basex
            data_x.at[i, "height"] = heightx
            data_x.at[i, "Area"] = areax
            data_x.at[i, "ybar"] = ybarx
            data_x.at[i, "Ay"] = Ay_x
            data_x.at[i, "Ay^2"] = Ay_sqx
            data_x.at[i, "Iox"] = Iox

        # Sum all columns
        sums_x = data_x.sum(axis=0)
        ybar_cg = sums_x["Ay"] / sums_x["Area"]
        Iox_all = sums_x["Iox"] + sums_x["Ay^2"] - ybar_cg * sums_x["Ay"]

        # print("Iox     = {:.4f}".format(Iox_all))
        # print("Ioy     = {:.4f}".format(Ioy_all))
        # print("xbar_cg = {:.4f}".format(xbar_cg))
        # print("ybar_cg = {:.4f}".format(ybar_cg))
        # print("Ay      = {:.4f}".format(sums_x["Ay"]))
        # print("Ax      = {:.4f}".format(sums_y["Ax"]))

        if(mirror==True):
            return sums_x["Ay"], sums_y["Ax"]

        return Iox_all, Ioy_all, xbar_cg, ybar_cg, sums_x["Ay"], sums_y["Ax"], sums_x["Area"], sums_y["Area"]

    # shapes is and array of [ [lower left corner, base, height] ]
    def plot_shapes(shapes, max_x_init=0, max_y_init=0, mirror=False):
        Iox_all, Ioy_all, xbar_cg, ybar_cg, Ay, Ax, Area_x, Area_y = section_properties(shapes)

        if(mirror==True):
            Ay, Ax = section_properties(shapes, mirror=mirror, xbar_init=xbar_cg, ybar_init=ybar_cg)

        if(max_x_init > 0):
            max_x = max_x_init
        else:
            max_x = 0
        if(max_y_init > 0):
            max_y = max_y_init
        else:
            max_y = 0
        min_x = 9999.0
        min_y = 9999.0

        for i in shapes:
            if (i[0][0] + i[1]) > max_x:
                max_x = (i[0][0] + i[1])
            if (i[0][1] + i[2]) > max_y:
                max_y = (i[0][1] + i[2])
            if (i[0][0]) < min_x:
                min_x = (i[0][0])
            if (i[0][1]) < min_y:
                min_y = (i[0][1])

        first_moment_y = 2*Ay*(max_y-min_y)*.5 / Iox_all

        fig, ax = plt.subplots(1)
        patches = []

        for i in shapes:
            rect = Rectangle( i[0], i[1], i[2])
            patches.append(rect)

        ax.axhline(y=ybar_cg, color='r')
        ax.axvline(x=xbar_cg, color='r')

        p = PatchCollection(patches, facecolors='none', edgecolor='m')
        ax.add_collection(p)
        ax.set_xlim([0, max_x * 1.3])
        ax.set_ylim([0, max_y * 1.3])
        plt.show()
        # html_fig = mpld3.fig_to_html(fig=fig)
        html_fig = "holder"

        data = np.array([Iox_all, Ioy_all, xbar_cg, ybar_cg, Ay, Ax, max_x, max_y])
        sec_props = pd.Series(data, index=["Iox_all", "Ioy_all", "xbar_cg", "ybar_cg", "Ay", "Ax", "max_x", "max_y"])

        if(max_x_init > 0):
            return sec_props, html_fig

        return  sec_props, html_fig, max_x, max_y,

    def split_shape(test, Y_divider, X_divider):
        upper = []
        lower = []
        left  = []
        right = []

        # Upper Lower
        for i in range(len(test)):
            x_orig = test[i][0][0]
            y_orig = test[i][0][1]
            base   = test[i][1]
            height = test[i][2]
            x_max  = x_orig + base
            y_max  = y_orig + height

            if (Y_divider < y_orig) & (Y_divider < y_max):
                upper.append(test[i])
            elif (Y_divider > y_orig) & (Y_divider > y_max):
                lower.append((test[i]))
            elif (Y_divider < y_max) & (Y_divider > y_orig):
                # Upper Shape
                new_origin = (x_orig, Y_divider)
                new_base   = base
                new_height = (height + y_orig) - Y_divider
                upper.append([new_origin, new_base, new_height])
                # Lower Shape
                new_origin = (x_orig, y_orig)
                new_base   = base
                new_height = Y_divider - y_orig
                lower.append([new_origin, new_base, new_height])

        # Left Right
        for i in range(len(test)):
            x_orig = test[i][0][0]
            y_orig = test[i][0][1]
            base   = test[i][1]
            height = test[i][2]
            x_max  = x_orig + base
            y_max  = y_orig + height

            if (X_divider < x_orig) & (X_divider < x_max):
                right.append(test[i])
            elif (X_divider > x_orig) & (X_divider > x_max):
                left.append((test[i]))
            elif (X_divider < x_max) & (X_divider > x_orig):
                # Right Shape
                new_origin = (X_divider, y_orig)
                new_base   = (base + x_orig) - X_divider
                new_height = height
                right.append([new_origin, new_base, new_height])
                # Left Shape
                new_origin = (x_orig, y_orig)
                new_base   = X_divider - x_orig
                new_height = height
                left.append([new_origin, new_base, new_height])

        Iox_all_up, Ioy_all_up, xbar_cg_up, ybar_cg_up, Ay_up, Ax_up, Area_x_up, Area_y_up = section_properties(upper)
        Iox_all_low, Ioy_all_low, xbar_cg_low, ybar_cg_low, Ay_low, Ax_low, Area_x_low, Area_y_low = section_properties(lower)
        Iox_all_right, Ioy_all_right, xbar_cg_right, ybar_cg_right, Ay_right, Ax_right, Area_x_right, Area_y_right = section_properties(right)
        Iox_all_left, Ioy_all_left, xbar_cg_left, ybar_cg_left, Ay_left, Ax_left, Area_x_left, Area_y_left = section_properties(left)

        tollerance = abs(Area_x_up - Area_x_low)
        # if(tollerance < 0.005):
        #     return upper, lower, right, left, Y_divider, X_divider
        if( (Area_x_up - Area_x_low) > 0.005 and (Area_x_up - Area_x_low) > 0 ):
            upper, lower,  right, left, Y_divider, X_divider = split_shape(test, Y_divider + 0.01)
        elif ( (Area_x_low - Area_x_up) > 0.005 and (Area_x_up - Area_x_low) > 0 ):
            upper, lower,  right, left, Y_divider, X_divider = split_shape(test, Y_divider - 0.01)

        tollerance2 = abs(Area_x_right - Area_x_left)
        if(tollerance2 < 0.005 * tollerance < 0.005):
            return upper, lower, right, left, Y_divider, X_divider
        if( (Area_x_right - Area_x_left) > 0.005 and (Area_x_right - Area_x_left) > 0 ):
            upper, lower,  right, left, Y_divider, X_divider = split_shape(test, Y_divider, X_divider + 0.01)
        elif ( (Area_x_left - Area_x_right) > 0.005 and (Area_x_right - Area_x_left) > 0 ):
            upper, lower,  right, left, Y_divider, X_divider = split_shape(test, Y_divider, X_divider - 0.01)


        return upper, lower, right, left, Y_divider, X_divider

    def upper_mirror(upper, C_divider):
        # x stays the same
        # New Y
        lower_mirror = []
        for i in upper:
            x_orig   = i[0][0]
            y_orig   = i[0][1]
            height   = i[2]
            y_mirror = C_divider - ((y_orig + height) - C_divider)
            origin_mirror = (x_orig, y_mirror)
            base_mirror   = i[1]
            height_mirror = i[2]
            lower_mirror.append([origin_mirror, base_mirror, height_mirror])
        for i in lower_mirror:
            upper.append(i)
        return upper

    def lower_mirror(lower, C_divider):
        # x stays the same
        # New Y
        upper_mirror = []
        for i in lower:
            x_orig   = i[0][0]
            y_orig   = i[0][1]
            height   = i[2]
            y_mirror = (C_divider - (y_orig + height)) + C_divider
            origin_mirror = (x_orig, y_mirror)
            base_mirror   = i[1]
            height_mirror = i[2]
            upper_mirror.append([origin_mirror, base_mirror, height_mirror])
        for i in upper_mirror:
            lower.append(i)
        return lower

    print("********************************")
    print("Original Shape")
    originalShapeProps, htmlOriginal, max_x, max_y = plot_shapes(shapes)
    print("********************************")

    #Split Shapes
    upper, lower, right, left, Y_divider, X_divider = split_shape(shapes, 2, 1)

    print("Upper Shape")
    upperShapeProps, htmlUpper = plot_shapes(list(upper),max_x, max_y)
    print("********************************")

    print("Lower Shape")
    lowerShapeProps, htmlLower = plot_shapes(list(lower),max_x, max_y)
    print("********************************")

    print("Right Shape")
    upperShapeProps, htmlUpper = plot_shapes(list(right),max_x, max_y,)
    print("********************************")

    print("Left Shape")
    lowerShapeProps, htmlLower = plot_shapes(list(left),max_x, max_y,)
    print("********************************")

    print("Upper Mirrored Shape")
    upper_mirrored = upper_mirror(list(upper), Y_divider)
    upperMirroredProps, htmlUpperMirrored = plot_shapes(upper_mirrored, max_x, max_y, mirror=True)
    print("********************************")

    print("Lower Mirrored Shape")
    lower_mirrored = lower_mirror(list(lower), Y_divider)
    lowerMirroredProps, htmlLowerMirrored = plot_shapes(lower_mirrored, max_x, max_y, mirror=True)
    print("********************************")

    

    result = { "analysis": {
        "OriginalShape": {
            "props": originalShapeProps.to_dict(),
            "html": htmlOriginal,
            "geom": shapes
        },

        # "Upper": {
        #     "props": upperShapeProps.to_dict(),
        #     "html": htmlUpper,
        #     "geom": upper
        # },
        # "Lower": {
        #     "props": lowerShapeProps.to_dict(),
        #     "html": htmlLower,
        #     "geom": lower
        # },
        "UpperMirroredProps": {
            "props": upperMirroredProps.to_dict(),
            "html": htmlUpperMirrored,
            "geom": upper_mirrored
        },
        "LowerMirroredProps": {
            "props": lowerMirroredProps.to_dict(),
            "html": htmlLowerMirrored,
            "geom": lower_mirrored
        }
    }}
    print(json.dumps(result, indent=2))
    return result

test = [[(0.50,    0), 1.00, 0.30],
        [(0.85,  0.3), 0.30, 2.40],
        [(0   ,  2.7), 2.00, 0.30]]

initializeAnalysis(test)
