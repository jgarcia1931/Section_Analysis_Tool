import matplotlib.pyplot as plt, mpld3
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import pandas as pd

def initializeAnalysis(shapes):

    def section_properties(test):
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
            areax = basex * heightx
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


        return Iox_all, Ioy_all, xbar_cg, ybar_cg, sums_x["Ay"], sums_y["Ax"]

    # shapes is and array of [ [lower left corner, base, height] ]
    def plot_shapes(shapes):
        Iox_all, Ioy_all, xbar_cg, ybar_cg, Ay, Ax = section_properties(shapes)

        fig, ax = plt.subplots(1)
        patches = []

        max_x = .5
        max_y = .5

        for i in shapes:
            rect = Rectangle( i[0], i[1], i[2])
            if (i[0][0] + i[1]) > max_x:
                max_x = (i[0][0] + i[1])
            if (i[0][1] + i[2]) > max_y:
                max_y = (i[0][1] + i[2])
            patches.append(rect)

        ax.axhline(y=ybar_cg, color='r')
        ax.axvline(x=xbar_cg, color='r')

        p = PatchCollection(patches, facecolors='none', edgecolor='m')
        ax.add_collection(p)
        ax.set_xlim([0, max_x * 1.3])
        ax.set_ylim([0, max_y * 1.3])
        # plt.show()
        # html_fig = mpld3.fig_to_html(fig=fig)
        html_fig = "holder"

        data = np.array([Iox_all, Ioy_all, xbar_cg, ybar_cg, Ay, Ax])
        sec_props = pd.Series(data, index=["Iox_all", "Ioy_all", "xbar_cg", "ybar_cg", "Ay", "Ax"])

        return  sec_props, html_fig

    def split_shape(test, C_divider):
        upper = []
        lower = []

        # Upper Lower
        for i in range(len(test)):
            x_orig = test[i][0][0]
            y_orig = test[i][0][1]
            base   = test[i][1]
            height = test[i][2]
            x_max  = x_orig + base
            y_max  = y_orig + height

            if (C_divider < y_orig) & (y_max > C_divider):
                upper.append(test[i])
            elif (C_divider > y_orig) & (y_max < C_divider):
                lower.append((test[i]))
            elif (C_divider < y_max) & (C_divider > y_orig):
                # print("Shape " + str(i + 1) + " needs to be divided")

                # Upper Shape
                new_origin = (x_orig, C_divider)
                new_base   = base
                new_height = (height + y_orig) - C_divider
                upper.append([new_origin, new_base, new_height])

                # Lower Shape
                new_origin = (x_orig, y_orig)
                new_base   = base
                new_height = C_divider - y_orig
                lower.append([new_origin, new_base, new_height])

        return upper, lower

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

    # test = [[(0.50,    0), 1.00, 0.30],
    #         [(0.85,  0.3), 0.30, 2.40],
    #         [(0   ,  2.7), 2.00, 0.30]]

    # print("********************************")
    # print("Original Shape")
    originalShapeProps, htmlOriginal = plot_shapes(shapes)
    # print("********************************")

    #Split Shapes
    upper, lower = split_shape(shapes, 2)

    # print("Upper Shape")
    upperShapeProps, htmlUpper = plot_shapes(list(upper))
    # print("********************************")

    # print("Lower Shape")
    lowerShapeProps, htmlLower = plot_shapes(list(lower))
    # print("********************************")

    # print("Upper Mirrored Shape")
    upper_mirrored = upper_mirror(list(upper), 2)
    upperMirroredProps, htmlUpperMirrored = plot_shapes(upper_mirrored)
    # print("********************************")

    # print("Lower Mirrored Shape")
    lower_mirrored = lower_mirror(list(lower), 2)
    lowerMirroredProps, htmlLowerMirrored = plot_shapes(lower_mirrored)
    # print("********************************")

    result = { "analysis": {
        "OriginalShape": {
            "props": originalShapeProps.to_dict(),
            "html": htmlOriginal,
            "geom": shapes
        },

        "Upper": {
            "props": upperMirroredProps.to_dict(),
            "html": htmlUpper,
            "geom": upper
        },
        "Lower": {
            "props": lowerShapeProps.to_dict(),
            "html": htmlLower,
            "geom": lower
        },
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
    return result
